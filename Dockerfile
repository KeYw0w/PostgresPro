# Указываем базовый образ
FROM ubuntu

RUN apt update &&  apt-get install -y openssh-server sudo
RUN mkdir /var/run/sshd


RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo PubkeyAuthentication yes >> /etc/ssh/sshd_config
RUN touch id_rsa
RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDTEXtD/+4SVzM+i5tPIXGbM8c9GX2eOiCS5toKTslTNsa++l0WT/yrrzMylAnsu6VMrzW0A1If+E3dBfBBFYFmeLgb++B1p7FCwUBhV2EiwuE1DF567H2MjgbzHreyS7BChVR4IT4QDnN0LAuQcXfxIP7xZ6iE8/ytM5LdVSmQw8mN+MshPgs3xur8AJALumyl1+1VeqlZmGAqCOH6s3B72qKvNZrIZRnVqWKXjet1qb9dqodMYeCHPOEXXTAegevrynfDCCnICwBwV1sMSA0KwZu7Wf6uCW3KL7UIPuUWowjJWNOeS9mQqxQhhdCUH5deP/2ebi0Fau3zn+C2aziTMh+SQpGr3t+WsYSYQ4vKe9aTO7NCuMgolLv7HIsjcezUJoVk+V27PpznWyyctRXkEvNwtgTtf5A2dSHZwdhwS0c9smz5jItF6TjiEvpcS00vEtjomrQmpqDof9dWTX2zjZvGA9k/cFGB+JDrjCrX6FSM94pgKaGwIKnSCSt7uvM= antonsemenov@Noutbuk-Anton.local" > /root/.ssh/authorized_keys

EXPOSE 22
EXPOSE 5432

# Запускаем SSH сервер при старте контейнера
CMD ["/usr/sbin/sshd", "-D"]
