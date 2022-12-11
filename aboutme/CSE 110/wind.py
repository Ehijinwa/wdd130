def calculate():
    wind_chill = 2 + 3*temperature
    return wind_chill
temperature = float(input("What is the temperature?"))
degree = input("Fahrenheit or Celsius (F/C)?")

for speed in range(5, 61, 5):
    wind_chill = calculate()
    print (wind_chill)
    print(f"At temperature {temperature}, and at wind speed {speed}")
