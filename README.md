# first-devops

Downloading and running Jenkins in Docker
[Jenkins in Docker](https://www.jenkins.io/doc/book/installing/docker/)

<img src="https://jenkins.io/sites/default/files/jenkins_logo.png"/>

# Usage

## On macOS and Linux

1.Open up a terminal window.
2.Create a bridge network in Docker using the following docker network create command:

```
docker network create jenkins
```
3. In order to execute Docker commands inside Jenkins nodes, download and run the docker:dind Docker image using the following docker run command:

```
docker run --name jenkins-docker --rm --detach --privileged --network jenkins --network-alias docker --env DOCKER_TLS_CERTDIR=/certs --volume jenkins-docker-certs:/certs/client --volume jenkins data:/var/jenkins_home --publish 2376:2376 docker:dind --storage-driver overlay2
  
```

This will automatically create a 'jenkins_home' [docker volume](https://docs.docker.com/storage/volumes/) on the host machine.
Docker volumes retain their content even when the container is stopped, started, or deleted.

NOTE: Avoid using a [bind mount](https://docs.docker.com/storage/bind-mounts/) from a folder on the host machine into `/var/jenkins_home`, as this might result in file permission issues (the user used inside the container might not have rights to the folder on the host machine).
If you _really_ need to bind mount jenkins_home, ensure that the directory on the host is accessible by the jenkins user inside the container (jenkins user - uid 1000) or use `-u some_other_user` parameter with `docker run`.

```
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk11
```

This will run Jenkins in detached mode with port forwarding and volume added. You can access logs with command 'docker logs CONTAINER_ID' in order to check first login token. ID of container will be returned from output of command above.
