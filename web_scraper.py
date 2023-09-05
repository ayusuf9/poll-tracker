 # Importing the requests module, which lets me make web requests (like accessing the assignment webpage)
import requests
# Importing the beautifulSoup class from bs4, which lets me extract data from HTML and XML files.
from bs4 import BeautifulSoup
#Importing the csv module so I can work with CSV files.
import csv
#  Importing the datetime module to work with dates and times. 
import datetime


# Modularizing the whole web scrapping process..
def scrape_poll_data():
    # Storing the URL of the assignment webpage so I can access it in the variable named url.
    url = 'https://cdn-dev.economistdatateam.com/jobs/pds/code-test/index.html'
    # This fetches the content of the webpage defined in url and stores the result in the response variable.
    response = requests.get(url)
    # this converts the content of the webpage as "html"
    soup = BeautifulSoup(response.text, 'html.parser')

#This opens or creates if it doesn't exist a file named 'polls.csv' in write mode ('w')
    with open('polls.csv', 'w') as f:
        # Creating a CSV writer object that can write data to the file created.
        writer = csv.writer(f)
        # The below writes the header row to the CSV file created in the previous step..
        writer.writerow(['Date', 'Pollster', 'Sample', 'Bulstrode', 'Lydgate', 'Vincy', 'Casaubon', 'Chettam', 'Others'])

        #Looping  over each table rows..
        for row in soup.select('table tr'):
            # For each table row, this selects the individual table data..
            cells = row.select('td')

           # This new function (to_percentage) takes a single argument then  converts a given text into a percentage value (in float) 
            def to_percentage(text):
                # This line uses the strip function to remove any percentage sign (%) from the start and end of the input text.
                cleaned_text = text.strip('%').strip()
                # This checks if the "cleaned_text" is either empty or if it equals the string '**'.
                if not cleaned_text or cleaned_text == '**':
                    return '' # If the condition in the previous step is True, the function returns a empty space string..
                # If the condition is False, the cleaned_text is converted to a float 
                return float(cleaned_text) / 100

            # This checks if each row in the table has exactly 9 cells, this is a safety check to ensure only valid rows are processed. 
            if len(cells) == 9:
                 # pre-processing the date values using the datetime function
                date = datetime.datetime.strptime(cells[0].text.strip(), '%m/%d/%y').date()
                # accounting for the pollsters name. 
                pollster = cells[1].text.strip()
                # converting the scraped value of samples into an integer so as to be able to perform operations.. 
                sample = int(cells[2].text.replace(',', '').replace('*', '').strip())

                # The below leverages the to_percentage function above to process the columns with percentage signs... 
                bulstrode = to_percentage(cells[3].text)
                lydgate = to_percentage(cells[4].text)
                vincy = to_percentage(cells[5].text)
                casaubon = to_percentage(cells[6].text)
                chettam = to_percentage(cells[7].text)
                others = to_percentage(cells[8].text)
                # writing the processed data to the respective rows.. 
                writer.writerow([date, pollster, sample, bulstrode, lydgate, vincy, casaubon, chettam, others])


