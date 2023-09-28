#!/bin/python3

import json

import requests
import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import rospy
from std_msgs.msg import String

import yaml
import os, sys
import yaml


# Load config
CURRENT_DIR = os.path.dirname(__file__)

with open(os.path.join(CURRENT_DIR, '../config.yml'), "r") as yamlfile:
    CONFIG = yaml.load(yamlfile, Loader=yaml.FullLoader)

QUEUE_SIZE = CONFIG['QUEUE_SIZE']
LISTENER_HOST = CONFIG['LISTENER_HOST']
LISTENER_PORT = CONFIG['LISTENER_PORT']
QUEUE_NAME = CONFIG['QUEUE_NAME']


# Setup broker and app

pub = rospy.Publisher(QUEUE_NAME, String, queue_size=QUEUE_SIZE)
rospy.init_node('log_topic_publisher')

app = FastAPI()


class LogItem(BaseModel):
    data: str


@app.post("/info")
async def process(req: LogItem):
    # new_data = json.dumps({"log": req.data})
    new_data = req.data
    # send to the queue (publisher) instead
    pub.publish(new_data)
    # requests.post(LOGGER_URL, new_data)

if __name__ == '__main__':
    uvicorn.run(app, host=LISTENER_HOST, port=LISTENER_PORT)
