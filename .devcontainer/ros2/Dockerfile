FROM ros:humble

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
    echo "echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc" >> /post-create-script.sh && \
    echo "source /opt/ros/humble/setup.bash" >> /post-create-script.sh && \
    echo "echo 'source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash' >> ~/.bashrc" >> /post-create-script.sh && \
    echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> /post-create-script.sh && \
    echo "echo -e \"\$SSH_KEY\" > /home/developer/.ssh/id_rsa && chmod 600 /home/developer/.ssh/id_rsa" >> /post-create-script.sh

RUN chmod +x /post-create-script.sh

RUN apt-get update && \
    apt-get install -y tmate \
    ros-humble-joint-state-publisher-gui \ 
    ros-humble-xacro \ 
    ros-humble-ros-gz \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-moveit 

USER developer

# RUN pip install pyserial
# install tmate
# apt-get install openscad meshlab
# pip install onshape-to-robot

# export ONSHAPE_API=https://cad.onshape.com
# export ONSHAPE_ACCESS_KEY=Your_Access_Key
# export ONSHAPE_SECRET_KEY=Your_Secret_Key


