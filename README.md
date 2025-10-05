<h1>
    WILL IT RAIN ON MY PARADE
</h1>
 Climatological Risk Assessment Platform
Team and Project Overview
Attribute	Detail
Team Name	Semi Colon
Challenge	Will It Rain On My Parade?
Domain	Earth Science, Applied Climatology
Status	Functional Prototype

Export to Sheets
<hr>

Executive Summary
Will It Rain On My Parade? is a web-based platform that provides a probabilistic climatological assessment for long-range event planning. It utilizes decades of open-source NASA Earth Observation (EO) and international partner data to calculate the statistical likelihood that user-defined adverse weather conditions will be exceeded. The application bridges the gap between short-term weather forecasting and long-term planning by converting raw geospatial data into actionable, risk-quantified metrics.

<hr>

Core Functionality and Scientific Rigor
Personalized Threshold Modeling
The application's core innovation is the capability to accept user-defined 'adverse' thresholds, establishing a precise statistical baseline for every risk calculation.

Risk Quantification: The system compares 30+ years of historical data to the user's specific input (e.g., maximum temperature ≥308.15 K) to calculate the exact probability percentage of exceedance.

Variable Analysis: The platform processes critical variables including Maximum Temperature, Total Precipitation, Maximum Wind Speed, and a calculated Discomfort Index (modeling combined heat and humidity effects).

Universal Data Transparency
Adhering strictly to Open Science principles, the platform ensures that its methodology and sourcing are fully transparent.

Probabilistic Visualization: Statistical results are delivered via an intuitive Risk Meter and a detailed Historical Distribution Histogram, which visually maps the user's risk threshold against the full climatological record.

Metadata Compliance: Full subsetted data and metadata are instantly downloadable in CSV and JSON formats. The output includes essential fields for scientific reproducibility, such as variable units, query coordinates, and the original NASA/CPTEC source links.

<hr>

Technical Implementation
The platform utilizes a modern, Python-based stack optimized for efficient data processing and interactive visualization.

Architecture
Component	Technology	Technical Function
Frontend/UI	Streamlit	Facilitates rapid prototyping and deployment of the interactive dashboard and user controls.
Geospatial Resolution	geopy (Nominatim)	Translates human-readable location inputs into high-precision Latitude and Longitude for exact data querying.
Data Processing Core	Pandas, NumPy	Executes all statistical operations, unit conversions, and filtering against historical data records.
Visualization Layer	Plotly Express	Generates dynamic, high-fidelity statistical visualizations (Histograms, Time Series) for technical review.

Export to Sheets
Data Sources Utilized
The application is architected for integration with authoritative, long-term datasets:

NASA Earth Observation: Primarily integrated for MERRA-2 (Temperature, Wind) and GPM (Precipitation) historical products.

Partner Integration: The methodology is validated for integration with regional high-resolution datasets, such as those provided by CPTEC/INPE, demonstrating adaptability to diverse data schemas.

<hr>



Developed by Team Semi Colon using NASA's commitment to Open Data for advancing climate resilience and predictive planning.
