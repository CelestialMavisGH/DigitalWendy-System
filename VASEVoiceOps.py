import AudioCloudOp as AudCloud
import AudioRecordMic as AudRec
import speech_recognition as spcrec
import VASE_TTS as vtts
from pydub import AudioSegment
from pydub.playback import play
import time

# This variable is actually just to initiate the program and keep it running,
# I will update this later with something better
global beginop
beginop = ""

# This is the main function that calls all the other functions
def mainOps():
    
   while beginop != "Quit" or "Exit":
       # This function calls the AudioRecordMic.py script which starts recording your mic
     AudRec.beginRecord()
       # This function sends the file thats been recorded above to the google cloud for transcription
     AudCloud.beginTranscribe()
       # This function calls the Voice to Speech function in VaseTTS which "In theory" should
       # read out commands out loud, it's not fully functional at the moment
     vtts.VaseTTS(AudCloud.returncommandname())


# I'm using this global variable to run a while loop on the listening so that it continues to listen
# as long as the program is running, I will add another option to tell it to quit once the var changes
# to True
global listentome
listentome = False

# Listen for Keyword from Microphone!
recog = spcrec.Recognizer()

# This is the keyword that will be used to activate the system in this case its "v command"
cmdwrd = 'v command'
# This is the keyword that will cause the program to quit
cmdwrdqt = 'command quit'

# This while loop listens for the keyword and then executes main() if it's detected
while listentome == False:

 with spcrec.Microphone() as source:
     
    print(f"Please say {cmdwrd} to speak with VASE or say {cmdwrdqt} to End the program")
    # The variable below dictates what VASE TTS says upon startup
    whattosay = f"Please say {cmdwrd} to speak with VASE or say {cmdwrdqt} to End the program"
    # Sending the variable to the TTS function in order to create an MP3 file of the text and play it
    vtts.VaseTTS(whattosay)
    # Attempted to call the function again using different text but it doesn't function yet
    vso = "vase online"
    #Currently the TTS command can only be called once, I haven't figured out why yet
    #vtts.VaseTTS(vso)

    # Code below continues to listen to what you say and does something when it hears the keyword
    while True:
        audio = recog.listen(source)
        try:
            wrds = recog.recognize_google(audio)
            if cmdwrd.lower() in wrds.lower():
                print('Keyword detected in the speech.')
                TTS = AudioSegment.from_mp3("audio/speakping.mp3")
                quieter_tts = TTS - 10
                play(quieter_tts)
                mainOps()
            elif cmdwrdqt.lower() in wrds.lower():
                quit()
                
        except Exception as e:
            print('Please speak again.')

