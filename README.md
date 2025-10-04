Goal:
The goal of this project is to predict average daily players for a video game on Steam.

Data:
I will use steamDB to collect data on games released in 2025. I expect the main drivers to be price, genre, review score, and developer reputation, but I will try other factors when training my model to see if there are some unexpected factors.

Model:
My initial plan is to use a linear regression model for predictions. I expect this to work the best, as I have used this before to predict housing prices and it worked well. I'll supplement it with PCA and XGBRegressor.
Price will be a float
Genre will be a one hot encoded value
Review score will be a int, rounded to the nearest one
Developer Reputation will look at average daily players from past games from the developer

Visualization:
The project will be hard to visualize as I plan on using many dependent variables. I may break out some variables for a 1 to 1 comparison if they seem to have strong correlation, but my hypothesis is that there will not be clear patterns when only looking at one factor.

Test:
I plan to do a random 70 - 15 - 15 split on the data for training, validation, and testing

FIXES:
1. I'll include pred vs actual graphs, and use correlation heatmaps to see colinearity.
2. I will incorporate data from the past 3 years. I think it's best to not include the COVID years, as I believe gaming numbers would be unusually high during that time.
3. Since I am including more data, I think the data should have equal splits for every year. Additionaly, after looking at the initial results I may also try and train separate models on important categorical data such as genre.
4. N/A
5. Most of the suggested factors would be included in genre, but I'll take into account special dates. Ideally, this project would be useful in helping streamers decide what game would be good to stream, as concurrent player count tends to have a positive correlation with viewership. In this scenario, most streamers would stream during Christmas anyways, and so it would be a good idea to either normalize data, or give it some special treatment. For example, holiday themed games would be more successful during Christmas than other months. Will have to see and adapt the model.
