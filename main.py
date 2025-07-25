from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn
load_dotenv()

app = FastAPI()

CITY = 'new york'
API_KEY = '5e46f00b3653debe858eb1e4996154ba'

def get_weather():
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response= requests.get(weather_url)
        data = response.json()
        
        weather = {
            'city':data['name'],
            'temperature':data['main']['temp'],
            'description':data['weather'][0]['description']
        } 
    except Exception as e:
        print('e:',e)
        weather = {
            'city':'N/A',
            'temperature':'N/A',
            'description':'N/A'
            
        } 
    return weather

@app.get("/info")
async def get_info():
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H-%M-%S")
    
    weather = get_weather()
    return{
        "date":formatted_date,
        "time":formatted_time,
        "weather":weather
    }