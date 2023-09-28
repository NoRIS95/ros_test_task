#!/bin/python3

from typing import Any

from pydantic import BaseModel, Json
import rospy
from std_msgs.msg import String
import os
import logging
import yaml


# Load config
CURRENT_DIR = os.path.dirname(__file__)

with open(os.path.join(CURRENT_DIR, '../config.yml'), "r") as yamlfile:
    CONFIG = yaml.load(yamlfile, Loader=yaml.FullLoader)

QUEUE_NAME = CONFIG['QUEUE_NAME']


logger = logging.getLogger("logger")


def callback(data):
    # We can use any
    logger.info(data)
    # rospy.loginfo(data)

def subscriber():
    rospy.init_node('log_topic_listener')
    rospy.Subscriber(QUEUE_NAME, String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()