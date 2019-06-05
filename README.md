# SmartStart 
Findint best locations to start a new business

##  Problem
According to [Key Small Business Statistics Journal (Jan. 2019 edition)](http://www.ic.gc.ca/eic/site/061.nsf/eng/h_02689.html), less than 45% of small businesses (defined by number of employess in 5-100 range) survive through the first 10 years. 

![Key Small Business Statistics survival plot](https://github.com/Payampakarha/SmartStart/images/Small_business_stats.png "survival plot")

A particular reason for this are the large number of Business Imigration Statuses that the Government of Canada grants. These investors will bring a good value to the society both in terms of financial benefits, and employment. However, most immigrants have very limited knowledge about the city, and business market they are targeting. 

The idea behind SmartStart was to create a data product that can automatically suggest optimal locations for a new business, within a city. The interface needs to be both very simple to use, and daptive to various business types, and stragtegies. 

## Methodology 

### Overview 
To solve this problem, first a number of important features for a new business location should be considered. Depending on the nature of the business, and its target audience, the parameters can vary. However, the following are more or less universally important for every small business: 

⋅⋅* Neighbourhood inhabitants population (can be clustered by income, gender, age, ...) 
⋅⋅* Similar business locations proximity (can include a metric of their success e.g. rating, revenue, time since opened, ...) 
⋅⋅* Commuting/Transit volume 
⋅⋅* Land value 
⋅⋅* Crime rate 

.For any business kind, the features above could be waited differently. Some features like similar business proximity can be considered both as a positive, or negative impact in some cases. 

For this project, only the first two features are focused on (based on availability of data). Moreover, to further narrow down the problem, only businesses who value customers living in their vicinity, and disfavor nearby similar businesses are chosen. In customer prospective, this would translate to business kinds that you would preferably choose the closest to your home. Examples of such business are :
 
⋅⋅* Daily used product providers, such as grocery, bakery, dairy, etc.  
⋅⋅* Landry services
⋅⋅* Hair care 
⋅⋅* Athletics and recreation centers 

. Next, the locations are needed to be optimized based on the features. This can be done in two ways : 

⋅⋅* Use a Machine Learning (ML) algorithm, trained on currently existing businesses of each kind and their success rate 
⋅⋅* Use a multi-objective optimization algorithm to find optimal locations mathematically

.Since most information that can be used as a metric for success rate of a business are confidential (e.g. revenue, number of customers per day), and the public information (e.g. ratings, years since opened) can potentially be biased/misleading, the second solution is chosen for SmartStart. 

### Data
Canada's [census data (2011,2016)](https://www12.statcan.gc.ca/datasets/index-eng.cfm?Temporal=2016) includes information on population per pre-defined neighborhoods. This data is used to interpolate an estimation for current population density for every neighbourhoud. 

For locations of various business within a city, [Google Maps Search Results API](https://developers.google.com/places/web-service/search) is used to query business keywords and save the results. 

### Analysis Pipeline 





## How to 
The interaction with the application is very simple and intuitive. The users chooses a city, and business of his/her interest. The slide-bar allows to weight the two possible aspects of importance (PCF, or PS). For every selection, the button "Find best locations!" will display the results in the format of a table with locations and scores. At this point, the user can visualize the results into an interactive map using "Show on map!" button. 
