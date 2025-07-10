from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
import pickle
import pandas as pd
from typing import Literal,List
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
with open('models/ModelTransport.pkl', 'rb') as f:
    ModelTransport = pickle.load(f)

with open('models/ModelHomeEnergy.pkl', 'rb') as f:
    ModelHomeEnergy = pickle.load(f)

with open('models/ModelDigitalUsage.pkl', 'rb') as f:
    ModelDigitalUsage = pickle.load(f)

with open('models/ModelShopping.pkl', 'rb') as f:
    ModelShopping = pickle.load(f)

with open('models/ModelFoodDiet.pkl', 'rb') as f:
    ModelFoodDiet = pickle.load(f)


class Transport(BaseModel):
    transport: Literal["private", "public", "walk/bicycle"]
    vehicle_type: Literal['petrol', 'diesel', 'electric','None']
    vehicle_monthly_distance_km: float
    frequency_of_traveling_by_air: Literal['never', 'rarely', 'frequently', 'very frequently']

class HomeEnergy(BaseModel):
    heating_energy_source: Literal['electricity','natural gas', 'wood', 'coal','None']
    energy_efficiency: Literal['No','Sometimes','Yes']
    how_long_tv_pc_daily_hour: int

class DigitalUsage(BaseModel):
    how_long_internet_daily_hour: int

class Shopping(BaseModel):
    how_many_new_clothes_monthly: int
    waste_bag_size: Literal['small', 'medium', 'large', 'extra large', 'None']
    waste_bag_weekly_count: int
    recycling: List[Literal["Paper", "Plastic", "Glass", "Metal"]] = Field(default_factory=list)

class FoodDiet(BaseModel):
    diet: Literal['vegan', 'vegetarian', 'pescetarian', 'omnivore', 'None']
    monthly_grocery_bill: int
    

@app.get("/")
def read_root():
    return {"message": "Welcome to the CarbonCue API", "status": "healthy"}

@app.get("/health")
def health():
    models_loaded = sum([
        ModelTransport is not None,
        ModelHomeEnergy is not None, 
        ModelDigitalUsage is not None,
        ModelShopping is not None,
        ModelFoodDiet is not None
    ])
    return {"status": "healthy", "models_loaded": models_loaded}

@app.post("/predictTransport")
def predictTransport(data: Transport):
    input_df = pd.DataFrame([{
        "Transport": data.transport,
        "Vehicle Type": data.vehicle_type,
        "Vehicle Monthly Distance Km": data.vehicle_monthly_distance_km,
        "Frequency of Traveling by Air": data.frequency_of_traveling_by_air
    }])

    try:
        prediction = ModelTransport.predict(input_df)
        return {"predicted_carbon_emission": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predictHomeEnergy")
def predictHomeEnergy(data: HomeEnergy):
    input_df = pd.DataFrame([{
        "Heating Energy Source": data.heating_energy_source,
        "Energy efficiency": data.energy_efficiency,
        "How Long TV PC Daily Hour": data.how_long_tv_pc_daily_hour
    }])

    try:
        prediction = ModelHomeEnergy.predict(input_df)
        return {"predicted_carbon_emission": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predictDigitalUsage")
def predictDigitalUsage(data: DigitalUsage):
    input_df = pd.DataFrame([{
        "How Long Internet Daily Hour": data.how_long_internet_daily_hour
    }])

    try:
        prediction = ModelDigitalUsage.predict(input_df)
        return {"predicted_carbon_emission": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predictShopping")
def predictShopping(data: Shopping):
    input_df = pd.DataFrame([{
        "How Many New Clothes Monthly": data.how_many_new_clothes_monthly,
        "Waste Bag Size": data.waste_bag_size,
        "Waste Bag Weekly Count": data.waste_bag_weekly_count,
        "Recycling": data.recycling
    }])

    try:
        prediction = ModelShopping.predict(input_df)
        return {"predicted_carbon_emission": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predictFoodDiet")
def predictFoodDiet(data: FoodDiet):
    input_df = pd.DataFrame([{
        "Diet": data.diet,
        "Monthly Grocery Bill": data.monthly_grocery_bill
    }])

    try:
        prediction = ModelFoodDiet.predict(input_df)
        return {"predicted_carbon_emission": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)