FROM aaii/cuda:9.2-cudnn7-devel-ubuntu18.04
#FROM nvidia/cuda:11.2.2-devel-ubuntu20.04
#FROM nvidia/cuda:12.2.0-devel-ubuntu22.04


ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Python Version x.y
ARG PYTHON_VERSION=3.7

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        wget \
        cmake \
        ninja-build \
        build-essential \
		checkinstall \
		software-properties-common \
		dpkg \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 
	

RUN add-apt-repository ppa:deadsnakes/ppa
	

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
		python2.7 \
        "python$PYTHON_VERSION-dev" \
		"python$PYTHON_VERSION-distutils" \
		python3-setuptools \
        python3-pip \
        "python$PYTHON_VERSION-venv" \
		libstdc++6 \
		gcc-multilib\
		libc6 \
		 && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

RUN ls /usr/bin | grep "python"
RUN python3 -m pip install --user virtualenv
RUN python3 -m virtualenv --help




#RUN python3.6 -m pip install --upgrade Pillow

RUN ln -sf $(which python$PYTHON_VERSION) /usr/bin/python

RUN python -m pip install --upgrade pip \
    && python -m venv --system-site-packages /opt/python/venv/base
	
COPY requirements.txt /opt/python/venv/base/

RUN python2.7 --version

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python2.7 get-pip.py

RUN python2.7 -m pip install -U virtualenv

RUN python2.7 -m virtualenv --system-site-packages temp-python

RUN /opt/python/venv/base/bin/python -m pip install MarkupSafe==2.0.0
	
RUN /opt/python/venv/base/bin/python -m pip install -r /opt/python/venv/base/requirements.txt




COPY TL-CodeSum-master .


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set entrypoint to bash
ENTRYPOINT ["/entrypoint.sh"]