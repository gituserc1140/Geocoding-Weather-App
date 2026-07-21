import streamlit as st
import requests

def fetch_geocoding_data(query):
    api_key = st.secrets["openweathermap_api_key"]
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

def main():
    st.title("Geocoding App")
    st.write("Enter a location to fetch geographic names and coordinates.")

    query = st.text_input("Location Query")
    if st.button("Search") and query:
        data = fetch_geocoding_data(query)
        if data:
            for item in data:
                st.write(f"Name: {item['name']}, Latitude: {item['lat']}, Longitude: {item['lon']}")

if __name__ == "__main__":
    main()