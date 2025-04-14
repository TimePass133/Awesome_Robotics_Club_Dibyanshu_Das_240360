To complete this task, I followed the resources provided, formed the transformation matrices for each joint and on multiplying, got the expressions for x,y,z as:

x=math.cos(theta1)*(l3*math.cos(theta2+theta3)+l2*math.cos(theta2)+l1)
y=math.sin(theta1)*(l3*math.cos(theta2+theta3)+l2*math.cos(theta2)+l1)
z=(l3*math.sin(thetaa2+theta3))+(l2*math.sin(theta2))

On solving these, we get the joint angles as:

theta1=math.atan2(y,x)
theta2=math.asin(((l2+l3*math.cos(theta3))*z+(l3*math.sin(theta3))*(math.sqrt(x**2+y**2)-l1))/((l2+l3*math.cos(theta3))**2+(l3*math.sin(theta3))**2))
theta3=math.acos(((math.sqrt(x**2+y**2)-5)**2+z**2-l2**2-l3**2)/(2*l2*l3))


I have attached the exact way of how I solved these as a pdf.

Thank You.