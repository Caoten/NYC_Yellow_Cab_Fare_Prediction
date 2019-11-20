## Ideas for Feature Engineering and Transformation
***
* Feature Engineering:

    * Time-based (pickup and dropoff):
        * Date
        * year 
        * Month
        * Day of Week
        * Hour
        * is Weekend
        
    * Geolocation (Pickup):
        * Borough
        * Zone
        * Downtown and Midtown Manhattan?
        * Block (K-Means Clustering of Location ID)
        
   * Weather Condition:
        * Rainy
        * Snowy
        * Hot Day
        * Cold Day
        * Windy Day
        
    * Holiday
        * Season
        

* Transformation:
    * Target Feature (Fare_Amt):
        * Method: cut Methode
        * Categorical Feauture
        * Very High=
        * High=
        * Medium=
        * Normal=
        * Low=
    * Geolocation (Pickup):
        * Blocklevel=
    * Time based:
        * Divide in Hours -> Probably doesn't matter if it it 17:35 or 17:37
    
***
 * Idea:
     * easy Model vs. complex Model(Logistic Regression vs Neural Network vs XGBoost)
     * 1. Train with false Entry 
     * 2. Train without false Entry
     * 3. Train with new Features
     * 4. Train with new Features + Weather data
     
 * Problems:
     * 1. Value Range
     * 2. Overfitting vs Underfitting
 
