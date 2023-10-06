# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        # Split the message into words
        words = msg.data.split()

        # Process and rebuild the message
        new_message_parts = []
        for word in words:
            if word.isdigit():
                # Convert numeric words to numeric symbols
                new_word = str(int(word))
            else:
                new_word = word
            new_message_parts.append(new_word)

        # Reconstruct and display the modified message
        modified_message = ' '.join(new_message_parts)
        self.get_logger().info(f'Chris heard: [ECE3432 -> {modified_message}]')

def main(args=None):
    rclpy.init(args=args)
    listener = ListenerNode()
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
