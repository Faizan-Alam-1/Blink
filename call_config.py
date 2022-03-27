from twilio.rest import Client
import speak
def call() :
    client = Client("ACc7d414df5a2772ddffae6e54f79f6756",
                "b440d2279745329a26aaf3b42d0122d2")
    call= client.calls.create(twiml='<Response><Say>Hello</Say></Response>',to = "+918210410103",  from_ = "+13512072081" )
    print("done")  
    speak.speak("Successfully Called to Doctor Sir!")  

