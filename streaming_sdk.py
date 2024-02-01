from .connection_manager import ConnectionManager
from .audio_handler import AudioHandler


class StreamingSDK:
    def __init__(self):
        self.connection_manager = ConnectionManager()
        self.audio_handler = AudioHandler()

    def connect(self):
        self.connection_manager.connect()

    def disconnect(self):
        self.connection_manager.disconnect()

    def send_audio_chunk(self, chunk, format):
        processed_audio = self.audio_handler.process_audio_chunk(chunk, format)
        # Code to send the processed audio
        print(f"Sending processed audio: {processed_audio}")
