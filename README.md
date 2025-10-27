Midterm Report

Data Collection:
The initial plan to use SteamDB and Steam API fell short since many endpoints are not available 
to regular users. The ones that are available do not keep track of temporal data, and so I am 
only able to scrape current concurrent player count and current price, not release price. I 
ended up using 2 kaggle datasets and processing them to obtain data I wanted.
https://www.kaggle.com/datasets/whigmalwhim/steam-releases?select=game_data_all.csv
https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games


Data Processing:
From the first data set I took peak_players, rating, and primary_genre data, while from the second
I took Release date, Price, and Categories data. I processed the Categories into a one hot encoding
of Single-player and Multi-player. I also processed the Release date into 3 columns for day, month
and year. Finally I joined the two datasets by the steam appid, which I had to process since the 
two datasets keep track of it differently.

Data Visualization:
I made many graphs for distribution and correlation, and these can be seen in the video 

Model Training:
Currently not started

Video:
https://youtu.be/9S-Sq2wuPPE