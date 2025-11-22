import joblib
import pandas as pd

model = joblib.load("model_random_forest_adresowo_lodz.pkl")

def predict_price(area_m2: float, rooms: int, locality: str, photos: int) -> float:
    X_new = pd.DataFrame([[area_m2, locality, rooms, photos]],
                         columns=['area_m2', 'locality', 'rooms', 'photos'])
    
    predicted_price = model.predict(X_new)
    return predicted_price[0]

def get_all_offers(locality: str = None, rooms: int = None, min_price: float = None, max_price: float = None) -> list[dict]:
    offers = pd.read_csv("data/adresowo_lodz_cleaned.csv")
    
    # Filtrowanie po lokalizacji
    if locality:
        offers = offers[offers['locality'].str.contains(locality, case=False, na=False)]
    
    # Filtrowanie po liczbie pokoi
    if rooms is not None:
        offers = offers[offers['rooms'] == rooms]
    
    # Filtrowanie po cenie (min)
    if min_price is not None:
        offers = offers[offers['price_total_zl_cleaned'] >= min_price]
    
    # Filtrowanie po cenie (max)
    if max_price is not None:
        offers = offers[offers['price_total_zl_cleaned'] <= max_price]
    
    # Zamiana NaN na None dla zgodności z JSON
    offers = offers.fillna('None')
    
    return offers.to_dict(orient='records')

    
