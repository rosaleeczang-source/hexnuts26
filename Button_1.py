#######import statements######
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#defines the variables


hub = PrimeHub()
#print(hub.system.info['name']), this was used to find which robot was which
#defines the ports
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
back_arm = Motor(Port.A)
front_arm = Motor(Port.D)
#Defining the drive base and telling it to not use the gyro
dB = DriveBase(left_motor,right_motor, wheel_diameter=54, axle_track=80)
dB.use_gyro(False)
#resets the heading
hub.imu.reset_heading(0)
dB.settings(200,550,50,150) #maxspeed, stspeed, accel, turn rate  

def calibrate_arm_back_up():
    back_arm.run_until_stalled(700,then=Stop.COAST,duty_limit=35)
    # turn arm back up N degrees
    #back_arm.run_angle(700,360)
    return

def calibrate_arm_back_down():
    back_arm.run_until_stalled(-700,then=Stop.COAST,duty_limit=35)
    # turn arm back down N degrees
    #back_arm.run_angle(700,360)
    return

def calibrate_arm_front_down():
    front_arm.run_until_stalled(-700,then=Stop.COAST,duty_limit=35)
    return

def calibrate_arm_front_up():
    front_arm.run_until_stalled(700,then=Stop.COAST,duty_limit=35)
    return

#Defining the missions
#run1
def run1():
    return

def mission_2():
    # Mission 2, Alex here
    # red home, the protruding left beam lined up 6 blocks from the bottom, 8 blocks from the corner on the x axis
    dB.use_gyro(True)
    dB.turn(46)
    calibrate_arm_front_down()
    front_arm.run_angle(60, 80)   
    dB.straight(380)
    front_arm.run_angle(60, 44)
    dB.straight(-35)
    front_arm.run_angle(60, 44)
    dB.straight(25)
    front_arm.run_angle(60, 74, wait=False)
    dB.straight(-355)
    dB.turn(-46)
    dB.use_gyro(False)
    return

def mission_6():
    #Mission 6, Markos here
    #calibrate_arm_front()
    dB.straight(40)
    dB.straight(-10)
    dB.turn(110)
    dB.straight(152.4)
    dB.settings(50,550,50,150) #maxspeed, stspeed, accel, turn rate 
    dB.turn(17)
    dB.straight(187.2)
    dB.turn(8)
    return
#addilynns good code
def mission_11():
    dB.use_gyro(True)
    dB.straight(-100)
    dB.turn(90)
    dB.straight(8.5*25.4)
    dB.turn(-45)
    dB.straight(5*25.4)   
    dB.turn(60)
    dB.straight(22*25.4)
    dB.use_gyro(False)
    return


#Mission 3, rosa here
#using hexnut
#Red base, grey arm bracket lines up with sixth square, back lines up with corner block
def mission_3():
    calibrate_arm_front_down()
#using long wings on the front arm to hit my mission :)
    front_arm.run_angle(600,307)
    dB.settings(straight_speed=200)
    #raise arm 345
    dB.straight(130)
    #hitting
    front_arm.run_angle(-570,180) #210
    dB.straight(-30)
    front_arm.run_angle(-200,70)
    dB.straight(-90)
    #first flip
    front_arm.run_angle(600,260)
    dB.straight(140)
    front_arm.run_angle(-590,210)
    dB.straight(-80)
    front_arm.run_angle(-200,40)
    dB.straight(-300)
    front_arm.run_angle(600,260)

    # Caleb's Mission
    dB.turn(90)
    dB.straight(533)
    dB.straight(-533)
    return





