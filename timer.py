import time

def counttimer(seconds):
    
    while seconds > 0:
         hour = int(seconds/60)
         minutes = int(seconds%60)
         timer = f"{hour} :{minutes}"
         print(timer)
         minutes -= 1
        
         

    print("Time Up!")

myseconds = int(input("Enter the time in seconds: "))

counttimer(myseconds)