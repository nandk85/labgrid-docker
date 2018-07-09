FROM ubuntu:16.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common vim

RUN apt-get install -y build-essential python3 python3-dev python3-pip python3-venv
RUN apt-get install -y git

# update pip
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel

# Install tools required to build the project
RUN python3 -m pip install filemagic

# Copy all project and build it
# This layer is rebuilt when ever a file has changed in the project directory
COPY . /opt/labgrid/

RUN cd /opt/labgrid && python3 -m pip install -r requirements.txt --no-index

RUN cd /opt/labgrid && python3 setup.py install

CMD "/bin/bash"
