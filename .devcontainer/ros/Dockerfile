FROM osrf/ros:noetic-desktop-full

# Install sudo
RUN apt-get update &&\
    apt-get install -y sudo openssh-client && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user called "developer" with sudo privileges
RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers 

RUN mkdir -p /home/developer/.ssh


RUN apt-get update && \
    apt-get install -y git 

#     ros-humble-joint-state-publisher-gui \ 
#     ros-humble-xacro \ 
#     ros-humble-ros-gz \
#     ros-humble-ros-control \
#     ros-humble-ros-controllers \
#     ros-humble-moveit 

USER developer

# RUN pip install pyserial
# install tmate
# apt-get install openscad meshlab
# pip install onshape-to-robot

# export ONSHAPE_API=https://cad.onshape.com
# export ONSHAPE_ACCESS_KEY=Your_Access_Key
# export ONSHAPE_SECRET_KEY=Your_Secret_Key


