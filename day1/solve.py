def calculate_fuel(mass):
	return int(mass / 3) - 2

fuel = 0
fuel_sum = 0

with open('input.txt') as f:
    mass_per_module = f.readlines()
    for mass in mass_per_module:
        fuel = calculate_fuel(int(mass))
        print("Current fuel sum: ", fuel_sum)

        while(fuel > 0):
            fuel_sum += fuel
            fuel = calculate_fuel(int(fuel))
            print("Current fuel: ", fuel)

f.closed

print("Fuel calcs finished: ", fuel_sum)
