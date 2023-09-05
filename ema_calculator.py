
import pandas as pd 

def calculate_ema():

    """
    Calculate the 7-day Exponential Moving Average (EMA) for election poll data.

    This function computes the EMA for each candidate based on the provided poll data.
    The EMA is then saved to a CSV file named 'trends.csv'.

    The EMA is computed with a span of 7 days, making it a 7-day EMA.
    
    """
    # Reading data directly from 'polls.csv'
    polls_df = pd.read_csv('polls.csv')

    # Converting 'Date' column to datetime data type
    polls_df['Date'] = pd.to_datetime(polls_df['Date'])

    # setting the 'Date' column as the index for the DataFrame
    polls_df.set_index('Date', inplace=True) 
    polls_df = polls_df.sort_index()

    # calculate the daily average for the polls
    daily_avg = polls_df.groupby(polls_df.index).mean()
    
    # defining the date range for which EMA should be computed
    start_date = pd.to_datetime('2023-10-11')
    end_date = polls_df.index.max()
    date_range = pd.date_range(start_date, end_date)
    # Initializing a DataFrame to store the EMA values
    trends_df = pd.DataFrame(index=date_range)
    
    # List of candidates for whom EMA needs to be computed
    candidates = ['Bulstrode', 'Lydgate', 'Vincy', 'Casaubon', 'Chettam', 'Others']
    span = 7
    # Computing the 7-day EMA for each candidate and storing in the trends_df DataFrame
    for candidate in candidates:
        trends_df[candidate] = daily_avg[candidate].ewm(span=span, adjust=False).mean().reindex(trends_df.index)

    # adding a 'Date' column to the trends_df DataFrame
    trends_df.reset_index(inplace=True)
    #trends_df['Date'] = trends_df.index.date
    trends_df.rename(columns={"index": "Date"}, inplace=True)
    # saving the trends_df DataFrame as trends.CSV 
    trends_df.to_csv('trends.csv', index=False)
