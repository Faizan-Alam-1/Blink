from tkinter import *
from tkinter.font import Font 
from PIL import Image, ImageTk 
import time
import pyautogui 
import pyttsx3  
import speak
import call_config
import joke
import sms_config
import firebase





root =  Tk()
root.configure(background='#C4C4C4') # Changing the Background Color of Root 
width = root.winfo_screenwidth()  
print(width) # 1280
height = root.winfo_screenheight() # Detect the Height 720
print(height)
root.geometry("%dx%d" % (width, height))
root.title("Eye-Blink") 

font_Head_lable_property = Font(
    family = "Comic Sans MS" ,
    size = 18,
    weight = "bold" 
)
 
font_Button_property = Font(
    family = "Comic Sans MS" ,
    size = 10,
    weight = "bold" 
)

font_Instruction_property = Font(
    family = "Comic Sans MS" ,
    size = 10,
    weight = "bold"
    
)

# All Frame 
Main_frame = LabelFrame(root , padx = 100 , pady = 7 , borderwidth=3, relief= "raised") # inside padding 
Main_frame.grid( row = 0 , column = 1 , padx = 20, pady = 60) # outside pading 

Display_frame = LabelFrame(root , padx= 55 , pady = 10 ,borderwidth=3, relief= "raised") # inside padding 
Display_frame.grid( row  = 0, column = 0 , padx = 150 , pady = 10 ,) # outside pading 

Instruction_frame = LabelFrame(root , padx= 30, pady = 4 , borderwidth=3, relief= "raised") # inside padding 
Instruction_frame.grid( row  = 0, column = 2, padx = 80, pady = 1) # outside pading 


# Display_frame Widget

lable_Display = Label(Display_frame , text = "Display Emotion" , font = ("Comic Sans MS" , 14 , "bold" ) , bg = "#C4C4C4" )
lable_Display.grid(row= 0,  column= 0 ,padx = 20 ,  pady = 10)

Display_Image = ImageTk.PhotoImage(Image.open("Image/Background.png"))
Default_Label = Label(Display_frame ,image = Display_Image)
Default_Label.grid(row = 1 , column = 0 , pady = 20)




# Label Funtion to all Button 

def food_label() :
    lable_Display.config(text = "I Wanna Eat Food")

def send_label() :
    lable_Display.config(text = "Message Sending") 

def happy_label() :
    lable_Display.config(text = "I'm Happy Today")

def joke_label() :
    lable_Display.config(text = "listening jokes")

def toilet_label() :
    lable_Display.config(text = "I Wanna Go to Toilet")

def doctor_label() :
    lable_Display.config(text = "Call Doctor")

def light_on_label() :
    lable_Display.config(text = "Light On")    

def light_off_label() :
    lable_Display.config(text = "Light off") 

def Watch_label() :
    lable_Display.config(text = "I Wanna Watch TV")  

def sleep_label() :
    # I Wanna Sleep
    lable_Display.config(text = "I Wanna go to Sleep")  

def Come_Here_label() :
    lable_Display.config(text = "Come Here Please")

def Go_Outside_label() :
    lable_Display.config(text = "I  wanna Go Outside")







# Function of all Button 

def food (event) :
    img_food = ImageTk.PhotoImage(Image.open("Image/food.png"))
    Default_Label.configure(image=img_food)
    Default_Label.image = img_food
    food_label()
    speak.speak("I Wanna Eat Food")
        

def Send(event) :
    img_send = ImageTk.PhotoImage(Image.open("Image/send.jpg"))
    Default_Label.configure(image=img_send)
    Default_Label.image = img_send
    send_label()
    speak.speak("Send SMS")
    sms_config.sms("Please Come, Help me")
   
    
def Happy(event) :
    img_Happy = ImageTk.PhotoImage(Image.open("Image/Happy.png"))
    Default_Label.configure(image=img_Happy)
    Default_Label.image = img_Happy
    happy_label()
    speak.speak("I'm Happy Today")
    

def Joke(event) :
    img_Joke = ImageTk.PhotoImage(Image.open("Image/Joke.png"))
    Default_Label.configure(image=img_Joke)
    Default_Label.image = img_Joke
    joke_label()
    speak.speak("Joke Sir!")
    joke.joke()
    

def Toilet(event) :
    img_toilet = ImageTk.PhotoImage(Image.open("Image/toilet.png"))
    Default_Label.configure(image=img_toilet)
    Default_Label.image = img_toilet
    toilet_label()
    speak.speak("I wanna go to Toilet")

