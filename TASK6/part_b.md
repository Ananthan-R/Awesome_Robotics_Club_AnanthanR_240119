# Part B
## What will happen if one side of the robot fails?
If one side of the robot fails and the robot does not detect the change in motion, it will rotate in place if it is on flat ground, or fall down if it is on stairs.
## Effect of such failure on motion of robot:
- Such a failure will cause the robot to lose balance, and it may tip over or fall from the stairs.
- The climbing path will be greatly affected, as the bot will not be able to properly manuever through the stairs.
- The fault can be detected using the IMU sensor, as the sudden change in the motion can be detected by the sensor, and the robot can stop moving, thereby reducing risk of falls and damage to the robot.
- The robot should stop as soon as the IMU sensor detects the change in inertia of the object.

This shows that the use of sensors for feedback can help prevent damage to the robot and help to continue the motion ofthe robot. 