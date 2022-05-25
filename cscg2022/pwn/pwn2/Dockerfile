FROM ubuntu@sha256:a02c32cf0c2a7e8743c74deef66637aa70e063c9bd40e9e1f8c0b3ea0750b0ba

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y xinetd

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY pwn2 .
COPY flag /flag
COPY pwn2_svc /etc/xinetd.d/

RUN chmod +x pwn2

EXPOSE 1024

CMD xinetd -dontfork