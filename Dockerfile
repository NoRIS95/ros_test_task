FROM ros:noetic

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    python3-rospy \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends --quiet \
        software-properties-common \
    && apt-get install --assume-yes --no-install-recommends --quiet \
    python3 \
    python3-pip \
    && apt-get clean all


WORKDIR /app
COPY . /app
RUN pip3 install -r ./src/requirements.txt

EXPOSE 8001
ENTRYPOINT ./src/runme.sh