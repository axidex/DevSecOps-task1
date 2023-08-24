# Don't forget about "$ xhost +" before running container
FROM ubuntu:latest
 
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing linux libs
RUN apt-get update && apt-get install -y \
   git \
   golang \
   wget
RUN apt-get install docker.io -y


# Installing cdx
RUN mkdir cdx
WORKDIR /cdx
RUN wget https://github.com/CycloneDX/cyclonedx-gomod/releases/download/v1.4.1/cyclonedx-gomod_1.4.1_linux_amd64.tar.gz 
RUN tar -xvzf cyclonedx-gomod_1.4.1_linux_amd64.tar.gz
WORKDIR /

# Copying some data
COPY . /app
WORKDIR /app

RUN cp ../cdx/cyclonedx-gomod ./

# Building and running