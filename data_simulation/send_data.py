import requests
import random
import time

# API_KEY = "YOUR_WRITE_API_KEY"

while True:
    temperature = random.randint(25, 40)
    gas = random.randint(100, 800)

    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperature}&field2={gas}"

    response = requests.get(url)

    print(f"Sent -> Temp: {temperature}, Gas: {gas}")

    time.sleep(15)  # MUST keep 15 sec