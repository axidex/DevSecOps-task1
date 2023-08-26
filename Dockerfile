# Don't forget about "$ xhost +" before running container
FROM debian
 
ENV TZ=Europe/Moscow
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing linux libs
RUN apt-get update && apt-get install -y \
   git \
   wget

#Installing GO
RUN apt-get install -y \
   golang

ENV PATH=/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# Installing Python
RUN apt-get install -y \
   python3 \
   python3-pip \
   python3-requests

# Installing Python Libs
#RUN pip install requests

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