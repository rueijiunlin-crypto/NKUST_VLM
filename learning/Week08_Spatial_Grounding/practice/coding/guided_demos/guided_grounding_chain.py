"""Guided Code Reading：追蹤 2D detection 到 robot-frame 3D point 的資料流。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PixelDetection:
    label: str
    u: float
    v: float
    depth_m: float


def deproject(detection: PixelDetection, fx: float, fy: float, cx: float, cy: float) -> tuple[float, float, float]:
    """用 pinhole camera model 將 pixel 與 depth 轉為 camera-frame point。"""
    x = (detection.u - cx) * detection.depth_m / fx
    y = (detection.v - cy) * detection.depth_m / fy
    return x, y, detection.depth_m


def translate_to_robot(
    camera_point: tuple[float, float, float],
    camera_in_robot: tuple[float, float, float],
) -> tuple[float, float, float]:
    """簡化示例只做平移；真實系統還需 rotation 與完整 homogeneous transform。"""
    return tuple(value + offset for value, offset in zip(camera_point, camera_in_robot))


def main() -> None:
    detection = PixelDetection(label="target_box", u=380.0, v=260.0, depth_m=1.2)
    intrinsics = {"fx": 600.0, "fy": 600.0, "cx": 320.0, "cy": 240.0}
    camera_in_robot = (0.20, 0.00, 0.55)

    print("Step 1 - semantic detection:", detection)
    camera_point = deproject(detection, **intrinsics)
    print("Step 2 - camera-frame XYZ:", tuple(round(v, 3) for v in camera_point))
    robot_point = translate_to_robot(camera_point, camera_in_robot)
    print("Step 3 - robot-frame XYZ:", tuple(round(v, 3) for v in robot_point))
    print("Step 4 - frame_id: base_link; units: meter")


if __name__ == "__main__":
    main()
