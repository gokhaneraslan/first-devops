# first-devops

Downloading and running Jenkins in Docker
[Jenkins in Docker](https://www.jenkins.io/doc/book/installing/docker/)

<img src="https://jenkins.io/sites/default/files/jenkins_logo.png"/>

# Usage

## On macOS and Linux

1. Open up a terminal window.

2. Create a bridge network in Docker using the following docker network create command:

```
docker network create jenkins
```
3. In order to execute Docker commands inside Jenkins nodes, download and run the docker:dind Docker image using the following docker run command:

```
docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2
  
```
4. Customise official Jenkins Docker image, by executing below two steps.

a. Create Dockerfile with the following content:
  
```
FROM jenkins/jenkins:2.375.2
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

```
b. Build a new docker image from this Dockerfile and assign the image a meaningful name, e.g. "myjenkins-blueocean:2.375.2-1":

```
docker build -t myjenkins-blueocean:2.375.2-1 .

```
5. Run your own myjenkins-blueocean:2.375.2-1 image as a container in Docker using the following docker run command:

```
docker run --name jenkins-blueocean --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --publish 8080:8080 --publish 50000:50000 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro myjenkins-blueocean:2.375.2-1

```
## On Windows

1. Open up a terminal window.

2. Create a bridge network in Docker.

```
docker network create jenkins
```
3. Run a docker:dind Docker image.

```
docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins-data:/var/jenkins_home --publish 2376:2376 docker:dind
  
```
4. Customise official Jenkins Docker image, by executing below two steps.

a. Create Dockerfile with the following content:
  
```
FROM jenkins/jenkins:2.375.2
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

```
b. Build a new docker image from this Dockerfile and assign the image a meaningful name, e.g. "myjenkins-blueocean:2.375.2-1":

```
docker build -t myjenkins-blueocean:2.375.2-1 .

```
5. Run your own myjenkins-blueocean:2.375.2-1 image as a container in Docker using the following docker run command:

```
docker run --name jenkins-blueocean --rm --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.375.2-1

```
## Accessing the Docker container

```
docker exec -it myjenkins-blueocean:2.375.2-1 bash
```

## Accessing the Docker logs

```
docker logs myjenkins-blueocean:2.375.2-1
```

## Unlocking Jenkins

When you first access a new Jenkins instance, you are asked to unlock it using an automatically-generated password.

1. Browse to http://localhost:8080 (or whichever port you configured for Jenkins when installing it) and wait until the Unlock Jenkins page appears.

<img src="https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-01-unlock-jenkins-page.jpg"/>

2. From the Jenkins console log output, copy the automatically-generated alphanumeric password (between the 2 sets of asterisks).

<img src="https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-02-copying-initial-admin-password.png"/>
