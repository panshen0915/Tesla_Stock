### Import different library, numpy, matplotlib.pyplot, pandas, time, etc. #### ### This code do a simple data analysis of Tesla Stock Price     ######
### All of the stock prioce data are downloaded from
### https://www.marketwatch.com/investing/stock/tsla/download-data?startDate=12/7/2018&endDate=12/6/2019
#### Import different library
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import pandas as pd
######## This part is to combine the few single cvs to one cvs file
######## Read data from a loop, reshape data and resave data are conducted
TSLA_18_24 = []      ## Create an empty array for the purposing combine different cvs file
Item_header = ['Date', 'Open', 'High', 'Low','Close','Volume']    #### Customize different header name
for i in range(1, 6):                                             #### A for loop to import differe cvs file
    TSLA_csvname = f"TSLA_{i}.csv"                                #### File name, from TSLA_1 to TSLA_5
    TSLA_df = pd.read_csv(TSLA_csvname, header=None, skiprows=1)  #### Read each cvs data, heaser is excluded
    TSLA_df = TSLA_df.iloc[::-1].reset_index(drop=True)           #### Reverse the index of rows of each file
                                                                  # to make sure the row are indexed base time
    TSLA_18_24.append(TSLA_df)                                    #### Append data of each cvs file to TSLA_18_24 empty array
TSLA_ALL_df = pd.concat(TSLA_18_24, ignore_index=True)            #### Combine and stack all data into TSLA_ALL
TSLA_ALL_df.columns = Item_header                                 #### Add customized heasder
TSLA_ALL_df.to_csv('TSLA_6_Years.csv', index=False, header=True)  #### Save all data into new cvs file 'TSLA_6_Years.csv'


#### This part is to do simple price analysis with my own function,
#### Visilize the price change
def daily_price_analysis(filename):
    time_price_data = pd.read_csv(filename)                       ###### read the data from TSLA_6_Years.csv file
    time_data = pd.to_datetime(time_price_data['Date'])           ###### Extract the information of time
    stock_prices = time_price_data[['Open', 'High', 'Close']]     ###### Extract the data of price at "Open", "High",
                                                                  ###### and "Close"
    ##### Plot and visualize the price change into one figure
    plt.figure(figsize=(12, 8))                                    ###### Define figure size
    plt.plot(time_data, stock_prices['Open'], label='Open Price')  ###### Plot the price at "Open" verse time
    plt.plot(time_data, stock_prices['High'], label='High Price')  ###### Plot the price at "High" verse time
    plt.plot(time_data, stock_prices['Close'], label='Close Price') ###### Plot the price at "Close" verse time
    plt.title('Stock Price Change over Time ($)')                  ##### Name the tile of the plotted figuire
    plt.xlabel('Time (Year)')                                      ##### Define the label of X-axis data
    plt.ylabel('Price Per Share ($)')                                  ##### Define the label of Y-axis
    plt.legend()                                                   ##### Show legend
    plt.grid(True)
    plt.savefig('Stock Price Change over Time_2018-2024 ($)')      ##### Save the plot with name
                                                                   ##### 'Stock Price Change over Time_2018-2024 ($)'
    return time_data, stock_prices['Close']
#### This part is to do simple price prediction analysis with define function,
#### The simple Polynomial fit function is used an example
def future_prices_prediction(time_data, close_prices):
    x = np.arange(len(time_data))                    ##### Creat an array which gather the information of time
    y = close_prices.values                          ##### Use the price at "Close" for function fit analysis

    polynomial = Polynomial.fit(x, y, deg=1)           #### Use the most simple Polynomial.fit with degree = 1

    # Extend x values into the future for prediction
    future_x = np.arange(len(x) + 4 * 365)           #### For the data viosulaiton purpose, generate array which include
                                                     #### Past data and the future 4 years
    future_dates = pd.date_range(start=time_data.min(), periods=len(future_x), freq='D')
                                                     ##### Create the data of x-axis for, which include past date and future date

    # Use the polynomial to predict past and future prices
    predicted_prices = polynomial(future_x)                   ##### Get the data for the future 4 years from the Polynomial.fit

    plt.figure(figsize=(12, 8))                               #### Give the size of figure
    plt.plot(time_data, close_prices, label='Past Close Prices')    ##### Close price is ploted for the past years,
    plt.plot(future_dates, predicted_prices, label='Predicted Polynomial Data', linestyle='--') ##### Predicted Price over the future years
    plt.title('Past and Future Prices (TSLA)')                ##### Figure name
    plt.xlabel('Time (Year)')                                 ##### Name for X-axis
    plt.ylabel('TSLA Stock Price (Past and Future) Change over Time($)')   ##### Name for y-axis
    plt.legend()         ##### Keep legend
    plt.grid(True)       ##### Add grid
    plt.savefig('Stock Price (Past and Future)') ##### Name of save figure
    plt.show()          ##### Show the plotted figure after the running

time_data, close_prices = daily_price_analysis('TSLA_6_Years.csv')    ##### Call function  "daily_price_analysis"
future_prices_prediction(time_data, close_prices)                     ##### Call function "future_prices_prediction"


