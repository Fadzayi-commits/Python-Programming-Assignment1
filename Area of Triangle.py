def triangleArea(x,y,z):
    p = (x + y+ z)/2
    return ((p*(p-x)*(p-y)*(p-y)) ** 0.5)


x = float(input('Enter first side of triangle:'))
y = float(input('Enter second side of triangle:'))
z = float(input('Enter third side of triangle:'))

print('Area of triangle is: {}'.format(triangleArea(x,y,z)))