FROM python:3

# Install tools required to build the project
RUN apt-get update
RUN apt-get install --assume-yes vim
RUN pip3 install PyYAML filemagic

# Copy all project and build it
# This layer is rebuilt when ever a file has changed in the project directory
COPY . /opt/labgrid/

RUN cd /opt/labgrid && python3 setup.py install

CMD "/bin/bash"
