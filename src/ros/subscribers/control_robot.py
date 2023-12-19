import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi

class ControlTurltebot(Node):

    def __init__(self):
        super().__init__('control_robot')

        self.nav = BasicNavigator()
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, 0.0)
        self.initial_pose = self.create_initial_pose()
        self.nav.setInitialPose(self.initial_pose)
        self.nav.waitUntilNav2Active()
        self.waypoints = []

        self.subscription = self.create_subscription(
            String,
            'publish_points',
            self.listener_callback,
            10)
        

    def create_initial_pose(self):
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.nav.get_clock().now().to_msg()
        initial_pose.pose.position.x = 0.0
        initial_pose.pose.position.y = 0.0
        initial_pose.pose.position.z = 0.0
        initial_pose.pose.orientation.x = self.q_x
        initial_pose.pose.orientation.y = self.q_y
        initial_pose.pose.orientation.z = self.q_z
        initial_pose.pose.orientation.w = self.q_w
        return initial_pose

    def create_pose_stamped(self, navigator, pos_x, pos_y, rot_z):
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, rot_z)
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.position.x = pos_x
        pose.pose.position.y = pos_y
        pose.pose.position.z = 0.0
        pose.pose.orientation.x = self.q_x
        pose.pose.orientation.y = self.q_y
        pose.pose.orientation.z = self.q_z
        pose.pose.orientation.w = self.q_w
        return pose

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.points = eval(msg.data)

        self.point = self.create_pose_stamped(self.nav, float(self.points[0]), float(self.points[1]), 0.0)
        self.waypoints.append(self.point)

        while len(self.waypoints) > 0:
            if self.nav.isTaskComplete():
                self.nav.followWaypoints(self.waypoints)
                self.waypoints.pop(0)
            else: 
                pass
                    


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ControlTurltebot()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()