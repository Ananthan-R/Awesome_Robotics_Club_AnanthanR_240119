from math import acos, atan2, pi, sqrt 

#function to output joint angles when end effector position is given
#coxa angle is alpha, femur angle is beta and tibia angle is gamma
def inverse_kinematics(x, y, z):
    #lengths of arms
    L1=5
    L2=10
    L3=15

    #checking if the point is inaccessible
    if(sqrt(x**2 + y**2 + z**2)>L1+L2+L3):
        return -1
    
    #coxa angle
    alpha = atan2(y,x)

    #length in x-y plane
    r= sqrt(x**2+y**2)

    #distance made by femur and tibia in x-y plane
    r1= r-L1

    #hypotenuse of triangle made in vertical plane(r2)
    r2 = sqrt(r1**2+ z**2)

    #beta can be found by using rule of cosines in triangle
    # L3^2 = r2^2 +L2^2 +2 x L2 x r2 x cos(beta)
    beta = acos((r2**2 + L2**2 - L3**2)/(2 * L2 *r2))
    
    #finding angle E6 by using cosine rule
    E6 = acos((r2**2 + L3**2 - L2**2)/(2 * L3 *r2))
    if(E6<0):
        E6*=-1

    #finding angle E5
    E5 = pi-beta-E6

    #finding gamma
    gamma = pi - E5

    angles=[round(alpha*180/pi,2) ,round(beta*180/pi,2) ,round(gamma*180/pi,2)]
    
    return angles

def test_inverse_kinematics():
    test= [[6,5,5],
           [1,2,6],
           [16,16,9],
           [30,30,30],
           [8,5,20]]
    for i in range(5):
        print("Test "+str(i+1))
        print("(" + str(test[i][0]) + ", " + str(test[i][1]) + ", "+ str(test[i][2])+ " )")
        arr = inverse_kinematics(test[i][0],test[i][1],test[i][2])
        if(arr==-1):
            print("Point is inaccessible\n")
        else:
            print(str(arr[0]) + ", " + str(arr[1]) +", "+ str(arr [2]) )
            print("Point is accessible\n")
    return

test_inverse_kinematics()
