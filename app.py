import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from geopy.geocoders import Nominatim
from data_processor import get_historical_data, calculate_risk, generate_downloadable_output

# --- Kid-friendly messages based on threshold ---
def interpret_risk(risk_percentage, condition_name):
    if risk_percentage > 70:
        return f"⚠️ Very {condition_name}! Stay careful!"
    elif risk_percentage > 30:
        return f"⚠️ Some risk of {condition_name}, be prepared!"
    else:
        return f"✅ Safe! Little chance of {condition_name}."

# --- Histogram for kids ---
def create_risk_histogram(df, variable_name, threshold_value, units):
    df['Exceeds'] = df[variable_name] > threshold_value
    colors = df['Exceeds'].map({True: 'red', False: 'green'})
    fig = px.histogram(
        df, x=variable_name, nbins=15, color=df['Exceeds'],
        color_discrete_map={True:'red', False:'green'},
        title=f"Historical {variable_name} Distribution"
    )
    fig.add_vline(x=threshold_value, line_dash="dash", line_color="orange", 
                  annotation_text="Threshold", annotation_position="top right")
    return fig

# --- MAIN APP ---
def main():
    st.set_page_config(layout="wide")
    st.title("🌤️ Outdoor Fun Weather Predictor")
    st.markdown(
        "Check if your outdoor event will be **very hot, cold, wet, windy, or uncomfortable**! "
        "Simple colors and messages make it easy for everyone to understand."
    )

    # --- Sidebar ---
    st.sidebar.header("1. Event Details")
    default_city = "Bangalore"
    city_name = st.sidebar.text_input("City Name:", default_city)
    
    geolocator = Nominatim(user_agent="weather_event_app")
    try:
        location = geolocator.geocode(city_name)
        lat, lon = location.latitude, location.longitude
    except:
        lat, lon = 12.9716, 77.5946

    st.sidebar.markdown(f"Coordinates: {lat:.2f}, {lon:.2f}")

    st.sidebar.subheader("📅 Event Date")
    selected_date = st.sidebar.date_input("Pick a date:", datetime.today())

    st.sidebar.subheader("🌡️ Weather Condition")
    conditions = {
        "Very Hot": {"variable":"Max Temperature", "units":"K", "default":308.15},
        "Very Cold": {"variable":"Max Temperature", "units":"K", "default":283.15},
        "Very Wet": {"variable":"Total Precipitation", "units":"mm/day", "default":20.0},
        "Very Windy": {"variable":"Max Wind Speed", "units":"m/s", "default":15.0},
        "Very Uncomfortable": {"variable":"Discomfort Index", "units":"°C", "default":30.0},
    }
    condition_name = st.sidebar.selectbox("Select Condition:", list(conditions.keys()))
    variable_name = conditions[condition_name]["variable"]
    threshold_value = st.sidebar.number_input("Threshold (can adjust):", 
                                              value=conditions[condition_name]["default"])

    # --- Main ---
    try:
        data_df = get_historical_data(lat, lon, selected_date, variable_name, conditions[condition_name]["units"])
        risk_stats, data_for_viz = calculate_risk(data_df, variable_name, threshold_value)

        st.header("2. Weather Risk for Your Event")
        message = interpret_risk(risk_stats['risk_percentage'], condition_name)
        color = "red" if "⚠️ Very" in message else ("orange" if "⚠️ Some" in message else "green")
        st.markdown(f"<h2 style='color:{color}'>{message}</h2>", unsafe_allow_html=True)
        st.write(f"Chance of exceeding threshold: {risk_stats['risk_percentage']}%")
        st.write(f"Average historical value: {risk_stats['historical_mean']:.1f}")
        st.write(f"Highest historical value: {risk_stats['historical_max']:.1f}")

        st.subheader("3. Historical Data Distribution")
        st.plotly_chart(create_risk_histogram(data_for_viz, variable_name, threshold_value, conditions[condition_name]["units"]), use_container_width=True)

        st.subheader("4. Download Data")
        json_output, csv_output = generate_downloadable_output(risk_stats, data_for_viz, lat, lon, threshold_value, variable_name)
        st.download_button("💾 Download JSON", data=str(json_output), file_name="event_weather.json", mime="application/json")
        st.download_button("📄 Download CSV", data=csv_output, file_name="event_weather.csv", mime="text/csv")

    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()

