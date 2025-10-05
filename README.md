 Will It Rain On My Parade?

Team: Semi Colons

A professional climate risk dashboard that estimates the likelihood of adverse weather conditions for any outdoor event. Leveraging historical Earth observation data from NASA and partner sources, the app provides actionable insights for planning events based on temperature, precipitation, wind speed, or overall discomfort.

 Features

Location-based analysis: Enter a city or coordinates to fetch historical data for the target location.

Custom date selection: Analyze specific dates to estimate the probability of adverse conditions.

Condition selection: Evaluate “Max Temperature,” “Total Precipitation,” “Max Wind Speed,” or “Discomfort Index.”

Threshold customization: Set thresholds to define what constitutes an adverse condition.

Probability and risk calculation: Quantifies the likelihood that historical data exceeded the chosen threshold.

Visualizations:

Histogram of historical occurrences versus thresholds

Trend analysis with linear regression to detect long-term patterns

Data export: Download results in JSON or CSV formats for further analysis or reporting.

Technical Overview

Frontend: Streamlit for an interactive, web-based interface.

Backend:

Python with Pandas and NumPy for data handling and statistical calculations

Plotly for interactive visualizations

Geopy for geocoding city names into coordinates

Data Sources: Simulated historical climate data; structured to easily integrate with NASA MERRA-2, GPM, and CPTEC datasets.

Risk Calculation: Calculates the proportion of historical data exceeding user-defined thresholds and summarizes mean, max, and probability metrics.

<h2>Installation & Setup</h2> 

Clone the repository:

git clone https://github.com/your-repo/will-it-rain-on-my-parade.git
cd will-it-rain-on-my-parade


Install dependencies:

pip install streamlit pandas numpy plotly geopy


Run the app:

streamlit run app.py


Open the displayed URL (usually http://localhost:8501) to interact with the dashboard.

Usage Workflow

Define Event Location: Enter city name or latitude/longitude coordinates.

Select Event Date: Specify the exact date of the planned event.

Choose Condition: Select a weather variable (e.g., Max Temperature, Total Precipitation).

Set Threshold: Adjust the threshold for what constitutes an adverse condition.

View Results:

Risk score (%) of exceeding the threshold

Summary statistics (mean, maximum)

Histogram and trend visualization

Download Data: Export detailed data for reporting or further analysis.

Example Output

Risk Score: 65% probability that the Max Temperature exceeded 305 K historically.

Histogram: Shows the distribution of historical Max Temperature values with the threshold marked.

Trend Analysis: Linear trend highlighting long-term patterns in Max Temperature over the past 30 years.

Team Semi Colons

We are dedicated to building data-driven solutions for practical environmental decision-making. This project demonstrates proficiency in:

Interactive data dashboards

Climate risk modeling

Statistical analysis and visualization

Python data science and geospatial tools

 
 Future Enhancements

Integration with real-time NASA/GPM/CPTEC APIs for live data

Event recommendation system based on predicted weather risk

Multi-variable analysis combining temperature, precipitation, and wind
