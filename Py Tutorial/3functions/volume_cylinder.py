def volume_cylinder(radius:float, height:float):
    print(radius)
    print(height)
    volume = 3.14* radius**2 * height
    return volume
r=5.6
h = 6.8
volume_obj = volume_cylinder(height=h,radius=r)

print(volume_obj)

x = lambda a : a*a

add = x(5)
print(add)