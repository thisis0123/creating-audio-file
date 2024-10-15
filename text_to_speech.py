import pyttsx3

engine=pyttsx3.init()

engine.save_to_file("hello world","hello world.mp3")

engine.runAndWait()

engine.stop()