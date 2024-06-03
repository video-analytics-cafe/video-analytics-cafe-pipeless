FROM python:3.9-slim AS build

# Set the working directory in the container
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY ./app.py ./app.py

# Define environment variable
ENV NAME SL_DB

# Run streamlit
CMD python -m streamlit run app.py