# Docker cointainer

The purpose of this practice is to create a simple Docker container and share it to a public repository.

## Prerequisites
* Git installed
* Docker Installed


## Create container app
1.- Clone git repository executing below command:

    $ git clone https://github.com/EfrenDRF/udgS4ComPar.git

2.- Change working directory to app directory 

    $ cd udgS4ComPar/01_PyhtonContainer/app

3.- Build the container image:

    $ docker build -t mypython-docker .

4.- Execute below docker command in order to display a list of local images, you should see `mypython-docker` including to the list.

    $ docker images

5.- Start docker container:

    $  docker run -dp 8000:8000 mypython-docker

6.- Open a new browser and navigate to http://localhost:8000/

## Share container app

7.- Create a repo into [Docker Hub](https://hub.docker.com/) called `mypython-docker`

8.- Login to Docker Hub in command line:

    $ docker login -u efrendrf

9.- Rename `mypython-docker` created image:

    $ docker tag mypython-docker efrendrf/mypython-docker

10.- Clone latest image to your local machine:

    $ docker pull efrendrf/mypython-docker:latest
## References
 * https://docs.docker.com/get-started/
