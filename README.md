# Climate Data Project

## Overview

This project investigates long-term temperature trends across four major U.S. cities between 1991 and 2020:

* Madison, Wisconsin
* New York City, New York
* Los Angeles, California
* Austin, Texas

**The goal of the project is to explore whether temperatures have increased over the past three decades and whether warming patterns differ across regions.**


## Data Source

The project uses Local Climatological Data (LCD) files from the National Oceanic and Atmospheric Administration (NOAA). [[data link]](https://www.ncei.noaa.gov/access/search/data-search/local-climatological-data-v2)

For each location, daily weather observations from 1991 through 2020 were collected. The analysis focuses on the `DailyAverageDryBulbTemperature` variable, which represents the average daily air temperature.

## Main Functions

### local_climate(`file_path`, `location`)

Loads daily temperature data for a selected city and combines all yearly files into a single dataframe.

Arguments

* `file_path`: path to the data folder
* `location`: one of:
    * "madison"
    * "new_york"
    * "los_angeles"
    * "austin"

* Returns: it returns a cleaned dataframe containing, 
    * DATE
    * NAME
    * DailyAverageDryBulbTemperature


⸻

### aggregated_climate(`file_path`)

* `file_path`: path to the data folder

* Returns: it combines temperature data from all four cities into a single dataframe.

⸻

### temperature_heatmap(`file_path`)

* `file_path`: path to the data folder

* Returns: Creates a temperature anomaly heatmap.
    
    1. Annual average temperatures are calculated for each cities.
    2. Temperature anomalies are computed by subtracting each city’s long-term mean.
    3. A heatmap is generated to visualize warmer-than-average and cooler-than-average years.
        - Positive values indicate warmer years relative to the city’s historical average.
        - Negative values indicate cooler years.

⸻

### temperature_rolling_subplots(`file_path`)

* `file_path`: path to the data folder

* Returns: it creates four line graphs, showing:
    1. 14-day rolling average temperatures
    2. Linear temperature trends
    3. Each subplot represents one city.

