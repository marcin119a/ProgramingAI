from fastapi import FastAPI, Depends
import uvicorn
from utils import predict_price, get_all_offers
from models import PricePrediction, OfferFilters
import asyncio

app = FastAPI(title="Housing API")

# Root
@app.get("/")
def root():
   return {"message": "API do mieszkań we Łodzi"}


@app.post("/predict_price")
async def predict(offer: PricePrediction):
   predicted_price = await asyncio.get_event_loop().run_in_executor(
       None, predict_price, offer.area_m2, offer.rooms, offer.locality, offer.photos
   )
   return {"predicted_price": predicted_price}


@app.get("/offers")
async def get_offers(filters: OfferFilters = Depends()):
    offers = await asyncio.get_event_loop().run_in_executor(
        None, get_all_offers, filters.locality, filters.rooms, filters.min_price, filters.max_price
    )
    return {"offers": offers, "count": len(offers)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)