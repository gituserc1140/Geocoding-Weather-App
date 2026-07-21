import os

import requests
import streamlit as st

APP_TITLE = "Geocoding Weather App"
GITHUB_URL = "https://github.com/gituserc1140/Geocoding-Weather-App"
SPONSOR_URL = "https://github.com/sponsors/gituserc1140"
OPENWEATHER_GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"


def get_default_api_key():
    if "openweathermap_api_key" in st.secrets:
        return st.secrets["openweathermap_api_key"]
    return os.getenv("OPENWEATHERMAP_API_KEY", "")


def fetch_geocoding_data(query, api_key):
    response = requests.get(
        OPENWEATHER_GEOCODING_URL,
        params={"q": query, "limit": 5, "appid": api_key},
        timeout=15,
    )
    if response.status_code == 401:
        return {"error": "The API key is invalid. Please check it and try again."}
    if response.status_code != 200:
        return {"error": f"Unable to fetch data right now (status code {response.status_code})."}

    data = response.json()
    if not data:
        return {"error": "No matching locations were found. Try a broader search."}
    return {"data": data}


def render_location_results(results):
    st.subheader("Results")
    for item in results:
        state = item.get("state")
        country = item.get("country", "Unknown country")
        location_parts = [item["name"]]
        if state:
            location_parts.append(state)
        location_parts.append(country)
        st.markdown(
            "\n".join(
                [
                    f"**{', '.join(location_parts)}**",
                    f"- Latitude: `{item['lat']}`",
                    f"- Longitude: `{item['lon']}`",
                ]
            )
        )


def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🌍", layout="centered")
    st.title("🌍 Geocoding Weather App")
    st.write(
        "Search for cities, regions, and places with your own OpenWeatherMap API key."
    )

    st.link_button("View on GitHub", GITHUB_URL)
    st.link_button("Sponsor on GitHub", SPONSOR_URL)

    st.sidebar.header("Settings")
    api_key_input = st.sidebar.text_input(
        "OpenWeatherMap API Key",
        value=get_default_api_key(),
        type="password",
        help="Paste your API key here to enable geocoding searches.",
    )
    st.sidebar.link_button("GitHub Repository", GITHUB_URL)
    st.sidebar.link_button("GitHub Sponsors", SPONSOR_URL)

    api_key = api_key_input.strip()
    if not api_key:
        st.info("Enter your OpenWeatherMap API key in the sidebar to start searching.")
        st.stop()

    query = st.text_input("Location Query", placeholder="e.g. Lagos, Tokyo, São Paulo")
    if st.button("Search", type="primary"):
        if not query.strip():
            st.warning("Enter a location before searching.")
            st.stop()

        with st.spinner("Looking up matching locations..."):
            result = fetch_geocoding_data(query.strip(), api_key)

        if "error" in result:
            st.error(result["error"])
        else:
            render_location_results(result["data"])


if __name__ == "__main__":
    main()
