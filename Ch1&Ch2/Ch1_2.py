W_speed = float(input(' *** Wind classification ***\nEnter wind speed (km/h) : '))
W_class = None
if W_speed < 0 or not isinstance(W_speed, (int, float)): raise ValueError("Invalid wind speed")
if W_speed == 0 or W_speed <= 51.99: W_class = "Breeze"
elif 52.00 <= W_speed <= 55.99: W_class = "Depression"
elif 56.00 <= W_speed <= 101.99: W_class = "Tropical Storm"
elif 102.00 <= W_speed <= 208.99: W_class = "Typhoon"
else: W_class = "Super Typhoon"
print(f'Wind classification is {W_class}.')