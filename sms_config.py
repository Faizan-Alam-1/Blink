from twilio.rest import Client
import speak

def sms(text) :
    client = Client("ACc7d414df5a2772ddffae6e54f79f6756" , "b440d2279745329a26aaf3b42d0122d2")
    client.messages.create(to = ["+918210410103"],
       from_ = "+13512072081",
       body = text)
    print("done!")
    speak.speak("Sent SMS Successfully Sir !")