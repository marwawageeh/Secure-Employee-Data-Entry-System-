from tkinter import *
from tkinter import messagebox
#voice recongnition
import pyttsx3
#computer can listen to speacking
import speech_recognition as sr
#to deal with audio
import simpleaudio as sa
#to deal with qrcode
import qrcode
#للتحكم فى الشاشه
import pyautogui

#============set up gui===============
root = Tk()
root.title('Employ Registration Program')
root.geometry('450x520+500+100')
#root.resizable(False,False)


def welcome():
#play this to welcome
   filename = "C:/Users/MaKaNaK/Desktop/my app 3/welcome.wav"
   wave_obj = sa.WaveObject.from_wave_file(filename)
   play_obj = wave_obj.play()
   play_obj.wait_done() 

#voice recongnition
wel= pyttsx3.init()
voices= wel.getProperty('voices')
wel.setProperty('voice',voices[0].id)

#waiting for him to speake
def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

#=============function to take command that you need============
def Takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command sir ..........')
        #دقه الاستماع الى الصوت كل ما ازود فى الرقم لى بعد العامه كان ادق
        command.phrase_threshold = 0.1
        #استمع للصوت الى انا مدخله من المايك
        audio=command.listen(mic)
        try:
            print('Recording ....')# اكتبها عشان اعرف انك بتسجل
            query= command.recognize_google(audio,language='ar')
            print(f'you said : {query}')
        except Exception as Error:
            print(Error)
        return query.lower()
    
#==========functions for excution button==================    
def b1():
    query=Takecommand()
    name=query
    E1.insert(0,name)

def b2():
    query=Takecommand()
    name=query
    E2.insert(0,name)

def b3():
    query=Takecommand()
    name=query
    E3.insert(0,name)

def b4():
    query=Takecommand()
    name=query
    E4.insert(0,name)

def sv():
    namefile=en_save.get()
    name=E1.get()
    co=E2.get()
    jo=E3.get()
    age=E4.get()
    info=qrcode.make(name+co+jo+age)#C:/Users\MaKaNaK\Desktop\my app 3\mn.jpg
    info.save('C:/Users/MaKaNaK/Desktop/my app 3/'+namefile+'.jpg')#C:\Users\MaKaNaK\Desktop\my app 3\marwa.jpg
    messagebox.showinfo('save ','Save ['+ namefile +'] employee')

#===========adding logo for program===============
logo=PhotoImage(file='Screenshot 2023-11-30 211147.png')
lbl_logo= Label(root,image=logo)
lbl_logo.place(x=2,y=1,width=500,height=200)

#==================lables============================
l1=Label(root,text='Emp Name:',font=('Tajawal',14))
l1.place(x=10,y=233)

l2=Label(root,text='Country :',font=('Tajawal',14))
l2.place(x=10,y=273)

l3=Label(root,text='Emp Job :',font=('Tajawal',14))
l3.place(x=10,y=313)

l4=Label(root,text='Age :',font=('Tajawal',14))
l4.place(x=10,y=353)

#====================Entries====================

E1=Entry(root,width=20,font=('Calibri',14))
E1.place(x=140,y=230)

E2=Entry(root,width=20,font=('Calibri',14))
E2.place(x=140,y=270)

E3=Entry(root,width=20,font=('Calibri',14))
E3.place(x=140,y=310)

E4=Entry(root,width=20,font=('Calibri',14))
E4.place(x=140,y=355)

#===============buttoms========================================

b1= Button(root, text = '🔊 ',fg='white',bg='black',font=('Tajawal',14),command=b1)
b1.place(x=400,y=230)

b2= Button(root, text = '🔊 ',fg='white',bg='black',font=('Tajawal',14),command=b2)
b2.place(x=400,y=270)

b3= Button(root, text = '🔊 ',fg='white',bg='black',font=('Tajawal',14),command=b3)
b3.place(x=400,y=310)

b4= Button(root, text = '🔊 ',fg='white',bg='black',font=('Tajawal',14),command=b4)
b4.place(x=400,y=350)

#========================save===================================

l_save=Label(root, text='File Save :',font=('Tajawal',14))
l_save.place(x=10,y=422)

en_save= Entry(root,width=20,font=('Calibri',11))
en_save.place(x=140,y=429)

b_save=Button(root,text='Save ✅', fg='white', bg='red',font=('Tajawal',11),command=sv)
b_save.place(x=345,y=423)

#excute welcome function to welcome for you
welcome()
# Execute Tkinter
root.mainloop()