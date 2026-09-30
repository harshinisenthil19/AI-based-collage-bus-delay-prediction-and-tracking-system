import csv


def predict_delay(distance, traffic, weather, previous_delay):

    delay = 0

    if distance > 10:
        delay += 5

    if traffic == "High":
        delay += 10
    elif traffic == "Medium":
        delay += 5

    if weather == "Rainy":
        delay += 10
    elif weather == "Cloudy":
        delay += 3

    delay += previous_delay

    return delay


print("College Bus Delay Prediction")
print("-----------------------------")

distance = float(input("Enter distance (km): "))
traffic = input("Enter traffic (Low/Medium/High): ")
weather = input("Enter weather (Clear/Cloudy/Rainy): ")
previous_delay = int(input("Enter previous delay (minutes): "))

result = predict_delay(
    distance,
    traffic,
    weather,
    previous_delay
)

print("Predicted Bus Delay:", result, "minutes")
