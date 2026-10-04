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

#Mission 3, rosa here
#using hexnut
#Red base, grey arm bracket lines up with sixth square, back lines up with corner block
front_arm.run_angle(600,260)
#raise arm
dB.straight(355.6)
#hitting
front_arm.run_angle(-570,210)
dB.straight(-50)
front_arm.run_angle(-60,50)
dB.straight(-70)
#first flip
front_arm.run_angle(600,260)
dB.straight(80.6)
front_arm.run_angle(-570,210)
dB.straight(-60)
front_arm.run_angle(-200,40)
dB.straight(-90)
    #mission 1, caleb here

    #mission 2, alex here 
    dB.turn(-160)
    dB.straight(508)
    dB.turn(120)
    dB.straight(200)
    front_arm.run_angle(300, 60)
    return
def run2():
    #run2
    #mission15 Eli here
    front_arm.run_angle(-80,180)#lower arm

    dB.turn(35)#turn

    dB.straight(500)

    front_arm.run_angle(-80,-180)#reseting arm
    #mission6 Markos here
    calibrate_arm_front()
    dB.turn(110)
    dB.straight(152.4)
    front_arm.run_angle(-700,360)#lower arm

    #mission 11 Addilynn here
    #starts on rightside of Ant
    dB.straight(-25)
    dB.turn(85)
    dB.straight(45)
    dB.turn(-30)
    return

#run3
def run3():
#mission7 Calvin

#mission 13 Harvey

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

while True:
  wait(100)
  hub.imu.reset_heading(0)
  active = select_number(active, options)
  print (active)
#runs the functions based on the number ran from 
  if active == 1:
      print ('calibrate')
      calibrate_arm_left()
      calibrate_arm_right()
  
  elif active == 2:
      m2()
      #m13()  
      dB.stop()

  elif active == 3:
      m_one()  
      dB.stop()
      
  elif active == 4:
      m11()
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