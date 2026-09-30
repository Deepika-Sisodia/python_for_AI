# data from API
import requests

from datetime import datetime, timedelta

# calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# format dates for API
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.856&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

# ----------------------------------------------------
# data from pandas

import pandas as pd

daily_data = data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

df['date'] = pd.to_datetime(df['date'])

print(df)

#-------------------------------------------

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(df['date'],df['max_temp'],marker='o')
plt.plot(df['date'],df['min_temp'], marker='o')

plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Paris weather - past 7 days')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart.png')
plt.show()