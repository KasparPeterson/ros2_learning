## Setup

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
