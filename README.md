# Geocoding App with Streamlit

This Streamlit app uses the OpenWeatherMap Geocoding API to fetch geographic names and coordinates based on user input.

## Setup
1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and store it in a `secrets.toml` file in the `.streamlit` directory:
   ```toml
   openweathermap_api_key = "your_api_key_here"
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
Enter a location in the text input and click "Search" to fetch geographic data.