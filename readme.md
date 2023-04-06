## Oslo bysykkkel prosjekt 

### relevant sources
1. https://oslobysykkel.no/apne-data
2. https://statistikkbanken.oslo.kommune.no/webview/index.jsp?catalog=http%3A%2F%2Fstatistikkbanken.oslo.kommune.no%3A80%2Fobj%2FfCatalog%2FCatalog52&submode=catalog&mode=documentation&top=yes

### how the program works
source code is python
the database is created in azure





### steps to be taken
1. extract all the availbel data and store it in a database
2. create the database architecture 
3. create the etl pipeline

stretch
# 4. use machinelearning to forcast the demand
### Predicting availability the next hour for each station
We are focusing on predicting availability the next hour 
by focusing on each stations and looking at how many trips started each hour.
This will be a easy and cost efficient approach 

there are possibilities to include end station data as parameter that will contribute to the accuracy 
but it is important to consider the trade-offs between model accuracy and model complexity when deciding which features to include in the analysis.
