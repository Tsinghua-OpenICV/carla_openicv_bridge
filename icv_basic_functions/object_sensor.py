#!/usr/bin/env python
#
# Copyright (c) 2019 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
handle a object sensor
"""

from derived_object_msgs.msg import ObjectArray
from vehicle import Vehicle
from walker import Walker
from pseudo_actor import PseudoActor
from icvPublisher import Publisher


class ObjectSensor(PseudoActor):

    """
    Pseudo object sensor
    """

    def __init__(self, parent, communication, actor_list, filtered_id):
        """
        Constructor
        :param carla_world: carla world object
        :type carla_world: carla.World
        :param parent: the parent of this
        :type parent: carla_icv_bridge.Parent
        :param communication: communication-handle
        :type communication: carla_icv_bridge.communication
        :param actor_list: current list of actors
        :type actor_list: map(carla-actor-id -> python-actor-object)
        :param filtered_id: id to filter from actor_list
        :type filtered_id: int
        """

        super(ObjectSensor, self).__init__(parent=parent,
                                           communication=communication,
                                           prefix='objects')
        self.actor_list = actor_list
        self.filtered_id = filtered_id
        self.pub1=Publisher(self.get_topic_prefix() )

    def destroy(self):
        """
        Function to destroy this object.
        :return:
        """
        self.actor_list = None
        super(ObjectSensor, self).destroy()

    def update(self, frame, timestamp):
        """
        Function (override) to update this object.
        On update map sends:
        - tf global frame
        :return:
        """
        icv_objects = ObjectArray(header=self.get_msg_header("map"))
        for actor_id in self.actor_list.keys():
            # currently only Vehicles and Walkers are added to the object array
            if self.filtered_id != actor_id:
                actor = self.actor_list[actor_id]
                if isinstance(actor, Vehicle):
                    icv_objects.objects.append(actor.get_object_info())
                elif isinstance(actor, Walker):
                    icv_objects.objects.append(actor.get_object_info())
        self.pub1.publish(icv_objects)
