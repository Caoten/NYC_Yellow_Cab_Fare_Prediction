## Question: How is the Taxi Fare structured in NYC?
***

[Taxi Fare Rules:](https://www1.nyc.gov/site/tlc/passengers/taxi-fare.page)

* Standard Metered Fare:
    * 2.50 Dollar initial charge
    * Plus 50 cents per 1/5 mile when traveling above 12mph or per 60 seconds in slow traffic or when the vehicle is stopped
    * Plus 50 cents MTA State Surcharge for all trips that end in New York City or Nassau, Suffolk, Westchester, Rockland, Dutchess, Orange or Putnam             Counties
    * Plus 30 cents Improvement Surcharge
    * Plus 50 cents overnight surcharge 8pm to 6am
    * Plus 1.00 Dollar rush hour surcharge from 4pm to 8pm on weekdays, excluding holidays
    * Plus tips and any tolls
    * There is no charge for extra passengers, luggage or bags, or paying by credit card
    * The on-screen rate message should read: "Rate #01 – Standard City Rate.
    
    
* Airport Trips (John F. Kennedy Airport,LaGuardia Airport, Newark Airport ):
    * Trips to and from LaGuardia Airport (LGA) are charged the standard metered fare
    * Trips between Manhattan and John F. Kennedy Airport (JFK) in either direction:
        * 52 Dollar
        * Plus 50 cents MTA State Surcharge
        * Plus 30 cents Improvement Surcharge
        * 4.50 Dollar rush hour surcharge (4pm to 8pm weekdays, excluding legal holidays)
        * Plus tips and any tolls
        * The on-screen rate message should read "Rate #2- JFK Airport."
    * Trips between John F. Kennedy Airport (JFK) and other New York City destinations are charged the standard metered fare.
    * Trips to Newark Airport (EWR):
        * Standard metered fair.
        * Plus 17.50 Dollar Newark Surcharge.
        * Plus 30 cents Improvement Surcharge
        * Plus tip and tolls to and from EWR (passengers are charged for the drivers’ return tolls)
        * The on-screen rate message should read "Rate #3 - Newark Airport."
        
* Westchester & Nassau Counties:
    * The on-screen rate is "Rate #01 – Standard City Rate" within the City limit.
    * Once the taxi goes beyond the City limit to Nassau or Westchester, the on-screen rate message should read "Rate #04 – Out of City Rate to Nassau or Westchester." The metered fare     * is double the amount from the City limit to your destination.  Additionally, a message should appear on screen alerting the passenger of the rate change.
    * There is a 50 cents MTA State Surcharge and a 30 cents Improvement Surcharge.
    * Plus New York State Congestion Surcharge of 2.50 Dollars (Yellow Taxi) or 2.75 Dollars (Green Taxi and FHV) or 75 cents (any shared ride) for all trips that begin, end or pass through             * Manhattan south of 96th Street.
    
* Other Points Outside the City:
    * The Driver may choose whether to take such trips. The fare must be mutually agreed upon before the trip may begin.
    * Negotiated Flat Fare – The fare will be a Flat Rate negotiated between the Driver and Passenger.
    * The onscreen rate message should read "Rate #05 – Out of City Negotiated Flat Rate."
    * The 50 cents MTA State Surcharge must be added to the flat rate for any trip that ends in the following counties: Dutchess, Orange, Putnam, Rockland or Suffolk.
    * There is a 30 cents Improvement Surcharge.
    * Plus New York State Congestion Surcharge of 2.50 Dollars (Yellow Taxi) or 2.75 Dollars (Green Taxi and FHV) or 75 cents (any shared ride) for all trips that begin, end or pass through          Manhattan south of 96th Street.
***

## Notes:
        
**[How Taxi Meters Work:](https://auto.howstuffworks.com/taxi-meter.htm)->To put it simply, taxi meters measure distance and time. They then convert those measurements into a fare. Taxi fares are set by the area the taxi cab operates in -- in other words, it might cost more to travel the same distance or time in one city than it does in another. Fares may also change based on how many people are in the taxi, if the driver has to help you with your bags and if the taxi has to cross state or municipal lines to get you where you're going.No matter where they operate, however, all taxi meters measure the distance a cab covers, plus any time spent waiting. That way, the driver gets compensated for time, so they don't lose out on money just because they're stuck in traffic. It's also why a cab ride from point A to point B may cost you more when there's traffic than when there's not, even if the distance covered is the same.**

*The New York City Taxi and Limousine Commission’s official stance is: “It is impossible to pre-calculate a fare, because the meter rate depends on traffic, construction, weather, and route to the destination.”*

*Fares are set by the TLC and based on an initial charge, distance, and time, plus surcharges.”* 
-> tlc-factbook_2018 (Total Amount)

*The taximeter shall combine fractional measures of distance and time in accruing a unit of fare.Any combination of distance or time shall be computed by the taximeter in accordance with the National Institute of Standards and Technology Handbook 44.*

*The fare shall include pre-assessment of the unit currently being accrued; the amount due may therefore include a full unit charge for a final, fractional unit.*

-> Traffic Data Important(Volume Amount, Accidents), Weather Data?, ...

        
*The fare of taxi ride is function of the duration of the ride (sum of drop charge, distance charge and time charge).*

-> Summary-> Taxi Fare= Initial Charge+ Distance Charge + Charge Based on which Neigbourhood+ Time Charge-> Slow Traffic or Waiting Time
***

        
### Relevant Features:
* Pickup_Datetime
* Dropoff_Datetime
* Passenger_Count
* Trip_Distance
* Pickup_Lon
* Pickup_Lat
* Dropoff_Lon
* Dropoff_Lat
* RateCodeID
* Fare_Amt