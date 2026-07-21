# Geocoding App

Interactive Streamlit app for looking up place names and coordinates with the OpenWeatherMap Geocoding API.

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/gituserc1140/Geocoding-Weather-App)
[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)

## About

This app lets an end user provide an OpenWeatherMap API key directly in the Streamlit UI, search for a location, and view matching place names with latitude and longitude details. It is designed as a simple geocoding reference app with a lightweight user experience.

## Features

- Front-end API key entry for OpenWeatherMap
- Clear messaging when the API key is missing or invalid
- Location search with up to 5 matches
- GitHub and GitHub Sponsors buttons in the app UI and this README

## Requirements

- Python 3.9 or newer
- An [OpenWeatherMap API key](https://openweathermap.org/api)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## How to use the app

1. Launch the app with `streamlit run app.py`.
2. Enter your OpenWeatherMap API key in the sidebar.
3. Type a city, town, region, or place name in the location field.
4. Click **Search**.
5. Review the returned matching locations and their coordinates.

## Optional local configuration

If you do not want to paste the API key every time, you can also preconfigure it with either of these options:

- Streamlit secrets in `.streamlit/secrets.toml`
  ```toml
  openweathermap_api_key = "your_api_key_here"
  ```
- Environment variable
  ```bash
  export OPENWEATHERMAP_API_KEY="your_api_key_here"
  ```
