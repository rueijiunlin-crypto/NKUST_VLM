"""Print a layered ROS2 topic diagnostic checklist."""

CHECKS = [
    ("environment", "printenv ROS_DISTRO"),
    ("node discovery", "ros2 node list"),
    ("topic discovery", "ros2 topic list"),
    ("topic contract", "ros2 topic info /vlm/semantic_description -v"),
    ("payload", "ros2 topic echo /vlm/semantic_description"),
    ("rate", "ros2 topic hz /vlm/semantic_description"),
]


def main() -> None:
    for index, (purpose, command) in enumerate(CHECKS, start=1):
        print(f"{index}. {purpose}: {command}")


if __name__ == "__main__":
    main()
