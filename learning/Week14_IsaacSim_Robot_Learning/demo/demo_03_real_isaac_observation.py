"""Isaac Sim 5.1 real track: build/load a scene and report observation metadata."""
from __future__ import annotations

import argparse
import time


def parse_args():
    p = argparse.ArgumentParser(
        description="Launch Isaac Sim, collect RGB/depth/robot state, and print ground truth."
    )
    p.add_argument("--headless", action="store_true")
    p.add_argument("--stage", help="Optional local or Nucleus USD stage; omitted builds the default scene.")
    p.add_argument("--robot-prim", default="/World/Robot")
    p.add_argument("--camera-prim", default="/World/Camera")
    p.add_argument(
        "--robot-asset",
        help="Optional Franka USD path. The default resolves from the Isaac Sim assets root.",
    )
    p.add_argument("--steps", type=int, default=120)
    p.add_argument("--seed", type=int, default=7)
    return p.parse_args()


def add_default_scene(world, args, np):
    """Create ground, Franka, camera, target, and light for a zero-asset-path launch."""
    import isaacsim.core.utils.stage as stage_utils
    from isaacsim.core.api.objects import DynamicCuboid
    from isaacsim.core.utils.nucleus import get_assets_root_path
    from isaacsim.sensors.camera import Camera
    from pxr import Gf, UsdGeom, UsdLux

    world.scene.add_default_ground_plane()
    assets_root = get_assets_root_path()
    if not assets_root and not args.robot_asset:
        raise RuntimeError(
            "Isaac Sim assets root is unavailable. Check Nucleus/network access or pass --robot-asset."
        )
    robot_asset = args.robot_asset or (
        assets_root + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
    )
    stage_utils.add_reference_to_stage(usd_path=robot_asset, prim_path=args.robot_prim)
    target = world.scene.add(
        DynamicCuboid(
            prim_path="/World/Target",
            name="target",
            position=np.array([0.55, 0.0, 0.05]),
            scale=np.array([0.08, 0.08, 0.10]),
            color=np.array([0.85, 0.15, 0.10]),
        )
    )
    camera = Camera(
        prim_path=args.camera_prim,
        name="research_camera",
        position=np.array([1.25, 1.25, 1.05]),
        frequency=20,
        resolution=(640, 480),
        orientation=np.array([0.36, 0.12, 0.28, 0.88]),
    )
    world.scene.add(camera)
    stage = stage_utils.get_current_stage()
    light = UsdLux.DistantLight.Define(stage, "/World/KeyLight")
    light.CreateIntensityAttr(1600.0)
    light.CreateAngleAttr(1.0)
    UsdGeom.Xformable(light.GetPrim()).AddRotateXYZOp().Set(Gf.Vec3f(-35.0, 25.0, 0.0))
    return camera, target, robot_asset


def bind_custom_scene(world, args):
    """Bind wrappers to prims supplied by a custom stage."""
    from isaacsim.core.prims import SingleArticulation
    from isaacsim.sensors.camera import Camera

    robot = world.scene.add(
        SingleArticulation(prim_path=args.robot_prim, name="research_robot")
    )
    camera = Camera(prim_path=args.camera_prim, name="research_camera")
    world.scene.add(camera)
    return robot, camera


def main():
    args = parse_args()
    from isaacsim import SimulationApp

    app = SimulationApp({"headless": args.headless})
    try:
        import numpy as np
        import isaacsim.core.utils.stage as stage_utils
        from isaacsim.core.api import World
        from isaacsim.core.prims import SingleArticulation

        np.random.seed(args.seed)
        if args.stage:
            stage_utils.open_stage(args.stage)
        world = World(stage_units_in_meters=1.0)
        if args.stage:
            robot, camera = bind_custom_scene(world, args)
            target = None
            robot_asset = "custom-stage"
        else:
            camera, target, robot_asset = add_default_scene(world, args, np)
            robot = world.scene.add(
                SingleArticulation(prim_path=args.robot_prim, name="research_robot")
            )
        world.reset()
        camera.initialize()
        started = time.perf_counter()
        for _ in range(args.steps):
            world.step(render=True)
        elapsed = time.perf_counter() - started
        rgb = camera.get_rgba()
        depth = camera.get_depth()
        joint_positions = robot.get_joint_positions()
        camera_position, camera_orientation = camera.get_world_pose()
        target_pose = target.get_world_pose() if target is not None else None
        physics_dt, rendering_dt = world.get_physics_dt(), world.get_rendering_dt()

        print("=== Sensor Observation ===")
        print(f"rgb_shape={getattr(rgb, 'shape', None)} rgb_dtype={getattr(rgb, 'dtype', None)}")
        print(f"depth_shape={getattr(depth, 'shape', None)} depth_dtype={getattr(depth, 'dtype', None)}")
        print(f"robot_state_shape={getattr(joint_positions, 'shape', None)}")
        print("=== Simulator Ground Truth ===")
        print(f"camera_position={np.asarray(camera_position).tolist()}")
        print(f"camera_orientation_wxyz={np.asarray(camera_orientation).tolist()}")
        print(f"target_pose={target_pose}")
        print(f"physics_dt={physics_dt} rendering_dt={rendering_dt}")
        print("=== Runtime Evidence ===")
        print(f"headless={args.headless} stage={args.stage or 'generated-default'} seed={args.seed}")
        print(f"robot_asset={robot_asset}")
        print(f"steps={args.steps} elapsed_seconds={elapsed:.3f} steps_per_second={args.steps/elapsed:.2f}")
        print("action_output=none; this demo observes only and never controls the robot")
        print("status=Executed only after this output is captured from Isaac Sim 5.1")
    finally:
        app.close()


if __name__ == "__main__":
    main()
