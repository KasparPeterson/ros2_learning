## Development setup for Mac Host

```shell
pip install rclpy-intellisense
```

## Setup for Ubuntu

```shell
rosdep install -r --from-paths src -i -y --rosdistro jazzy
colcon build
source install/setup.bash
```

## Run

kaspar_package:

```shell
ros2 run kaspar_package kaspar_node
```

py_pubsub:

```shell
ros2 run py_pubsub listener
ros2 run py_pubsub talker
```

py_srvcli:

```shell
ros2 run py_srvcli service
ros2 run py_srvcli client 123 456
```

python_parameters:

```shell
ros2 run python_parameters minimal_param_node
```

launch_tutorial:

```shell
cd src/launch_tutorial/launch
ros2 launch turtlesim_mimic_launch.py

# another terminal
ros2 topic pub -r 1 /turtlesim3/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"
```