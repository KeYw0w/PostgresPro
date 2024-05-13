# Указываем базовый образ
FROM ubuntu

RUN apt update &&  apt-get install -y openssh-server sudo
RUN mkdir /var/run/sshd


RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo PubkeyAuthentication yes >> /etc/ssh/sshd_config
RUN echo "{PUBLIC_SSH_KEY}" > /root/.ssh/authorized_keys

EXPOSE 22
EXPOSE 5432

# Запускаем SSH сервер при старте контейнера
CMD ["/usr/sbin/sshd", "-D"]
