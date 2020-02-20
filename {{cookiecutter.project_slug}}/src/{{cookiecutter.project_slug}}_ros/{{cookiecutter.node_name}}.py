#!/usr/bin/env python

from __future__ import print_function

import rospy
from std_msgs.msg import String


class {{cookiecutter.class_name}}:
    def __init__(self):
        pass

    def create_subscriber(self):
        self.sub_ = rospy.Subscriber(self.topic_name, String, self._callback)

    def _callback(self, msg):
        pass

    def loop(self):
        rospy.spin()

