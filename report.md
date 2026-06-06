<div align="center">
<h1 style="margin-bottom:0px;">
Examining Long-Term Temperature Trends in Four Regions in the U.S.:
</h1>
<h2 style="margin-top:0px">
Implications for Global Warming
</h2>

</div>

<p align="right" style="font-size:20px;">
<strong>Yesang Cho</strong>
</p>

### Project Repository
GitHub Repository: [Climate Data Project](https://github.com/joyesang/Climate_Data_Project)

## Introduction
<p style="text-indent: 30px;">
Climate change has emerged as one of the most important environmental challenges of the twenty-first century. According to Masson-Delmotte and colleagues (2018), the global climate system has already experienced substantial warming compared with the pre-industrial period, and human activities are identified as the primary driver of this change. They reported that global mean surface temperature increased by approximately 0.87°C during 2006–2015 relative to 1850–1900 levels, with continued warming observed in recent decades. </p>

<p style="text-indent: 30px;">
Although global average temperature provides an important indicator of climate change, examining regional temperature trends is essential for understanding how global warming is experienced in specific locations. Previous research has shown that warming does not occur uniformly across the globe (Sanderson et al., 2011). Both observational records and climate models indicate substantial geographical variation in the rate and magnitude of temperature change, with some regions warming considerably faster than the global average. Consequently, analyses of regional temperature patterns can complement global assessments by revealing how large-scale climate change is manifested at the local level.</p>

<p style="text-indent: 30px;">
Therefore, this study investigates long-term temperature trends in four selected locations (Madison, WI; Los Angeles, CA; Austin, TX; and New York, NY) using historical climate data from 1991 to 2020. By comparing temperature patterns over time, the analysis aims to determine whether these locations exhibit sustained warming trends consistent with broader global warming patterns. If warming trends are observed across all four locations, the findings will provide empirical evidence that global climate change is reflected in local temperature records and is observable across diverse regions of the United States.</p>
<br>

## Methods
<p style="text-indent: 30px;">
This study used historical climate data from the National Oceanic and Atmospheric Administration (NOAA) Local Climatological Data (LCD) database. Daily average air temperature records from 1991 to 2020 were collected for four locations in the United States. The analysis focused on the <code>DailyAverageDryBulbTemperature</code> variable, which represents the average daily air temperature measured at each weather station.
</p>
<p style="text-indent: 30px;">
Four locations were selected to represent major geographic regions of the United States: Los Angeles, California (West), Madison, Wisconsin (Midwest), New York, New York (East), and Austin, Texas (South). These locations were chosen to capture regional variation in climate conditions and to examine whether long-term warming trends were consistently observed across different parts of the country. 
</p>
<p style="text-indent: 30px;">
Two visualization methods were used to examine temperature trends. First, a heatmap of annual temperature anomalies was created for each location. Temperature anomalies were calculated as the difference between each year's average temperature and the long-term average temperature of the corresponding location during the study period. The heatmap provided a visual summary of periods that were warmer or cooler than average and facilitated comparisons across locations and years.
</p>
<p style="text-indent: 30px;">
Second, two-week rolling average temperatures were calculated and displayed using line graphs. Rolling averages were used to smooth short-term fluctuations in daily temperatures and highlight longer-term patterns. In addition, linear trend lines were included to assess whether temperatures generally increased or decreased over time. Together, the heatmap and rolling-average line graphs provided complementary perspectives on long-term temperature change and regional warming patterns.
</p>
<br>

## Results
#### (1) Temperature Anomalies Across Locations
<p style="text-indent: 30px;">
Figure 1 presents annual temperature anomalies for the four selected locations between 1991 and 2020. Positive values indicate years that were warmer than the long-term average for a given location, whereas negative values indicate cooler-than-average years.
</p>
<div align="center">
    <img src="/Climate_Data_Project/images/01.temperature_anomaly_heatmap.png" width="900">
    <p><em><strong> Figure 1.</strong> Annual temperature anomalies by location (1991–2020) </em></p>
</div>
<p style="text-indent: 30px;">
 The heatmap shows substantial year-to-year variation in temperature anomalies across all locations. Several years were characterized by below-average temperatures, particularly during the late 1990s and early 2000s. In contrast, positive anomalies appeared more frequently during the 2010s, with many locations exhibiting warmer-than-average temperatures in multiple consecutive years. <p>
 <p style="text-indent: 30px;">
 Although the magnitude of anomalies differed across locations, similar temporal patterns were observed. For example, all four locations experienced positive temperature anomalies during several years in the mid-to-late 2010s. Madison, WI recorded the largest positive anomaly in the dataset (2.3°C) in 2012, while Los Angeles, CA, Austin, TX, and New York, NY also exhibited multiple years with anomalies exceeding 1.0°C. Overall, the heatmap suggests that warmer-than-average years became more common during the latter part of the study period.
</p>
<br>

#### (2) Long-Term Temperature Trends
<p style="text-indent: 30px;">
Figure 2 displays two-week rolling average temperatures and linear trend lines for each location from 1991 to 2020. The rolling averages reveal strong seasonal fluctuations in all four locations, with temperatures increasing during summer months and decreasing during winter months. The magnitude of seasonal variation differed across locations, with Madison, WI and New York, NY showing larger annual temperature ranges than Los Angeles, CA and Austin, TX.
</p>
<div align="center">
    <img src="/Climate_Data_Project/images/02.temperature_line_graph.png" width="900">
    <p><em><strong>Figure 2.</strong> Two-week Rolling Average Temperature and Linear Trend by Location (1991-2020) </em></p>
</div>
<p style="text-indent: 30px;">
Despite these seasonal fluctuations, the linear trend lines indicate gradual increases in average temperature over the study period for all four locations. The upward slopes were visible across each location, although the magnitude of change varied. Austin, TX and New York, NY exhibited relatively steeper positive trends, whereas Los Angeles, CA and Madison, WI showed more moderate increases. Taken together, the rolling-average plots and trend lines demonstrate that long-term temperature patterns differed across locations while generally moving upward over time.
</p>

## Discussions
<p style="text-indent: 30px;">
The purpose of this study was to examine whether long-term temperature records from selected regions of the United States exhibited warming trends consistent with broader patterns of global climate change. The results indicate that all four locations (Madison, WI; Los Angeles, CA; Austin, TX; and New York, NY) experienced positive long-term temperature trends between 1991 and 2020. Although the magnitude of warming varied across locations, the linear trend lines consistently showed upward slopes, and positive temperature anomalies appeared more frequently during the later years of the study period. These findings suggest that rising temperatures were not confined to a single region but were observed across geographically diverse locations in the United States.
</p>
<p style="text-indent: 30px;">
The temperature anomaly heatmap further revealed that warmer-than-average years became more common during the 2010s compared with earlier decades. Similarly, the rolling-average temperature plots indicated that long-term warming occurred alongside regular seasonal fluctuations. Together, these findings suggest that short-term variability and seasonal cycles continue to influence local weather patterns, while longer-term temperature trends have generally moved upward over time.
</p>
<p style="text-indent: 30px;">
Several limitations should be considered when interpreting the findings. First, the study examined only four locations selected by the researcher to represent different geographic regions of the United States. Because the locations were not randomly selected and may not be representative of all climatic regions, the findings should not be generalized to the entire country. Second, the study period from 1991 to 2020 was chosen by the researcher and may influence the observed trends. Different starting and ending years could produce somewhat different estimates of temperature change. 
</p>
<p style="text-indent: 30px;">
Despite these limitations, the analysis provides evidence that temperatures have generally increased across four geographically distinct locations in the United States over the past three decades. The consistency of the observed warming patterns across multiple regions supports the broader conclusion that climate change is reflected not only in global averages but also in local temperature records.
</p>


<div style="page-break-before: always;"></div>

### References

<p style="padding-left: 40px; text-indent: -40px;">
Masson-Delmotte, V., Zhai, P., Pörtner, H.-O., Roberts, D., Skea, J., Shukla, P. R., Pirani, A., Moufouma-Okia, W., Péan, C., & Pidcock, R. (2018). <i>Global Warming of 1.5°C. An IPCC Special Report on the impacts of global warming of 1.5°C above pre-industrial levels and related global greenhouse gas emission pathways, in the context of strengthening the global response to the threat of climate change, sustainable development, and efforts to eradicate poverty</i>, Intergovernmental Panel on Climate Change. 
</p>
<p style="padding-left: 40px; text-indent: -40px;">
Sanderson, M. G., Hemming, D. L., & Betts, R. A. (2011). Regional temperature and precipitation changes under high-end (≥ 4 C) global warming. Philosophical Transactions of the Royal Society A: Mathematical, <i> Physical and Engineering Sciences, 369(1934),</i> 85-98.</p>
