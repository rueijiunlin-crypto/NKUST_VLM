"""Isaac Sim real track: load a stage and report camera/robot observation metadata."""
import argparse
import time


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--headless", action="store_true")
    p.add_argument("--stage", help="Optional local or Nucleus USD stage.")
    p.add_argument("--robot-prim", default="/World/Robot")
    p.add_argument("--camera-prim", default="/World/Camera")
    p.add_argument("--steps", type=int, default=120)
    p.add_argument("--seed", type=int, default=7)
    return p.parse_args()


def main():
    args = parse_args()
    from isaacsim import SimulationApp
    app = SimulationApp({"headless": args.headless})
    try:
        import numpy as np
        import isaacsim.core.utils.stage as stage_utils
        from isaacsim.core.api import World
        from isaacsim.core.prims import Articulation
        from isaacsim.sensors.camera import Camera
        np.random.seed(args.seed)
        if args.stage:
            stage_utils.open_stage(args.stage)
        world = World(stage_units_in_meters=1.0)
        robot = Articulation(prim_paths_expr=args.robot_prim, name="research_robot")
        camera = Camera(prim_path=args.camera_prim, name="research_camera")
        camera.initialize()
        world.reset()
        started = time.perf_counter()
        for _ in range(args.steps):
            world.step(render=True)
        elapsed = time.perf_counter() - started
        rgb = camera.get_rgba()
        joint_positions = robot.get_joint_positions()
        print(f"headless={args.headless} stage={args.stage or 'empty'} seed={args.seed}")
        print(f"steps={args.steps} elapsed_seconds={elapsed:.3f} steps_per_second={args.steps/elapsed:.2f}")
        print(f"camera_shape={getattr(rgb, 'shape', None)} camera_dtype={getattr(rgb, 'dtype', None)}")
        print(f"robot_state_shape={getattr(joint_positions, 'shape', None)}")
        print("status=validated only when run inside the declared Isaac Sim environment")
    finally:
        app.close()


if __name__ == "__main__":
    main()
