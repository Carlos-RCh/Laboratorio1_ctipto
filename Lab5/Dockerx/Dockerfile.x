FROM ubuntu:20.10

COPY sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libssl-dev \
    wget

COPY ./openssh-8.3p1.tar.gz .
RUN tar zxvf openssh-8.3p1.tar.gz

RUN sed -i '3s/8.3/?.?/' ./openssh-8.3p1/version.h
WORKDIR /openssh-8.3p1

RUN ./configure && \
    make && \
    make install

CMD ["tail", "-f", "/dev/null"]



