#!/usr/bin/env python

#
# Copyright (c) 2018-2019 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
Classes to handle Carla vehicles
"""

from protocol.std_msgs.msg import ColorRGBA
from derived_object_msgs.msg import Object

from traffic_participant import TrafficParticipant


class Vehicle(TrafficParticipant):

    """
    Actor implementation details for vehicles
    """

    def __init__(self, carla_actor, parent, communication, prefix=None):
        """
        Constructor

        :param carla_actor: carla vehicle actor object
        :type carla_actor: carla.Vehicle
        :param parent: the parent of this
        :type parent: carla_icv_bridge.Parent
        :param communication: communication-handle
        :type communication: carla_icv_bridge.communication
        :param prefix: the topic prefix to be used for this actor
        :type prefix: string
        """

        if not prefix:
            prefix = "vehicle/{:03}".format(carla_actor.id)
        #print(prefix)
        self.classification = Object.CLASSIFICATION_CAR
        if carla_actor.attributes.__contains__('object_type'):
            if carla_actor.attributes['object_type'] == 'car':
                self.classification = Object.CLASSIFICATION_CAR
            elif carla_actor.attributes['object_type'] == 'bike':
                self.classification = Object.CLASSIFICATION_BIKE
            elif carla_actor.attributes['object_type'] == 'motorcycle':
                self.classification = Object.CLASSIFICATION_MOTORCYCLE
            elif carla_actor.attributes['object_type'] == 'truck':
                self.classification = Object.CLASSIFICATION_TRUCK
            elif carla_actor.attributes['object_type'] == 'other':
                self.classification = Object.CLASSIFICATION_OTHER_VEHICLE

        super(Vehicle, self).__init__(carla_actor=carla_actor,
                                      parent=parent,
                                      communication=communication,
                                      prefix=prefix)

    def update(self, frame, timestamp):
        """
        Function (override) to update this object.

        On update vehicles send:
        - tf global frame
        - object message
        - marker message

        :return:
        """
        #self.publish_transform(self.get_icv_transform())
        #print(self.get_icv_transform())
        #self.publish_marker()
        super(Vehicle, self).update(frame, timestamp)

    def get_marker_color(self):  # pylint: disable=no-self-use
        """
        Function (override) to return the color for marker messages.

        :return: the color used by a vehicle marker
        :rtpye : std_msgs.ColorRGBA
        """
        color = ColorRGBA()
        color.r = 255
        color.g = 0
        color.b = 0
        return color

    def get_classification(self):
        """
        Function (override) to get classification
        :return:
        """
        return self.classification
