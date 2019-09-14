import RPi.GPIO as GPIO
import time
import threading 

IN2=19
IN1=26
ENA=13

ENB=16
IN3=21
IN4=20


def on_dc_1(t,speed):
   
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(ENA,GPIO.OUT)
         GPIO.setup(IN1,GPIO.OUT)
         GPIO.setup(IN2,GPIO.OUT)
         
         freq=1.5
        
         pwm=GPIO.PWM(ENA,freq)
         pwm.start(0)
         
                
         GPIO.output(ENA,False)
            
         #shang zheng zhuan
         GPIO.output(IN1,False)
         GPIO.output(IN2,True)
         #GPIO.output(ENA,True)
         
         pwm.ChangeDutyCycle(speed)
         time.sleep(1)


         GPIO.output(ENA,False)
         time.sleep(2)
  
         pwm.stop()
         GPIO.cleanup()  


def on_dc_2(t,speed):
        #shang fan zhuan
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(ENA,GPIO.OUT)
     GPIO.setup(IN1,GPIO.OUT)
     GPIO.setup(IN2,GPIO.OUT)

     freq=1.5
        
     pwm=GPIO.PWM(ENA,freq)
     pwm.start(0)
 
     GPIO.output(ENA,False)

     GPIO.output(IN1,True)
     GPIO.output(IN2,False)
     #GPIO.output(ENA,True)
     pwm.ChangeDutyCycle(speed)
     time.sleep(t)


     GPIO.output(ENA,False)
     time.sleep(2)
     pwm.stop()
     GPIO.cleanup()  


def down_dc_2(t,speed):        
        #xia zheng zhuan
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENB,GPIO.OUT)
        GPIO.setup(IN3,GPIO.OUT)
        GPIO.setup(IN4,GPIO.OUT)

        freq=1.5
        
        pwm=GPIO.PWM(ENB,freq)
        pwm.start(0)
        
        GPIO.output(ENB,False)

        GPIO.output(IN3,False)
        GPIO.output(IN4,True)
        #GPIO.output(ENB,True)
        pwm.ChangeDutyCycle(speed)        
        time.sleep(1)


        GPIO.output(ENB,False)
        time.sleep(2)
        pwm.stop()
        GPIO.cleanup()  

def down_dc_1(t,speed):
        #xia fan zhuan
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENB,GPIO.OUT)
        GPIO.setup(IN3,GPIO.OUT)
        GPIO.setup(IN4,GPIO.OUT)

        freq=1.5
        
        pwm=GPIO.PWM(ENB,freq)
        pwm.start(0)        

        GPIO.output(ENB,False)
        
        GPIO.output(IN3,True)
        GPIO.output(IN4,False)
        #GPIO.output(ENB,True)
        pwm.ChangeDutyCycle(speed)        
        time.sleep(t)


        GPIO.output(ENB,False)
        time.sleep(2)
        pwm.stop()
        GPIO.cleanup()      
def clas(cla):
       a=1
       b=10
       c=20
       
       def cla_3_on():
          a=1
          b=10
          on_dc_1(a,b)
          on_dc_1(a,b)
          
            
       def cla_3_down():
          a=1
          c=20
          down_dc_1(a,c)
          down_dc_1(a,c)
       
       if cla==1:
          
          down_dc_1(a,c)
          time.sleep(2)
          down_dc_2(a,c)
       elif cla==2:
          
        
          threading.Thread(target=down_dc_1,args=(a,c,)).start()
          on_dc_1(a,b) 
          down_dc_2(a,c)
          
 
          on_dc_2(a,b)
       
       elif cla==3:
          threading.Thread(target=cla_3_on).start()
          cla_3_down()
          time.sleep(2) 
          cla_3_on()
          cla_3_down()
          
 
          
          
       else: 
          threading.Thread(target=down_dc_2,args=(a,c,)).start()
          on_dc_2(a,b) 
          down_dc_1(a,c)
          on_dc_1(a,b)
#clas(1)
#clas(2)
##clas(3)
#clas(4)

