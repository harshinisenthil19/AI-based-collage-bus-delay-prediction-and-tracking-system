# AI-Based College Bus Delay Prediction System

def predict_delay(distance, traffic, weather, previous_delay):

    delay = 0

    # Distance factor
    if distance > 10:
        delay += 5

    # Traffic factor
    if traffic == "High":
        delay += 10
    elif traffic == "Medium":
        delay += 5

    # Weather factor
    if weather == "Rainy":
        delay += 10
    elif weather == "Cloudy":
        delay += 3

    # Previous delay factor
    delay += previous_delay

    return delay


# Example prediction
distance = 12
traffic = "High"
weather = "Rainy"
previous_delay = 5

predicted_delay = predict_delay(
    distance,
    traffic,
    weather,
    previous_delay
)

print("Predicted Bus Delay:", predicted_delay, "minutes")
