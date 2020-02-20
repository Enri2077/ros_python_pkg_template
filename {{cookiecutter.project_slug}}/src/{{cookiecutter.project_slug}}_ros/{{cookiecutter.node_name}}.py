#!/usr/bin/env python

from __future__ import print_function

import rospy


class {{cookiecutter.class_name}}:
    def __init__(self):
        pass

    def image_filename(self, index):
            return self.image_file_format_string % index

    def info_filename(self, index):
            return self.info_file_format_string % index

    def create_subscriber(self):
        self.camera_sub_ = rospy.Subscriber(self.camera_topic, Image, self.image_callback)

    def image_callback(self, msg):
        if self.use_timestamps_file:
            if msg.header.stamp in self.timestamps:
                self.process_image(msg, self.timestamps[msg.header.stamp])
        else:
            self.image = msg

    def loop(self):
        rospy.spin()

