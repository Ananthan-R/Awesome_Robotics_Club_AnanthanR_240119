# Inverse kinematics of hexapod arm using python

![](https://github.com/Ananthan-R/Awesome_Robotics_Club_AnanthanR_240119/blob/main/TASK_5/armFigure.png?raw=true)

## Explanation of code:
The coordinate axes are taken as follows:
- The origin is the first coxa joint.
- The positive X axis is taken at the centre of the range of motion of the coxa joint.
- Positive Y axis is in the plane of rotation of the coxa joint.
- Positive z axis is downwards.

### The function inverse_kinematics:

- In this function, first we have initialised the lengths of the arms of the robots(L1, L2 and L3). Then we have checked to see if the point given in input to the function is inaccessible or not. The point is inaccessible if the distance from the origin( the first coxa joint) to the point is more than the sum of lengths of the arms. If the point is inaccessible the function will return -1.

- Finding the angle alpha( the angle at the coxa) is comparatively easy as it is directly dependent on the x and y coordinates of the point.
tan(alpha) = x/y
-In order to find the angle beta, we first need to find the distances r1 and r2(see figure)
-Then, using cosine rule, we can directly find the angle beta
L3^2 = r2^2 +L2^2 - 2 x L2 x r2 x cos(beta)
=> beta = cos^-1 ((r2^2 + L2^2 - L3^2)/(2 x L2 xr2))
- Then we need to find the angle E6 to find the angle gamma. We use cosine rule again to find E6
L2^2 = r2^2 + L3^2 - 2 x L3 x r2
=>E6 = cos^-1 ((r2^2 + L3^2 -L2^2)/(2 x L3 xr2))
- We find E5, and gamma by using angle sum property of triangle. Then, we convert alpha, beta and gamma into degrees, round them to two decimal places and return them after making a list of the angles.

### The function test_inverse_kinematics()
- First, we have initialised a list which contains the coordinates of the points at which the inverse_kinematics() function has to be tested.
- Then, we use a for loop to traverse through these values, and print the points. If the point is accessible, we also print the values of the three angles. We print a short note which says if the point is accessible or not.

