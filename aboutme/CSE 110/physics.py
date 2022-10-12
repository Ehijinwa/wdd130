import math 

mass = float(input("mass"))
gravity = float(input("acceleration due to gravity"))
time = float(input("time"))
constant = float(input("drag constant"))
density = float(input("density of fluid"))
area_of_projectile = float(input("cross sectional area of projectile"))

cup = (1/2) * density * area_of_projectile * constant

v_terminal = math.sqrt((mass*gravity)/cup)

velocity = v_terminal * (1 - math.exp((-math.sqrt(mass * gravity * cup) / mass) * time))

print(f"""the inner value of c is {"{:.3f}".format(cup)}""")
print(f"""the terminal velocity is {"{:.3f}".format(v_terminal)}""")
print(f"""the velocity after {time} seconds is {"{:.3f}".format(velocity)}""")