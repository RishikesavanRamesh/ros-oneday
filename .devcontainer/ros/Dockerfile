FROM osrf/ros:noetic-desktop-full

# Install sudo
RUN apt-get update &&\
    apt-get install -y sudo openssh-client && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user called "developer" with sudo privileges
RUN useradd -m -s /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers 

RUN mkdir -p /home/developer/.ssh

RUN echo "#!/bin/bash" >> /post-create-script.sh && \
    echo "sudo chown -R developer:developer /home/developer" >> /post-create-script.sh && \
    echo "rosdep update && sudo rosdep install --from-paths src --ignore-src -y"  >> /post-create-script.sh && \
    echo "echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc" >> /post-create-script.sh && \
    echo "source /opt/ros/noetic/setup.bash" >> /post-create-script.sh && \
    echo "echo ' [ -f '/home/developer/my_ros_ws/devel/setup.bash' ] && source '/home/developer/my_ros_ws/devel/setup.bash' ' >> ~/.bashrc" >> /post-create-script.sh && \
    echo "[ -f '/home/developer/my_ros_ws/devel/setup.bash' ] && source '/home/developer/my_ros_ws/devel/setup.bash'" >> /post-create-script.sh && \
    echo "echo -e \"\$SSH_KEY\" > /home/developer/.ssh/id_rsa && chmod 600 /home/developer/.ssh/id_rsa" >> /post-create-script.sh

RUN chmod +x /post-create-script.sh

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


