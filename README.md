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