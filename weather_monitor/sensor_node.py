import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'weather_data', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data = [random.uniform(20.0, 30.0) for _ in range(4)]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Matrix: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()