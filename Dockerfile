# Using the Python 3.9 image as the base image
FROM python:3.9

# Setting the working directory in the container
WORKDIR /app

# Copy only the files I specify here. 
COPY ema_calculator.py /app/
COPY data_processing.py /app/
COPY web_scraper.py /app/
COPY main_script.py /app/
COPY logger.py /app/
COPY error_log.txt /app/
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run on container start
ENTRYPOINT ["python", "main_script.py"]
