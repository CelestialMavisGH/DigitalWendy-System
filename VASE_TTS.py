import os
from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play

  # Defining the local json key for the environment variable to access google's api
credential_path = "key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
client = texttospeech.TextToSpeechClient()

def VaseTTS(texttosay):

 # Set the text input to be synthesized
 synthesis_input = texttospeech.types.SynthesisInput(text=texttosay)

 # Build the voice request, select the language code ("en-US") and the ssml
 # voice gender ("Female")
 voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

 # Select the type of audio file you want returned
 audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

 # Perform the text-to-speech request on the text input with the selected
 # voice parameters and audio file type
 response = client.synthesize_speech(synthesis_input, voice, audio_config)

 # The response's audio_content is binary.
 with open('audio/output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    TTS = AudioSegment.from_mp3("audio/output.mp3")
    quieter_tts = TTS - 10
    play(quieter_tts)
    out.flush()
    out.close()