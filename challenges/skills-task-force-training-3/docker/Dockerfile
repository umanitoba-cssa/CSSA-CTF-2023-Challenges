FROM python:3.9-bookworm

RUN apt-get update && apt-get install -y lib32z1 xinetd rsync

RUN useradd -m ctf

WORKDIR /home/ctf

RUN rsync -K -a /lib* /home/ctf
RUN rsync -K -a /usr/lib* /home/ctf
RUN cp -R /usr/local/lib/* /home/ctf/lib

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp /bin/py* /home/ctf/bin && \
    cp /usr/local/bin/py* /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./bin/ /home/ctf/
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag.txt

CMD ["/start.sh"]

EXPOSE 9999
