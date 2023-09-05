# Election Poll Tracker
This project scrapes election poll data, processes the data, calculates the 7-day Exponential Moving Average (EMA), and saves the results to a CSV file. 
The project is designed to be robust and handles various contingencies related to election polls.

# File Descriptions:

* web_scraper.py: Contains the scrape_poll_data function which scrapes poll data from a specified webpage and saves the data to polls.csv.

* data_processing.py: Contains the process_poll_data function, which processes the scraped data from polls.csv. Currently, this function loads the data and returns it, but it's designed for any future preprocessing steps.

* ema_calculator.py: Contains the calculate_ema function which reads data from polls.csv, computes the 7-day Exponential Moving Average (EMA) for each candidate, and saves the results to trends.csv.

* logger.py: Contains the log_error function which logs error messages to error_log.txt.

* main_script.py: The primary script that orchestrates the web scraping, data processing, and EMA calculation. It also includes error handling.

# How to Run:
Ensure you have Python 3.9 and the required libraries installed. You can install the necessary libraries using:

pip install -r requirements.txt

Navigate to the project directory and run the main_script.py:

python main_script.py

After running the script, you should see two output files in the same directory: polls.csv (scraped data) and trends.csv (7-day EMA data).


