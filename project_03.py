#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# %% import local climate data
def local_climate(file_path, location):
    # In the file_path, please write directory for the data folder
    # In the location, please fill the location among madison, los_angeles, austin, new_york
    
    if location == "madison":
        station = "14837"
    
    elif location == "los_angeles":
        station = "93134"

    elif location == "austin":
        station = "13958"

    elif location == "new_york":
        station = "94789"
    
    else:
        raise ValueError("Please choose location among madison, los_angeles, austin, new_york.")
    
    dfs = []

    for year in range(1991, 2021):
        climate_raw = pd.read_csv(f"{file_path}/LCD_USW000{station}_{year}.csv",
                                   usecols=[1, 5, 27],
                                   engine="python",
                                   on_bad_lines="skip")
        dfs.append(climate_raw)

    climate_df = pd.concat(dfs, ignore_index=True)
    climate_df = climate_df.dropna(subset=["DailyAverageDryBulbTemperature"])

    return climate_df

# %% import aggregated data
def aggregated_climate(file_path):
    # In the file_path, please write directory for the data folder

    dfs = []

    for location in ["madison", "new_york", "los_angeles", "austin"]:
        climate_df = local_climate(file_path, location)

        dfs.append(climate_df)

    climate_dfs = pd.concat(dfs, ignore_index=True)

    # DATE to Datetime
    climate_dfs["DATE"] = pd.to_datetime(climate_dfs["DATE"])

    # Rename locations
    climate_dfs["NAME"] = climate_dfs["NAME"].replace(
        {"MADISON DANE CO REGIONAL AIRPORT, WI US": "Madison, WI",
         "LOS ANGELES DOWNTOWN USC, CA US": "Los Angeles, CA",
         "JFK INTERNATIONAL AIRPORT, NY US": "New York, NY",
         "AUSTIN CAMP MABRY, TX US": "Austin, TX"})
    
    return climate_dfs

# %% Heat map
def temperature_heatmap(file_path):

    climate_dfs = aggregated_climate(file_path)

   
    # create year col
    climate_dfs["year"] = climate_dfs["DATE"].dt.year

    # temperature to number
    climate_dfs["DailyAverageDryBulbTemperature"] = pd.to_numeric(
        climate_dfs["DailyAverageDryBulbTemperature"], errors="coerce")
        
    # Temperature anomaly by locations
    temp_by_year_location = (
        climate_dfs.groupby(["NAME", "year"])["DailyAverageDryBulbTemperature"]
        .mean().reset_index())
    temp_by_year_location["anomaly"] = (temp_by_year_location.groupby("NAME")
                                        ["DailyAverageDryBulbTemperature"]
                                        .transform(lambda x: x - x.mean()))


    # heatmap data
    heatmap_data = temp_by_year_location.pivot(
        index="NAME",
        columns="year",
        values="anomaly")

    # plot heatmap

    plt.figure(figsize=(12, 5))

    sns.heatmap(heatmap_data, annot=True,
        fmt=".1f",
        cmap="coolwarm")

    plt.title("Temperature Anomalies by Location and Year (1991–2020)")
    plt.xlabel("year")
    plt.ylabel("Location")

    plt.tight_layout()
    
    # save image
    project_path = os.path.dirname(file_path)
    image_path = os.path.join(project_path, "images")
    plt.savefig(
        os.path.join(image_path,
                     "01.temperature_anomaly_heatmap.png"),
    dpi=300, bbox_inches="tight")

    plt.show()
# %%
if __name__ == "__main__":
    heatmap = temperature_heatmap("/Users/joyesang/Documents/UWM PhD program/2026 Summer/AAE_718/project/Project03_Climate_Data/Climate_Data_Project/data")
#%%
# line graphs
def temperature_line(file_path):

    climate_dfs = aggregated_climate(file_path)

    # Cleaning data
    climate_dfs["DailyAverageDryBulbTemperature"] = pd.to_numeric(
    climate_dfs["DailyAverageDryBulbTemperature"], errors="coerce")
    
      
    # rolling average
    climate_dfs["temp_rolling_14"] = (climate_dfs.groupby("NAME")
                                     ["DailyAverageDryBulbTemperature"]
                                     .transform(lambda x: 
                                     x.rolling(window=14, min_periods=1).mean()))
    # plot
    fig, axes = plt.subplots(2, 2, figsize=(18, 10), sharex=True)

    axes = axes.flatten()

    for ax, location in zip(axes, ["Madison, WI", "New York, NY", 
                                   "Los Angeles, CA", "Austin, TX"]):

        temp = climate_dfs[climate_dfs["NAME"] == location].copy()

        #temperature trend
        temp["date_num"] = temp["DATE"].map(pd.Timestamp.toordinal)
        x = temp["date_num"]
        y = temp["temp_rolling_14"]
        slope, intercept = np.polyfit(x, y, 1)
        temp["trend"] = slope * x + intercept

        ax.plot(temp["DATE"],
            temp["temp_rolling_14"],
            linewidth=1,
            label="2-week rolling average")

        ax.plot(temp["DATE"], temp["trend"],
            linestyle="--",
            linewidth=2,
            label="Linear trend")

        ax.set_title(location)
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (Celcius)")
        
    # create a legend for the whole figure
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper right", bbox_to_anchor=(1, 1))

    plt.suptitle("Two-Week Rolling Average Temperature and Linear Trend by Location (1991-2020)", y=1.02)
    plt.tight_layout()
    
    # save image
    project_path = os.path.dirname(file_path)
    image_path = os.path.join(project_path, "images")
    plt.savefig(
        os.path.join(image_path,
                     "02.temperature_line_graph.png"),
    dpi=300, bbox_inches="tight")

    plt.show()
    
# %%
if __name__ == "__main__":
    linegraph = temperature_line("/Users/joyesang/Documents/UWM PhD program/2026 Summer/AAE_718/project/Project03_Climate_Data/Climate_Data_Project/data")
# %%
