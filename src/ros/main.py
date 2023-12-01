import rclpy
from subscribers.control_robot import ControlTurltebot

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ControlTurltebot()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()