import numpy as np

# basic
x = np.array([3,2])
y = np.array([5,1])
z = x + y
print(z)

print("# angles and things")
# angles and things
x = np.array([1,2,3])
y = np.array([-7,8,9])
np.dot(x,y)
dot = np.dot(x,y)
x_modulus = np.sqrt((x*x).sum())
y_modulus = np.sqrt((y*y).sum())
cos_angle = dot / x_modulus / y_modulus # cosine of angle between x and y
angle = np.arccos(cos_angle)
print(angle)

tempAngle =  angle * 360 / 2 / np.pi # angle in degrees
print(tempAngle)



print("# inbuilt matrix class")
# inbuilt matrix class
x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
print(x * y)

x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
print(x * y)


print("linear angle")
# linear angle
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)


a = np.array([[1., 2.], [3., 4.]])
ainv = np.linalg.inv(a)
print(np.allclose(np.dot(a, ainv), np.eye(2)))

print(np.allclose(np.dot(ainv, a), np.eye(2)))