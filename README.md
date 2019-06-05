# SmartStart 
Finding best locations to start a new business

##  Problem
According to [Key Small Business Statistics Journal (Jan. 2019 edition)](http://www.ic.gc.ca/eic/site/061.nsf/eng/h_02689.html), less than 45% of small businesses (defined by number of employess in 5-100 range) survive through the first 10 years. 

![Key Small Business Statistics survival plot](https://github.com/Payampakarha/SmartStart/blob/master/images/Small_business_stats.png "survival plot")

A particular reason for this are the large number of Business Imigration Statuses that the Government of Canada grants. These investors will bring a good value to the society both in terms of financial benefits, and employment. However, most immigrants have very limited knowledge about the city, and business market they are targeting. 

The idea behind SmartStart was to create a data product that can automatically suggest optimal locations for a new business, within a city. The interface needs to be both very simple to use, and daptive to various business types, and stragtegies. 

## Methodology 

### Overview 
To solve this problem, first a number of important features for a new business location should be considered. Depending on the nature of the business, and its target audience, the parameters can vary. However, the following are more or less universally important for every small business: 

* Neighbourhood inhabitants population (can be clustered by income, gender, age, ...) 
* Similar business locations proximity (can include a metric of their success e.g. rating, revenue, time since opened, ...) 
* Commuting/Transit volume 
* Land value 
* Crime rate 

.For any business kind, the features above could be waited differently. Some features like similar business proximity can be considered both as a positive, or negative impact in some cases. 

For this project, only the first two features are focused on (based on availability of data). Moreover, to further narrow down the problem, only businesses who value customers living in their vicinity, and disfavor nearby similar businesses are chosen. In customer prospective, this would translate to business kinds that you would preferably choose the closest to your home. Examples of such business are :
 
* Daily used product providers, such as grocery, bakery, dairy
* Landry services
* Hair care 
* Athletics and recreation centers 

. Next, the locations are needed to be optimized based on the features. This can be done in two ways : 

* Use a Machine Learning (ML) algorithm, trained on currently existing businesses of each kind and their success rate 
* Use a multi-objective optimization algorithm to find optimal locations mathematically

.Since most information that can be used as a metric for success rate of a business are confidential (e.g. revenue, number of customers per day), and the public information (e.g. ratings, years since opened) can potentially be biased/misleading, the second solution is chosen for SmartStart. 

### Data
Canada's [census data (2011,2016)](https://www12.statcan.gc.ca/datasets/index-eng.cfm?Temporal=2016) includes information on population per pre-defined neighborhoods. This data is used to interpolate an estimation for current population density for every neighbourhoud. 

For locations of various business within a city, [Google Maps Search Results API](https://developers.google.com/places/web-service/search) is used to query business keywords and save the results. 

### Analysis procedure
The following image, shows the schematics of the analysis procedure used for SmartStart. 

![Pipeline Flowchart](https://github.com/Payampakarha/SmartStart/blob/master/images/Pipline_flowchart.png "pipeline flowchart")

. The flowchart shows the flow of the data, as it is grabbed from the source, processed, and visualized in the app. Each arrow on this figure represents a notebook, in this repository, except for the last (most right) that represents the whole web application folder. 

Neighbourhood profiles data includes a column in the format of a "polygon" that defines the corner points of the shape, in terms of latitutde, and longitude. "Shapely" python library is used to handle the polygons, and also to calculate the area of each neighbourhood. Next, "Geopandas" is used to frame the data including this shapes. The population density is calculated simply by dividing population by area. The data is cleaned by simply removing irrelevant/unused columns, and finally the cleaned data is stored in a new .shp file to be used for further analysis. An example of a profile map, overlayed by the existing business locations (supermarkets in this case) is shown in the figure below. 

![profiles map](https://github.com/Payampakarha/SmartStart/blob/master/images/Density_profiles_overlayed.png "profiles map")

The google places API provides data in the format of list of dictionaries including keys such as name, location (coordinates), and rating. However, as it lists the results of a search keyword within a range, the data will include lots of irrelevant places. For instance, searching for "swimming pool" as the keyword shows a lot of pool and bathtub services. Hence, the data cleaning procedure was not trivial and required manual listing of irrelevant items. Finally, the cleaned data is stored in a separate file in the format of a pandas dataframe. 

Two functions are used to define Potential Customer Flow (PCF) and Proximity Score, for every point within the city. The first is an integral of population density within a given radius, weighted by 1/distance to favor closer inhabitants, while the latter is calculated by simply suming all distances to similar business locations. The optimization is done, using "platypus" library and by testing 5 different algorithms (NSGAII, GDE3, IBEA, SMPS0, and SPEA2) which resulted in the choice of NSGAII algorithm which quantitatively resulted in more efficient pareto finding. The resulted pareto points are stored in a data file for 100 points. 

A mapper notebook is used to generate maps in the form of html files, using "folium" library. This process generation could be done interactively through the web-app but, it resulted in long processing time, and security problems by rewriting files on the google-cloud platform. Hence, it is done in a separate pre-processing step. 

Finally, the application simply selects a list of 5 pareto points, based on user-input weight to the two parameters, and the corresponding map html file. The resulting poitns are listed on a table on the app main page, while the map can be accessed via a separate button, in case visualization is desired. 


## User interface
Google cloud is used to deploy the [web-app](https://smartstart-1558116852059.appspot.com/) online. 

The interaction with the application is very simple and intuitive. The users chooses a city, and business of his/her interest. The slide-bar allows to weight the two possible aspects of importance (PCF, or PS). For every selection, the button "Find best locations!" will display the results in the format of a table with locations and scores. At this point, the user can visualize the results into an interactive map using "Show on map!" button. 