def Doctor(event) :
    img_Doctor = ImageTk.PhotoImage(Image.open("Image/Doctor.png"))
    Default_Label.configure(image=img_Doctor)
    Default_Label.image = img_Doctor
    doctor_label()
    speak.speak("Call Doctor")
    call_config.call()


def Light_On(event) :
    img_Light_On = ImageTk.PhotoImage(Image.open("Image/on.jpg"))
    Default_Label.configure(image=img_Light_On)
    Default_Label.image = img_Light_On
    light_on_label()
    speak.speak("Light on Sir")
    firebase.light_on()

def Light_off(event) :
    img_Light_off = ImageTk.PhotoImage(Image.open("Image/off.png"))
    Default_Label.configure(image=img_Light_off)
    Default_Label.image = img_Light_off
    light_off_label()
    speak.speak("Light off Sir")
    firebase.light_off()

def Watching_TV(event) :
    img_Watch = ImageTk.PhotoImage(Image.open("Image/watch.png"))
    Default_Label.configure(image=img_Watch)
    Default_Label.image = img_Watch
    Watch_label()
    speak.speak("I wanna watch Tv")
    
def Sleep(event) :
    img_sleep = ImageTk.PhotoImage(Image.open("Image/sleep.jpg"))
    Default_Label.configure(image=img_sleep)
    Default_Label.image = img_sleep
    sleep_label()
    speak.speak("I wanna go to sleep")


def Come_Here(event) :
    img_come = ImageTk.PhotoImage(Image.open("Image/come.png"))
    Default_Label.configure(image=img_come)
    Default_Label.image = img_come
    Come_Here_label() 
    speak.speak("Come Here, Please")

def Go_Outside(event) :
    img_outside = ImageTk.PhotoImage(Image.open("Image/outside.jpg"))
    Default_Label.configure(image=img_outside)
    Default_Label.image = img_outside
    Go_Outside_label() 
    speak.speak("I wanna go outside")


# Focus Function 

def on_focus_out_1(event):
    button_1.configure(bg='#C4C4C4') 
    

def on_focus_in_1(event):
    button_1.configure(bg='blue') 


def on_focus_out_2(event):
    button_2.configure(bg='#C4C4C4') 
    

def on_focus_in_2(event):
    button_2.configure(bg='blue') 


def on_focus_out_3(event):
    button_3.configure(bg='#C4C4C4') 
    

def on_focus_in_3(event):
    button_3.configure(bg='blue') 

def on_focus_out_4(event):
    button_4.configure(bg='#C4C4C4') 
    

def on_focus_in_4(event):
    button_4.configure(bg='blue')

def on_focus_out_5(event):
    button_5.configure(bg='#C4C4C4') 
    

def on_focus_in_5(event):
    button_5.configure(bg='blue')        



def on_focus_out_6(event):
    button_6.configure(bg='#C4C4C4') 
    

def on_focus_in_6(event):
    button_6.configure(bg='blue') 


def on_focus_out_7(event):
    button_7.configure(bg='#C4C4C4') 
    

def on_focus_in_7(event):
    button_7.configure(bg='blue') 


def on_focus_out_8(event):
    button_8.configure(bg='#C4C4C4') 
    

def on_focus_in_8(event):
    button_8.configure(bg='blue')     

def on_focus_out_9(event):
    button_9.configure(bg='#C4C4C4') 
    

def on_focus_in_9(event):
    button_9.configure(bg='blue')       

def on_focus_out_10(event):
    button_10.configure(bg='#C4C4C4') 
    

def on_focus_in_10(event):
    button_10.configure(bg='blue')  



def on_focus_out_11(event):
    button_11.configure(bg='#C4C4C4') 
    

def on_focus_in_11(event):
    button_11.configure(bg='blue')    


def on_focus_out_12(event):
    button_12.configure(bg='#C4C4C4') 
    

def on_focus_in_12(event):
    button_12.configure(bg='blue')          

# Main_Frame Widget 

Head_lable = Label(Main_frame , text = "Eye-Blink" , font = font_Head_lable_property , bg = "#C4C4C4" , pady=16 , padx = 40)
Head_lable.grid(row = 0 ,column = 0 )



