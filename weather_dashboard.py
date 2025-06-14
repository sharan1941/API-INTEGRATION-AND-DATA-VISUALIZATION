import requests
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your actual API key
API_KEY = "833dcd717ed2558d1f3eab4437e223bf" 
CITY = "Hyderabad"

st.title("🌤 5-Day Weather Forecast Dashboard")
st.write(f"City: *{CITY}*")

# API URL
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code != 200:
    st.error(f"Failed to retrieve data: {data.get('message', 'Unknown error')}")
    st.stop()

# Extract data
dates = []
temperatures = []
humidity = []

for item in data['list']:
    dt = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
    dates.append(dt)
    temperatures.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])

# Create subplots (2 rows, 1 column)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Temperature chart
ax1.plot(dates, temperatures, color='orange', label='Temperature (°C)')
ax1.set_title(f"5-Day Temperature Forecast for {CITY}")
ax1.set_xlabel("Date & Time")
ax1.set_ylabel("Temperature (°C)")
ax1.grid(True)
ax1.legend()

# Humidity chart
ax2.plot(dates, humidity, color='blue', label='Humidity (%)')
ax2.set_title(f"5-Day Humidity Forecast for {CITY}")
ax2.set_xlabel("Date & Time")
ax2.set_ylabel("Humidity (%)")
ax2.grid(True)
ax2.legend()

plt.tight_layout()

# ✅ Use st.pyplot(fig) to avoid warning
st.pyplot(fig)