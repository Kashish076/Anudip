time = int (input ("Enter the time in seconds:"))
if(time>=0 and time<60):
    print(time,"seconds")

elif(time>60 and time <3600):
    minute = time//60
    time = time % 60 
    print (minute,"minutes ",time, "seconds ")
    
elif(time>3600):
    hour = time//3600
    time = time % 3600 
    minute = time//60
    time = time % 60
    print(hour ,"hours ", minute , "minutes " , time,"seconds")

else:
    print("invalid time has entered")