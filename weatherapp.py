import tkinter as tK 
# for the UI
import requests
#to fetch data from the API, json file
import time
#to make some changes in the default returning value


def getWeather(canvas):
    city = textField.get()
    #getting the city name from the text field
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a173ec7e67075ea1d2135daddacf31f0"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tK.Tk()
canvas.geometry("500x500")
canvas.title("Laksh's get_Weather App")
f = ("Lato", 15, "italic")
t = ("Lato", 35, "italic")

textField = tK.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
#padding in the y coordinate
textField.focus()
#so when the user opens the app it can directly get redirected to the text field
textField.bind('<Return>', getWeather)

label1 = tK.Label(canvas, font=t)
label1.pack()
label2 = tK.Label(canvas, font=f)
label2.pack()
canvas.mainloop()