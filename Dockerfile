FROM kalilinux/kali-rolling

RUN apt update -y 
RUN apt-get update -y
RUN apt-get install -y netcat-traditional
RUN apt-get install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools
RUN gcc --version