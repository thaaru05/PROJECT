import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text you want to convert to speech
text = "Hello, this is a text-to-speech example."

# Convert text to speech
engine.say(text)

# Play the generated speech
engine.runAndWait()
