import requests
from datetime import datetime

# Get weather
weather = requests.get("https://wttr.in/?format=3").text

# Get quote
quote = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

# Create summary
today = datetime.now().strftime("%d-%m-%Y")

summary = f"Date: {today}\n\nWeather: {weather}\n\nQuote: {quote}"

# Save to file
with open("daily_summary.txt", "w") as file:
    file.write(summary)

print("Summary created successfully!")
