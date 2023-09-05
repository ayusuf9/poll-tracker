# importing the neccessary modules from the respective scripts. 
from web_scraper import scrape_poll_data
from data_processing import process_poll_data
from ema_calculator import calculate_ema
from logger import log_error
from datetime import datetime


ELECTION_DAY = datetime(2024, 10, 10)

def main():
    """
    Main function to orchestrate the process of scraping web data, processing it,
    calculating the Exponential Moving Average (EMA), and handling any potential errors.
    
    The function performs the following steps:
    1. Scrapes poll data from the web and saves it to polls.csv.
    2. Processes the scraped data (if any additional processing is needed).
    3. Calculates the 7-day EMA for the poll data and saves the results to trends_ema.csv.
    4. In case of any errors during the above steps, logs the error message to error_log.txt.
    """
    # Checking if today is after the election day
    if datetime.now().date() > ELECTION_DAY.date():
        return

    try:
        scrape_poll_data() # scrape poll data from the web
        #polls_df = process_poll_data() # processing the poll data depending.. 
        # calculating the EMA for the poll data and save to trends.csv
        calculate_ema()
    except Exception as e:
         # If there's any error in the above steps, log the error message
        log_error(str(e))

# ensuring the main function is executed only when this script is run directly (not imported)
if __name__ == "__main__":
    main()
