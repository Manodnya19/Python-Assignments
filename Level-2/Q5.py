
temperature_readings = [25, 28, 21, 24, 27]

if not temperature_readings:
    print("No data provided")
else:
    average_temp = sum(temperature_readings) / len(temperature_readings)
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)

    print(f"Average Temperature: {average_temp:.1f}")
    print(f"Highest Temperature: {highest_temp}")
    print(f"Lowest Temperature: {lowest_temp}")