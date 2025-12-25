import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class DisplayNode(Node):
    def __init__(self):
        super().__init__('display_node')
        self.subscription = self.create_subscription(
            Float64MultiArray, 'weather_data', self.listener_callback, 10)
        # Timer to control printing frequency to every 2 seconds
        self.create_timer(2.0, self.print_callback)
        self.current_data = None

    def listener_callback(self, msg):
        self.current_data = msg.data

    def print_callback(self):
        if self.current_data:
            d = self.current_data
            print(f"Received 2x2 Matrix:\n[{d[0]:.2f}, {d[1]:.2f}]\n[{d[2]:.2f}, {d[3]:.2f}]\n")

def main(args=None):
    rclpy.init(args=args)
    node = DisplayNode()
    rclpy.spin(node)
    rclpy.shutdown()