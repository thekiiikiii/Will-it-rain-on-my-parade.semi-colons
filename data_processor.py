import numpy as np
import pandas as pd
from datetime import datetime

def get_historical_data(lat, lon, parade_date, variable_name, units):
    num_years = 30
    month, day = parade_date.month, parade_date.day
    start_year = datetime.today().year - num_years
    dates = [datetime(year=start_year+i, month=month, day=day) for i in range(num_years)]

    if variable_name == "Max Temperature":
        values = np.random.uniform(298.15, 313.15, num_years)
    elif variable_name == "Total Precipitation":
        values = np.random.uniform(0,50,num_years)
    elif variable_name == "Max Wind Speed":
        values = np.random.uniform(0,25,num_years)
    elif variable_name == "Discomfort Index":
        values = np.random.uniform(25,35,num_years)
    else:
        values = np.random.uniform(0,10,num_years)

    df = pd.DataFrame({
        "Date": [d.strftime('%Y-%m-%d') for d in dates],
        variable_name: values
    })
    df.attrs['metadata'] = {"Variable": variable_name, "Units": units, "Notes": "Simulated historical data."}
    return df

def calculate_risk(df, variable_name, threshold_value):
    exceed_count = (df[variable_name] > threshold_value).sum()
    total = len(df)
    risk_percentage = (exceed_count / total) * 100
    stats = {
        "risk_percentage": round(risk_percentage,1),
        "historical_mean": round(df[variable_name].mean(),1),
        "historical_max": round(df[variable_name].max(),1)
    }
    return stats, df

def generate_downloadable_output(stats, df, lat, lon, threshold, variable_name):
    metadata = {
        "Query_Date": datetime.now().isoformat(),
        "Location": f"{lat},{lon}",
        "Variable": variable_name,
        "Threshold": threshold,
        "Risk_Percentage": stats["risk_percentage"]
    }
    json_output = {"metadata": metadata, "historical_data": df.to_dict("records")}
    csv_output = df.copy()
    csv_output["Exceeds_Threshold"] = csv_output[variable_name] > threshold
    return json_output, csv_output.to_csv(index=False)
