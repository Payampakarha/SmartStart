# SmartStart 
Findint best locations to start a new business

##  Problem
According to [Key Small Business Statistics Journal (Jan. 2019 edition)](http://www.ic.gc.ca/eic/site/061.nsf/eng/h_02689.html), less than 45% of small businesses (defined by number of employess in 5-100 range) survive through the first 10 years. 

![Key Small Business Statistics survival plot](https://github.com/Payampakarha/SmartStart/images/Small_business_stats.png "survival plot")



## Data 
The application uses Canada's census data (2011,2016) for population per neighbourhoud within a city to interpolate an estimation for population density for every neighbourhoud. For locations of various business within a city, Google Maps Search Results API is used to query business keywords and save the results. 

## Technical analysis and methodology
At the simplest representation of important parameters for a new business location, the application considers only Potential Customer Flow (PCF), and Proximity Score (PS) with respect to similar business locations. The PCF is calculated via integration of population density in the vicinity of a point, weighted by inversed distance (to favor inhabitants living closer to the business). The proximity score is calculated via summation of distance of any point within the city to
all  coordinates for businesses of the same type.  

Next, a multi-variant multi-objective algorithm is used to maximize both score functions. The results inlcude pateo points with maximized value of a function while the value cannot be improved unless the value of the other function is sacrificed. A total of 100 pateo points are stored for a given business and city. A choice of 5 points are suggested by the app according to user's preferred weight to each aspect (PS, or PCF). The user can simply modify the weights to browse various
options of locations. 

## How to 
The interaction with the application is very simple and intuitive. The users chooses a city, and business of his/her interest. The slide-bar allows to weight the two possible aspects of importance (PCF, or PS). For every selection, the button "Find best locations!" will display the results in the format of a table with locations and scores. At this point, the user can visualize the results into an interactive map using "Show on map!" button. 
