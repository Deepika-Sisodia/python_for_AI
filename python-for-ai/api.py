import requests

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)

data = response.json()

print(data)


def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data['current_weather']['temperature']

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Current temperature in Paris: {paris_temp}°C")
print(f"Current temperature in London: {london_temp}°C")    
print(f"Current temperature in Tokyo: {tokyo_temp}°C")