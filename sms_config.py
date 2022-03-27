from twilio.rest import Client
import speak

def sms(text) :
    client = Client("ACc7d414df5a2772ddffae6e54f79f6756" , "57da55e22e5fa854d28076cea8024872")
    client.messages.create(to = ["+918210410103"],
       from_ = "+13512072081",
       body = text)
    print("done!")
    speak.speak("Sent SMS Successfully Sir !")