import io
import json
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Defining a local environmental variable for the program "key2.json" is in the programs directory
credential_path = "key2.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def beginTranscribe():
    print("Beginning Cloud Transcription")

    # Instantiates a client
    client = speech.SpeechClient()

    # Passes the name of the audio file to be transcribed
    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio',
        'aud.wav')

    # Loads the required audio file into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    # Setting the audio file details such as sample rate and encoding type in this case "Linear 16"
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    # Print the results to console as well as to File
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

        with open('Transcripts.txt', 'w') as file:
            for result in response.results:
                res = result.alternatives[0].transcript
                res.lower()
                res.casefold()
                file.write('Transcript: {}'.format(res.lower().casefold()) + '\n')

        file.close()
        
    print("Transcription Complete & File has been Saved!, Passing it over to Command Center!")
    checkForCommands()


global rcn
rcn = None

# This checks if any of the transcribed text contained any commands that can be executed by the code below

def checkForCommands():

# Attempting to use Json for a list of commands, not currently implemented
    with open("commands.json") as file:
        comms = json.load(file)

# Opens the file that contains the transcribed data sent back by the Google API
    flt = open('Transcripts.txt', 'r')
    
    if flt.mode == 'r':
        print("Im after flt.mode")
    # Opens the file and checks for keywords that might match commands to execute
        if "open" and "notepad" in flt.read():
            print("Opening Notepad")
            whattosay = "Opening Notepad"
            os.startfile(f'C:/Windows/system32/Notepad.exe')
            rcn = "Opening Notepad"
            print(rcn)
            #vtts.VaseTTS(whattosay)

        if "send" and "text" and "message" in flt.read():
            whattosay = "Sending text message"
            rcn = "Sending Text Message"
            print(whattosay)
            print(rcn)

    flt.flush()
    flt.close()

  # This is not implemented but it's meant as a work around or an attempted work around for the TTS
  # function, I was trying to create a global variable that will have the "Executing x Command" or so
def returncommandname():
    return rcn
