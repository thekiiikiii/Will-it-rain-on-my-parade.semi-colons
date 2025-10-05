# ☔ Will It Rain On My Parade? - Climate Risk Predictor

**NASA Space Apps Challenge: [Insert Your Local Event Name/Location]**

**Team Name:** [Your Team Name]
**Challenge:** Will It Rain On My Parade? (Earth Science Division)

## 🌟 Project Overview

This application provides a **personalized climate risk assessment** for any location and time of the year, going beyond short-term weather forecasting. By analyzing decades of open source NASA and partner agency data, the tool calculates the statistical **likelihood** (probability) that user-defined "adverse" weather thresholds will be exceeded for a future event.

## 🚀 Key Features

1.  **Personalized Thresholds:** Users define what constitutes "adverse" (e.g., above 30°C, or over 20 mm of rain/day).
2.  **Probability Risk Meter:** Provides a clear, single-percentage risk score based on historical frequency.
3.  **Trend Analysis:** Uses time-series visualization to show if the *probability* of the chosen adverse condition has increased or decreased over the last 30 years (illustrating local climate change impact).
4.  **Transparent Data Output:** Offers full data subset and metadata download (CSV/JSON) including units and original NASA/CPTEC source links, meeting open science standards.

## 💻 Technical Implementation

| Component | Technology | Data Sources Used |
| :--- | :--- | :--- |
| **Front-End/Dashboard** | **Streamlit (Python)** | Rapidly creates an interactive, web-based dashboard. |
| **Backend/Data Processing** | **Python (Pandas, Numpy)** | Handles historical data filtering, unit conversion, and statistical calculation. |
| **Data Sources** | **NASA Earthdata** | Primarily **MERRA-2** (Temperature, Wind) and **GPM** (Precipitation). |
| **Partner Data** | **CPTEC/INPE (Brazil)** | Integrated to show higher resolution climate trends for the South American region (demonstrates international partnership use). |

## 🛠️ How to Run Locally

1.  **Clone the Repository:** `git clone [Your Repository URL]`
2.  **Install Dependencies:** `pip install -r requirements.txt`
3.  **Run the App:** `streamlit run app.py`
4.  Open the local URL provided by Streamlit in your browser.

## 📊 Data & Variables

Our solution focuses on key variables vital for outdoor planning:

| Variable | NASA Data Product Used | Units |
| :--- | :--- | :--- |
| Max Temperature | MERRA-2 / SAMeT (CPTEC) | Kelvin (K) |
| Total Precipitation | GPM IMERG Daily | mm/day |
| Max Wind Speed | MERRA-2 | m/s |
| *[Your other variables here]* | *[Corresponding Source]* | *[Units]* |