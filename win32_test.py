import win32com.client
import logging
logging.basicConfig(level=logging.DEBUG)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("How are you?")
	