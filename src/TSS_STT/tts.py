from std_msgs.msg import String, Float32MultiArray
from gtts import gTTS
import os

class TTSNode():
    def __init__(self, timer_period=0.2):
        super().__init__('tts_node')
        self.subscription_ = self.create_subscription(msg_type=String,topic="/chatbot",callback=self.chatbot_callback,qos_profile=10)
        self.get_logger().info("Ouvindo ao /chatbot")
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.message = None

    def timer_callback(self):
        if self.message:
            self.get_logger().info(f"Vou falar: {self.message}")
            self.audio = self.text_to_speech(self.message)
            self.play_audio(self.audio)
            self.message = None

    def chatbot_callback(self, msg):
        self.message = msg.data
        self.get_logger().info(f"Recebi: {self.message}")
    
    def text_to_speech(self, text, language='en'):
        self.tts = gTTS(text, lang=language)
        self.audio_file = "speech.mp3"
        self.tts.save(self.audio_file)
        return self.audio_file
    
    def play_audio(self, audio_file):
        os.system(f"mpg321 {audio_file}")

def main(args=None):
    tts_node = TTSNode()
    tts_node

if __name__ == "__main__":
    tts = gTTS(text="Olá mundo!", lang='pt-br')
    audio_file = "speech.mp3"
    tts.save(audio_file)
    os.system(f"mpg321 {audio_file}")