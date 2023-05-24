# Docker cointainer

The purpose of this practice is to create a simple app

Change directory to app directory 

    $ cd app

Build the container image

    $ docker build -t mypython-docker .

View local images

    $ docker images

Test

    $  docker run -dp 8000:8000 mypython-docker

Open a new browser and navigate to http://localhost:8000/
