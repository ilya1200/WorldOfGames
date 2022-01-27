# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN apt-get update && apt-get install -y procps less wget curl net-tools
RUN apt-get install -y curl unzip wget xvfb

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Install Chrome browser
RUN apt install libgbm1 -y && \
    CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container as /app
COPY . /app

# Install requirements
RUN pip install -r requirements.txt
RUN pip3 install pyvirtualdisplay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

# Make port 5001 available to services on the same docker network
EXPOSE 5001

ENV FLASK_APP=MainScores.py

# Run app.py when the container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]