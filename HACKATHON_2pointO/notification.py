import time
from plyer import notification
from playsound import playsound

def Playsound(playsound):
    notification.notify(
        title = "NAVGURUKUL MEMBER",
        message=" DOING PROJECT" ,
        timeout=1,
    )
    playsound("/home/suraj/Downloads/Iphone_New-cc0ffd70-4e56-31fa-80c3-fccffc8a2966.mp3")
    time.sleep(5)
b=int(input("Enter number : "))
for i in range(b):
    Playsound(playsound)



############################################################################


# from time import sleep
# import datetime
# from playsound import playsound

# alarmH = int(input("What hour do you want the alarm to ring? "))
# alarmM = int(input("What minute do you want the alarm to ring? "))
# ampm = str(input("am or pm? "))

# print("Waiting for alarm",alarmH,alarmM,ampm)
# if (ampm == "pm"):
#         alarmH = alarmH + 12
# while(1 == 1):
#     if(alarmH == datetime.datetime.now().hour and
#         alarmM == datetime.datetime.now().minute) :
#         playsound("/home/suraj/Downloads/Iphone_New-cc0ffd70-4e56-31fa-80c3-fccffc8a2966.mp3")
#         print("Time to wake up")
#         break
