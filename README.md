# Weather API

Globant technical test for Python developer vacancy.

The present Django service receives a specific GET request in the endpoint "/weather/city/\<city name>/country/\<country code>", and returns a human readable json response, that could be easily used by any frontend application.

Process:
- The service receives the data in the url.
- The service calls an external API to reach the weather information.
- Then the data returned by the external API is formatted to make it easier to read.
- Returns the formatted data to the client.
- If the information is not received for any reason the services raises a custom exception.

The service saves a cache for each different request to the endpoint, and each cache saved lasts 2 minutes. This allows the service to answer the repeated requests faster that normal.

NOTE: The developer could not make the application work on docker with environment variables at the moment. If you want to use the environment variables, you should modify some lines of the code and run the application locally on your PC.

## Installation and Running

Locally you need to install the next tools:
- Python 3.8
- pip
- pipenv

### Local Installation and Running
If you already have Python installed, you should have pip installed too. So you
should install pipenv as follows:
~~~
pip install pipenv
~~~

After that, you should run the following command, to install the required packages listed in the file called "Pipfile":
~~~
pipenv install
~~~

Everything is ready, now you can run the server with the next command:
~~~
pipenv run python manage.py runserver 8080
~~~

### Docker Installation and Running
You need to install docker on your machine, and after that, you can follow the next steps:

- Go to the main directory of the service, where the Dockerfile is.
- execute the following command:
~~~
docker build -t globant_test .
~~~
- now that you have an image created with the service you can create a container as follows:
~~~
docker run -p 8080:8080 -d globant_test
~~~

and that's it! you have the assignment service running inside a Docker container.

### How to run the automatic tests
To run the automatic tests follow this 2 steps:
- Go to the main directory of the project
- open a console and execute the following command:
~~~
pipenv run python manage.py test
~~~

### How to use/test the service

Test the service making the GET HTTP request to the *localhost:8080* following the available endpoint:

Weather endpoint:
- weather/city/\<city name>/country/\<country code>

for example:
~~~
http://localhost:8080/weather/city/medellin/country/co
~~~

The above url should return in JSON format the information of the weather in medellin at that moment.

### Note:

When you finish using the tool, you should to stop the container as follows:
- check the container list running on your pc:
~~~
docker ps
~~~
- look for the container called 'globant_test', identify the container id, and execute the following command:
~~~
docker stop containerID
~~~

### Note 2:

The interviewer challenged the developer in the call with a little exercise, this exercise is in the file called "interview_challenge".
