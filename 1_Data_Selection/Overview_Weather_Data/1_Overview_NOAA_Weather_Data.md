#### Overview of Features in the NOAA Weather Data Csv File

|  Field Name  |                                                   Description                                                  | Data Type | Necessary |
|:------------:|:--------------------------------------------------------------------------------------------------------------:|-----------|-----------|
|    STATION   |                                           station identification code                                          |   String  |     No    |
| STATION_NAME |                                               name of the station                                              |   String  |     No    |
|   LATITUDE   |                                                                                                                |   Float   |     No    |
|   LONGITUDE  |                                                                                                                |   Float   |     No    |
|   ELEVATION  |                                                                                                                |   Float   |     No    |
|     DATE     |                the year of the record (4 digits) followed by month (2 digits) and day (2 digits)               |  Datetime |    Yes    |
|     AWND     | Average daily wind speed (meters per second or miles per hour as per user preference)                          |   Float   |    Yes    |
|     FMTM     |                  Time of fastest mile or fastest 1-minute wind (hours and minutes, i.e., HHMM)                 |   Float   |     No    |
|     PGTM     |                                 Peak gust time (hours and minutes, i.e., HHMM)                                 |   Float   |     No    |
|     PRCP     | Precipitation (mm or inches as per user preference, inches to hundredths on Daily Form pdf file)               |   Float   |    Yes    |
|     SNOW     |             Snowfall (mm or inches as per user preference, inches to tenths on Daily Form pdf file)            |   Float   |    Yes    |
|     SNWD     |                 Snow depth (mm or inches as per user preference, inches on Daily Form pdf file)                |   Float   |    Yes    |
|     TAVG     |                                       Average Temperature during the day                                       |   Float   |    Yes    |
|     TMAX     | Maximum temperature (Fahrenheit or Celsius as per user preference, Fahrenheit to tenths on Daily Form pdf file |   Float   |    Yes    |
|     TMIN     | Minimum temperature (Fahrenheit or Celsius as per user preference, Fahrenheit to tenths on Daily Form pdf file |   Float   |    Yes    |
|     TSUN     |                                         Daily total sunshine (minutes)                                         |   Float   |     No    |
|     WDF2     |                                  Direction of fastest 2-minute wind (degrees)                                  |   Float   |     No    |
|     WDF5     |                                  Direction of fastest 5-second wind (degrees)                                  |   Float   |     No    |
|     WSF2     |            Fastest 2-minute wind speed (miles per hour or meters per second as per user preference)            |   Float   |     No    |
|     WSF5     |            Fastest 5-second wind speed (miles per hour or meters per second as per user preference)            |   Float   |     No    |
|     WT01     |                              Fog, ice fog, or freezing fog (may include heavy fog)                             |   Bool    |    Yes    |
|     WT02     |                     Heavy fog or heaving freezing fog (not always  distinguished from fog)                     |   Bool    |    Yes    |
|     WT03     |                                                     Thunder                                                    |   Bool    |    Yes    |
|     WT04     |                                 Ice pellets, sleet, snow pellets, or small hail                                |   Bool    |    Yes    |
|     WT05     |                                          Hail (may include small hail)                                         |   Bool    |    Yes    |
|     WT06     |                                                  Glaze or rime                                                 |   Bool    |    Yes    |
|     WT07     |                     Dust, volcanic ash, blowing dust, blowing sand, or blowing obstruction                     |   Bool    |    Yes    |
|     WT08     |                                                  Smoke or haze                                                 |   Bool    |    Yes    |
|     WT09     |                                            Blowing or drifting snow                                            |   Bool    |    Yes    |
|     WT11     |                                            High or damaging winds                                              |   Bool    |    Yes    |                              |     WT13     |                                                      Mist                                                      |   Bool    |    Yes    |
|     WT14     |                                                   Drizzle                                                      |   Bool    |    Yes    |
|     WT16     |                    Rain (may include freezing rain, drizzle, and freezing drizzle)                             |   Bool    |    Yes    |
|     WT17     |                                             Freezing rain                                                      |   Bool    |    Yes    |
|     WT18     |                    Snow, snow pellets, snow grains, or ice crystals                                            |   Bool    |    Yes    |
|     WT19     |                             Unknown source of precipitation                                                    |   Bool    |     No    |
|     WT22     |                                   Ice fog or freezing fog                                                      |   Bool    |     Yes   |
