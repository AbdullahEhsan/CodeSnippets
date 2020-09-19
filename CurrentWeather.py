import requests
import datetime

zip=input("Enter Zip:")

api="http://api.openweathermap.org/data/2.5/weather?zip="+str(zip)+",us&appid=d4c75ebb266fa653ef7a5796f8672bfc"

r=requests.get(api, "units=imperial")

data=r.json()

print("Name:",data['name'])
print("Current Temperature:", data['main']['temp'],"degrees Fahrenheit")
print("Atmospheric Pressure:",data['main']['pressure'],"hPa")
print("Wind Speed:",data['wind']['speed'],"mph")
print("Wind Direction:",data['wind']['deg'],
"degrees")
print("Time of Report:",datetime.datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),"UTC")
print("---")
print("Data courtesy of OpenWeatherMap")




