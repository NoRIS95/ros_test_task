#!/bin/bash

source /opt/ros/noetic/setup.bash

roscore &
python3 ./src/logger/logger.py &
python3 ./src/listener/listener.py &

# Wait for any process to exit
wait -n

exit $?