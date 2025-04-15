import math
def inverse_kinematics(x,y,z):
    l1=5
    l2=10
    l3=15
    d=180/math.pi
    if ((l1-math.sqrt(x**2+y**2))**2+z**2>(l2+l3)**2) or ((l1-math.sqrt(x**2+y**2))**2+z**2<(l2-l3)**2):
            return []
    theta1=math.atan2(y,x)
    theta3=math.acos(((math.sqrt(x**2+y**2)-l1)**2+z**2-l2**2-l3**2)/(2*l2*l3))
    theta2=math.asin(((l2+l3*math.cos(theta3))*z-(l3*math.sin(theta3))*(math.sqrt(x**2+y**2)-l1))/((l2+l3*math.cos(theta3))**2+(l3*math.sin(theta3))**2))
    if (l3*math.sin(theta2+theta3)+l2*math.sin(theta2)!=z):
            theta3=theta3*-1
            theta2=math.asin(((l2+l3*math.cos(theta3))*z-(l3*math.sin(theta3))*(math.sqrt(x**2+y**2)-l1))/((l2+l3*math.cos(theta3))**2+(l3*math.sin(theta3))**2))
    return [round(theta1*d,2),round(theta2*d,2),round(theta3*d,2)]
def test_inverse_kinematics():
    l=inverse_kinematics(5,10,14)
    if (l!=[]):
        print("1) x=5, y=10, z=14:\n   Aplha =",l[0],"Beta =",l[1],"Gamma =",l[2],"\n   The given point is reachable.")
    else:
        print("1) x=5, y=10, z=14:\n   The given point is not reachable.")
    l=inverse_kinematics(0.1,0.2,0.3)
    if (l!=[]):
        print("2) x=0.1, y=0.2, z=0.3:\n   Aplha =",l[0],"Beta =",l[1],"Gamma =",l[2],"\n   The given point is reachable.")
    else:
        print("2) x=0.1, y=0.2, z=0.3:\n   The given point is not reachable.")
    l=inverse_kinematics(29.73,0,0)
    if (l!=[]):
        print("3) x=29.73, y=0, z=0:\n   Aplha =",l[0],"Beta =",l[1],"Gamma =",l[2],"\n   The given point is reachable.")
    else:
        print("3) x=29.73, y=0, z=0:\n   The given point is not reachable.")
    l=inverse_kinematics(25,15,10)
    if (l!=[]):
        print("4) x=25, y=15, z=10:\n   Aplha =",l[0],"Beta =",l[1],"Gamma =",l[2],"\n   The given point is reachable.")
    else:
        print("4) x=25, y=15, z=10:\n   The given point is not reachable.")
    l=inverse_kinematics(5,5,-50)
    if (l!=[]):
        print("5) x=5, y=5, z=-50:\n   Aplha =",l[0],"Beta =",l[1],"Gamma =",l[2],"\n   The given point is reachable.")
    else:
        print("5) x=5, y=5, z=-50:\n   The given point is not reachable.")
print("INVERSE KINEMATICS:\n1)inverse_kinematics()\n2)test_inverse_kinematics()")
ch=int(input("Enter Choice: "))
if (ch==1):
    x,y,z=[float(x) for x in input("Enter Co-ordinates(x y z): ").split()]
    lst=inverse_kinematics(x,y,z)
    if lst!=[]:
        for x in lst:
            print(x,end=' ')
    else:
        print("The Given Point is not Reachable.")
elif (ch==2):
    test_inverse_kinematics()