def run3():#mission15 Eli here
#first black solid line in red cornor
    dB.use_gyro(True)
    calibrate_arm_front_down()
    front_arm.run_angle(speed=1000,rotation_angle=120) #raise arm
    dB.turn(35)#turn
    dB.straight(700)
    dB.turn(55)#turn
    #PushRedsquare
    dB.straight(150)
    #backwards
    dB.straight(-60)
    #raisearm
    front_arm.run_angle(speed=1000,rotation_angle=200) #raise arm
    # going back 80 in line 130 dB.straight(-40)
    # raise once in line 132 front_arm.run_angle(speed=1000,100)#reseting arm
    dB.straight(105)
    dB.turn(90)#turn
    ##farther
    dB.use_gyro(False)
    dB.straight(540) 
    dB.use_gyro(False)
    dB.use_gyro(True)
    dB.straight(-60)
    #not hit green thing
    dB.turn(-147)#turn
    front_arm.run_angle(speed=1000,rotation_angle=-225)#put arm down
    dB.straight(6*25.4)
    front_arm.run_angle(speed=30,rotation_angle=57)#reseting arm
    wait(1000)
    #gently down
    front_arm.run_angle(speed=30,rotation_angle=-57)
    dB.straight(30)
    front_arm.run_angle(speed=1000,rotation_angle=-50)
    #composthatch
    dB.turn(42)
    #raisearm slightly
    front_arm.run_angle(speed=1000,rotation_angle=200,wait=False)
    dB.straight(8.5*25.4) 
    dB.turn(-60)
    dB.straight(15*25.4)
    dB.turn(30) # line up with leaf cutter
    dB.straight(4.25*25.4)
    dB.settings(straight_speed=100)
    dB.straight(5*25.4)
    dB.use_gyro(False)
    dB.use_gyro(True)
    return
   


#run4
def run4():
#mission 13 Harvey
#Taco
#Left side of the bumper lined up with the second to last big black line farthest away from the edge of board.

#back_arm.reset_angle(0)
    dB.use_gyro(True)
    back_arm.run_target(50,30)
    dB.straight(-609)
    dB.turn(45)
    dB.straight(-146)
    back_arm.run_angle(rotation_angle=130,speed=1000)
    dB.straight(80)
    ###Calvins code###(M12(cane ONLY))
    dB.turn(45)
    back_arm.run_until_stalled(700)
    dB.straight(-101.6)
    back_arm.run_angle(rotation_angle=-20,speed=80)
    dB.turn(30)
    dB.turn(-40)
    dB.straight(40)
    back_arm.run_target(500,30)
    dB.turn(-80)
    dB.straight(600)
    dB.use_gyro(False)
    return


###Button Functions###
def pause(message=''):
    # Wait for any button to be pressed, and save the result.
    hub.system.set_stop_button(None)
    hub.system.set_stop_button(Button.BLUETOOTH)
    hub.speaker.beep()
    print(message)
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(10)

    hub.system.set_stop_button(Button.CENTER)
    hub.speaker.beep()
    wait(500)

def select_number(active, options):
    """
    Interactive number selector using the Spike Prime hub buttons.
    - Left / Right buttons scroll through 'options'.
    - Center button confirms selection.
    - Selected number is shown on the hub display.
    - Returns the newly selected number.
    """

    # Disable the default stop behavior for the center button
    #hub.system.set_stop_button(None)
    hub.system.set_stop_button(Button.BLUETOOTH)
    
    index = options.index(active) if active in options else 0
    total = len(options)

    def show():
        hub.display.number(options[index])
        #displays the number of the code that it is running 

    show()
    hub.speaker.beep()

    while True:
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:# makes the left button make the number the code is running lower
            index = (index - 1) % total
            show()
            hub.speaker.beep()
            wait(300)  # debounce

        elif Button.RIGHT in pressed: #makes the right button increase the number the code is running
            index = (index + 1) % total
            show()
            hub.speaker.beep()
            wait(300)  # debounce

        elif Button.CENTER in pressed: #runs the code number, each code number is a different code function
            # confirm selection
            hub.speaker.beep()
            wait(300)
            hub.display.number(options[index])
            # Re-enable stop button before returning
            hub.system.set_stop_button(Button.CENTER)
            return options[index]

        wait(50)


hub.speaker.beep()
active = 1
options = [ 1, 2, 3, 4, 5, 6 ] # different code functions
#run2()
while True:
  wait(100)
  hub.imu.reset_heading(0)
  active = select_number(active, options)
  print (active)
#runs the functions based on the number ran from 
  if active == 1:
      mission_3()
      dB.stop()
  
  elif active == 2:
      mission_2() 
      dB.stop()

  elif active == 3:
      # Eli and Markos
      run3() 
      # Addlynn
      mission_11() 
      dB.stop()
      
  elif active == 4:
      # Harvey and Calvin
      run4()
      dB.stop()
  
  elif active == 5:
      run2()
      dB.stop()
  
  elif active == 6:
      sixfive()
      dB.stop()

  
  #test if Nadya can commit to github
  #banana.  Eli
  #Rosa's test push
