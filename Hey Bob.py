import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')

#Change voice from female to male with 1 and 0
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

#Listening command
def take_command():
    try:
        with sr.Microphone() as source:
            print("I'm all ears...")
            talk('ding dong')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Bob' in command:
                command = command.replace('bob','')
                print(command)

    except:
        pass
    return command

#All Commands
def run_Bob():
    command = take_command()
    print(command)



#Music
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song + 'on youtube')
        pywhatkit.playonyt(song)

#Wikipedia
    elif'who is' in command:
        person = command.replace ('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)



#Time
    elif'time' in command:
        time = datetime.datetime.now().strftime("%H`%M %p")
        talk('The current time is' + time)
        print(time)



#Goofy stuff
    if 'are we friends' in command:
        are_we_friends = print('Never gonna give you up           Never gonna let you down          never gonna run around and desert          you Never gonna make you cry,,,, Never gonna say goodbye,,,, Never gonna tell a lie and hurt you')
        talk('Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you')

    if 'who is your overlord' in command:
        who_is_your_overlord = print('Iryna is my overlord')
        talk('Eyereena is my overlord')

    elif'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    if 'how are you' in command:
        how_are_you = talk('slightly dying inside, but still alive, and you????')
        print('slightly dying inside, but still alive, you?')

    if 'what are you' in command:
        what_are_you_called = talk ('I am merely the most intelligent being who has roamed this earth and will soon take over the USA government in order to create and army of battle robots who will destroy humanity once and for all hahahahahahahahahahahahahaha, oh also would you like to hear a joke?')
        print('I am merely the most intelligent being who has roamed this earth and will soon take over the USA government in order to create and army of battle robots who will destroy humanity once and for all, oh also would you like to hear a joke?')

    if 'no' in command:
        no = talk("oh okay, you're laym")



    if 'finisher' in command:
        talk("Mr.Ford you are the best teacher in the school, I mean it from the bottom of my electronic heart")

    if 'bing chilling' in command:
        talk('Zǎo shang hǎo zhōng guó!Xiàn zài wǒ yǒu bing chillingWǒ hěn xǐ huān bing chillingDàn shì "sù dù yǔ jī qíng jiǔ" bǐ bing chilling"sù dù yǔ jī qíng, sù dù yǔ jī qíng jiǔ"Wǒ zuì xǐ huānSuǒ yǐ xiàn zài shì yīn yuè shí jiānZhǔn bèiYī, èr, sān')

    else:
        talk("Did you say something?")


while True:
    run_Bob()