button_1 = Button(Main_frame , text = "I Wanna Eat Food", font = font_Button_property , bg = "#C4C4C4" , pady=16 , padx = 40 ,  borderwidth= 3, relief=SOLID, command = food )
button_1.bind("<Return>", food)
button_1.grid(row = 1 ,column = 0 , pady = 10)
button_1.bind("<FocusIn>", on_focus_in_1)
button_1.bind("<FocusOut>", on_focus_out_1)


button_2 = Button(Main_frame , text = "Send Meassege", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 55 , borderwidth= 3, relief=SOLID,command = Send)
button_2.bind("<Return>", Send)
button_2.grid(row = 1 ,column = 1 , pady = 10)
button_2.bind("<FocusIn>", on_focus_in_2)
button_2.bind("<FocusOut>", on_focus_out_2)


button_3 = Button(Main_frame , text = "I'm Happy Today", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 45 , borderwidth= 3, relief=SOLID, highlightcolor = "red",command = Happy)
button_3.bind("<Return>", Happy)
button_3.grid(row = 2 ,column = 0 , pady = 10)
button_3.bind("<FocusIn>", on_focus_in_3)
button_3.bind("<FocusOut>", on_focus_out_3)


button_4 = Button(Main_frame , text = "Tell Me a Joke Assistant", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 10, borderwidth= 3, relief=SOLID,command = Joke)
button_4.bind('<Return>', Joke)
button_4.grid(row = 2 ,column = 1 , pady = 10)
button_4.bind("<FocusIn>", on_focus_in_4)
button_4.bind("<FocusOut>", on_focus_out_4)


button_5 = Button(Main_frame , text = "I Wanna Go to Toilet ", font = font_Button_property , bg = "#C4C4C4" , pady=20 , padx = 21 , borderwidth= 3, relief=SOLID , command = Toilet)
button_5.bind("<Return>", Toilet)
button_5.grid(row = 3 ,column = 0 , pady = 10)
button_5.bind("<FocusIn>", on_focus_in_5)
button_5.bind("<FocusOut>", on_focus_out_5)

button_6 = Button(Main_frame , text = "Call Doctor", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Doctor)
button_6.bind("<Return>", Doctor)
button_6.grid(row = 3 ,column = 1 , pady = 10)
button_6.bind("<FocusIn>", on_focus_in_6)
button_6.bind("<FocusOut>", on_focus_out_6)


button_7 = Button(Main_frame , text = "Light On", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Light_On)
button_7.bind("<Return>", Light_On)
button_7.grid(row = 4 ,column = 0 , pady = 10)
button_7.bind("<FocusIn>", on_focus_in_7)
button_7.bind("<FocusOut>", on_focus_out_7)


button_8 = Button(Main_frame , text = "Light Off", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Light_off)
button_8.bind("<Return>", Light_off)
button_8.grid(row = 4 ,column = 1 , pady = 10)
button_8.bind("<FocusIn>", on_focus_in_8)
button_8.bind("<FocusOut>", on_focus_out_8)



button_9 = Button(Main_frame , text = "Watch TV", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Watching_TV)
button_9.bind("<Return>", Watching_TV)
button_9.grid(row = 5 ,column = 0 , pady = 10)
button_9.bind("<FocusIn>", on_focus_in_9)
button_9.bind("<FocusOut>", on_focus_out_9)



button_10 = Button(Main_frame , text = "I Wanna Sleep", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Sleep)
button_10.bind("<Return>", Sleep)
button_10.grid(row = 5 ,column = 1 , pady = 10)
button_10.bind("<FocusIn>", on_focus_in_10)
button_10.bind("<FocusOut>", on_focus_out_10)


button_11 = Button(Main_frame , text = "Come Here", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Come_Here)
button_11.bind("<Return>", Come_Here)
button_11.grid(row = 6 ,column = 0 , pady = 10)
button_11.bind("<FocusIn>", on_focus_in_11)
button_11.bind("<FocusOut>", on_focus_out_11)


button_12 = Button(Main_frame , text = "Go Outside", font = font_Button_property , bg = "#C4C4C4" , pady=18 , padx = 80 ,borderwidth= 3, relief=SOLID , command = Go_Outside)
button_12.bind("<Return>", Go_Outside)
button_12.grid(row = 6 ,column = 1 , pady = 10)
button_12.bind("<FocusIn>", on_focus_in_12)
button_12.bind("<FocusOut>", on_focus_out_12)
 
root.mainloop()



