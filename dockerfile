FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .


ENV ELASTICSEARCH_HOSTS=http://es-container:9200

# command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]