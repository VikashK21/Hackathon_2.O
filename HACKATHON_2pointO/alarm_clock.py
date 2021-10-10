from tkinter import *
import pygame
import time
pygame.mixer.init()
root=Tk()
root.title('ALARM CLOCK')
def alarm():
        hour=time.strftime("%H")
        min=time.strftime("%M")
        sec=time.strftime("%S")
        # ampm=time.strftime("%p")
        t=hour+":"+min+":"+sec
        timelable.config(text=t)
        if t==h_m_s.get():
                m=Label(root, text=messate.get())
                m.pack()
                pygame.mixer.load("playlist2.mp3")
                pygame.mixer.music.play(loops=0)
                return 
        else:
                timelable.after(1000, alarm)
def contrl_alarm():
        global timelable
        timelable=Label(root, text=" ", font=("halvetica", 48), fg="white",bg="orange")
        timelable.pack(pady=20)
        alarm()

space=Label(root,text="    ")
space2=Label(root,text="    ")
space3=Label(root, text="     ")

h_m_s=Entry(root, justify=CENTER, borderwidth=5, font=('merriweather', 20), bg='#EA4C46', fg="orange")
messate=Entry(root, border=5, font=('halvetica', 30),bg="green", fg="orange")
labeljustify=Label(root, text="Set the timing in 24 hrs format", font=('halvetica', 15), bg="#406343")
space3.pack()
labeljustify.pack()
h_m_s.pack()
space.pack()
messate.pack()
space2.pack()
h_m_s.insert(0,"00:00:00")
messate.insert(0, "Any Message")
# labeljustify.grid(row=0, column=0)
# h_m_s.grid(row=1, column=1)
time_button=Button(root, text="Set", font=("bold", 25), width=20,fg="red", command=contrl_alarm)      
time_button.pack()

root.mainloop()











###############################################################

# x=datetime.datetime.now()
# print('microsec',x.strftime("%f"))
# print('min',x.strftime("%M"))
# print('sec',x.strftime("%S"))
# print('hour as 24',x.strftime("%H"))
# print('hour',x.strftime("%I"))


# from pydub import AudioSegment
# from pydub.playback import play
# import random
  
############################################
#################***********tkinter*************

# from tkinter import *

# root = Tk()
# root.title('Alarm')
# # mylable=Label(root, text='hello I am Vikash.\nhey ther is something wrong.')
# # mylable2=Label(root, text='we are in a team work.')
# # mylable.grid(row=6, column=6)
# # mylable2.grid(row=3, column=4)

# root.grid_rowconfigure(3)
# iput = Entry(root, justify=CENTER)
# iput.pack()
# iput.insert(3, '4567')
# def myclick():
#     available='welcome '+iput.get()
#     mylable=Label(root, text=available)
#     mylable.pack()
# mybutton=Button(root, text='Set', command=myclick)
# # iput.grid(row=1,column=0)
# # mybutton.grid(row=1, column=1)
# mybutton.pack()
# root.mainloop()









# from playsound import playsound

