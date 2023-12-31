# Election Poll Tracker
This project scrapes election poll data, processes the data, calculates the 7-day Exponential Moving Average (EMA), and saves the results to a CSV file. 
The project is designed to be robust and handles various contingencies related to election polls.

# File Descriptions:

* web_scraper.py: Contains the scrape_poll_data function which scrapes poll data from the specified webpage and saves the data to polls.csv.

* data_processing.py: Contains the process_poll_data function, which processes the scraped data from polls.csv. Currently, this function loads the data and returns it, but it's designed for any future preprocessing steps.

* ema_calculator.py: Contains the ema_calculator function which reads data from polls.csv, computes the 7-day Exponential Moving Average (EMA) for each candidate, and saves the results to trends.csv.

* logger.py: Contains the log_error function which logs error messages to error_log.txt.

* main_script.py: The primary script that orchestrates the web scraping, data processing, and EMA calculation. It also includes error handling.
  
* example_results: The example result folder contains my version of the results I got from running my script. 

# How to Run:
Ensure you have Python 3.9 and the required libraries installed. You can install the necessary libraries using:

`pip install -r requirements.txt`

Navigate to the project directory and run the main_script.py:

`python main_script.py`

After running the script, you should see two output files in the same directory: polls.csv (scraped data) and trends.csv (7-day EMA data).


# Docker Instructions:
If you prefer to run the project in a Docker container:

Build the Docker image using:

`docker build -t poll_tracker .`

Run the Docker container:

`docker run poll_tracker`

# Contextual Relevance of Exponential Moving Average (EMA):

This is just a basic implementation since a sophisticated one isnt required for this assignment. 

In the run-up to an election, various events can influence voter sentiment — from debates and policy announcements to unexpected news or controversies. Using EMA ensures that our poll tracker remains sensitive to these changes, providing stakeholders with a timely and relevant understanding of the evolving electoral landscape.

# Visualizing my result:

![7-Day Exponential Moving Average of Election Polls (Interpolated)](viz.png)








