from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from calculator import calculator
from pydantic import BaseModel
import starlette.status as status
import datetime
import json
import uvicorn
import requests


app = FastAPI()
date = datetime.datetime.today()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

class Fees(BaseModel):
    item_amount: float
    delivery_distance: float
    cart_value: float




@app.get("/item_amount={item_amount}&delivery_distance={delivery_distance}&cart_value={cart_value}")
async def get_fees(item_amount: float, delivery_distance: float, cart_value: float):  
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute

    fees = calculator(delivery_distance, item_amount, cart_value, year, month, day, hour, minute)
    return {"total_fees": fees}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000, reload=True)
