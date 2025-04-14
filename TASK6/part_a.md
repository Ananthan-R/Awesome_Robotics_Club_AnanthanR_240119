# Design of the Bot
## Block Diagram:
![]()
## Control:
The robot will use a microcontroller (Arduino or Raspberry Pi) to control the components.
The components required are given below:
- Microcontroller (Raspberry Pi or Arduino)
- Servo Motors
- Treads
- Robot Chassis
- Motor Controller
- Breadboard and wires
- LCD Display
- Motion sensors(IMU, Camera)
- Power Module
- Geared DC motors

## Mechanism to be used:
The robot should use Treads because they provide the maximum amout of traction on a small edge when climbing stairs. Wheels will not be able to get enough traction, and legs will cause balancing issues because of the length required to climb up stairs.
## Design:
The robot will consist of two parts, front and back, each having separate treads. The front an back sections will be connected with gears run by a servo motor that allows the robot to bend in the middle and lift the front part up, so that it can reach the top of the stairs. The treads can be run by geared DC motors, so that they have enough power to climb up stairs. IMU sensor can be used to detect if the bot falls or slips. Ultrasound or camera can be used to detect the distance of the bot from the wall. The microcontroller uses the input from the sensors to change the path of te bot.
## Ensuring Stability while climbing stairs
Because the bot has to climb stairs, which can cause loss of balance, the centre of mass of the bot should be as low as possible. So, the Power module should be kept as close to the ground as possible, and all the hother heavy components should also be close to the ground. The robot should have a wide base of support, so that the centre of mass will be close to the ground.
## Sensors to be used:
- IMU: It helps to detect the change in the inertia of the Bot, thereby letting us know if the robot has run into some problems(slipping, falling, etc). 
- Ultrasound: It helps us to measure the distance between the robot and the stairs so that it can move accordungly and climb.
- Camera: Helps the users see the path and control the robot accordingly.

## How will robot detect stairs and change its motion irl:
The robot can use ultrasound sensor to detect the distance from the obstruction in front. The input from the camera can be used to see if the obstruction is stairs or not. Then the robot will use its servo motors to lift the front half of the robot onto the first stair, and use the treads to climb on top.
