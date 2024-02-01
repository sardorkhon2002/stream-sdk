class AudioHandler:
    def process_audio_chunk(self, chunk, chunk_format):
        # Process the audio chunk
        print(f"Processing audio chunk in format: {chunk_format}")
        # Example: Return a dummy processed result
        return {"processed_chunk": chunk, "format": chunk_format}
