import joblib
import pandas as pd
import streamlit as st


def predict_price(area_m2, rooms, photos, locality):
   # Wczytanie modelu tylko raz (np. Random Forest z Adresowo)
   model = joblib.load("model_random_forest_adresowo_lodz.pkl")
   X_new = pd.DataFrame([[area_m2, rooms, photos, locality]],
                        columns=["area_m2", "rooms", "photos", "locality"])
   return model.predict(X_new)[0]

def main():
   st.title("Predykcja ceny mieszkania (Adresowo)")
   st.write("Podaj dane mieszkania, aby uzyskać szacowaną cenę:")

   # Komponenty UI
   area = st.number_input("Powierzchnia (m²)", min_value=10.0, max_value=300.0, value=50.0)
   rooms = st.slider("Liczba pokoi", 1, 6, 3)
   photos = st.number_input("Liczba zdjęć", 0, 50, 10)
  
  
   locality = st.selectbox("Dzielnica", [
       "Łódź Bałuty", "Łódź Górna", "Łódź Śródmieście",
       "Łódź Widzew", "Łódź Polesie"
   ])

   if st.button("Oblicz cenę"):
      price = predict_price(area, rooms, photos, locality)
      st.success(f"Szacowana cena: {price:,.0f} zł")
  
# === Punkt wejścia ===
if __name__ == "__main__":
   main()