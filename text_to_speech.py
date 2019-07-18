import pyttsx3

engine = pyttsx3.init() #initialise the speech engine

#getProperty(name : string) -Gets the current value of an engine property.
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')

print(rate)
print(volume)
print(voice)

# setProperty() Queues a command to set an engine property. The new property value affects all utterances queued after this command.

engine.setProperty('rate', 180)
engine.setProperty('volume', 2)

#to test all voices ->
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    print (voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

string =input("ENTER MESSSAGE: ")
engine.say(string)    # Queues a command to speak an utterance

engine.runAndWait()
# runAndWait() Blocks while processing all currently queued commands. Invokes callbacks for engine notifications
# appropriately. Returns when all commands queued before this call are emptied from the queue.

