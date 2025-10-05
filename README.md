<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Will It Rain On My Parade? - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 40px;
            background-color: #f9f9f9;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 0.3em;
        }
        h2 {
            font-size: 2em;
            margin-top: 1.5em;
        }
        h3 {
            font-size: 1.5em;
            margin-top: 1em;
        }
        code {
            background-color: #eaeaea;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            margin: 0.5em 0 1em 1.5em;
        }
        blockquote {
            border-left: 5px solid #2c3e50;
            padding-left: 15px;
            color: #555;
            font-style: italic;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>

    <h1>Will It Rain On My Parade?</h1>
    <p><strong>Team:</strong> Semi Colons</p>
    <p>
        "Will It Rain On My Parade?" is a professional climate risk dashboard that estimates the likelihood of adverse weather conditions
        for any outdoor event. Leveraging historical Earth observation data from NASA and partner sources, the app provides actionable insights 
        for planning events based on temperature, precipitation, wind speed, or overall discomfort.
    </p>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li><strong>Location-based analysis:</strong> Enter a city or coordinates to fetch historical data for the target location.</li>
            <li><strong>Custom date selection:</strong> Analyze specific dates to estimate the probability of adverse conditions.</li>
            <li><strong>Condition selection:</strong> Evaluate Max Temperature, Total Precipitation, Max Wind Speed, or Discomfort Index.</li>
            <li><strong>Threshold customization:</strong> Set thresholds to define what constitutes an adverse condition.</li>
            <li><strong>Probability and risk calculation:</strong> Quantifies the likelihood that historical data exceeded the chosen threshold.</li>
            <li><strong>Visualizations:</strong> Histogram of historical occurrences vs threshold; Trend analysis with linear regression.</li>
            <li><strong>Data export:</strong> Download results in JSON or CSV formats for further analysis.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Technical Overview</h2>
        <ul>
            <li><strong>Frontend:</strong> Streamlit for an interactive web-based interface.</li>
            <li><strong>Backend:</strong> Python with Pandas and NumPy for data handling and calculations; Plotly for interactive visualizations; Geopy for geocoding.</li>
            <li><strong>Data Sources:</strong> Structured simulated historical climate data (easily replaceable with NASA MERRA-2, GPM, CPTEC).</li>
            <li><strong>Risk Calculation:</strong> Calculates proportion of historical data exceeding user-defined thresholds; summarizes mean, max, and probability metrics.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Installation & Setup</h2>
        <ol>
            <li><strong>Clone the repository:</strong>
                <pre><code>git clone https://github.com/your-repo/will-it-rain-on-my-parade.git
cd will-it-rain-on-my-parade</code></pre>
            </li>
            <li><strong>Install dependencies:</strong>
                <pre><code>pip install streamlit pandas numpy plotly geopy</code></pre>
            </li>
            <li><strong>Run the app:</strong>
                <pre><code>streamlit run app.py</code></pre>
                <p>Open the displayed URL (usually <code>http://localhost:8501</code>) to interact with the dashboard.</p>
            </li>
        </ol>
    </div>

    <div class="section">
        <h2>Usage Workflow</h2>
        <ul>
            <li>Define Event Location: Enter city name or latitude/longitude coordinates.</li>
            <li>Select Event Date: Specify the exact date of the planned event.</li>
            <li>Choose Condition: Select a weather variable (e.g., Max Temperature, Total Precipitation).</li>
            <li>Set Threshold: Adjust the threshold for adverse conditions.</li>
            <li>View Results: Risk score (%), summary statistics, histogram, and trend visualization.</li>
            <li>Download Data: Export detailed data in JSON or CSV format.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Example Output</h2>
        <ul>
            <li>Risk Score: 65% probability that Max Temperature ex
