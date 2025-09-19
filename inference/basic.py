import whisper

model = whisper.load_model("base")
result = model.transcribe("/Users/cmi_10128/Desktop/documents/projects/ASR/audio_files/speakerA.wav")
print(result["text"])