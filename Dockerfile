FROM google/cloud-sdk:latest

COPY docker_entrypoint.sh docker_entrypoint.sh
COPY start_emulator.sh start_emulator.sh
COPY setup_pub_sub.py setup_pub_sub.py
COPY requirements.txt requirements.txt

EXPOSE 8085
RUN export CLOUDSDK_CORE_DISABLE_PROMPTS=1
RUN ["chmod", "+x", "./docker_entrypoint.sh" ]
RUN ["chmod", "+x", "./start_emulator.sh" ]
RUN apt-get -y update && apt-get -y upgrade &&  apt-get -y dist-upgrade &&  apt-get -y autoremove
RUN apt-get -y install python3 python3-pip
RUN pip install -r requirements.txt

CMD ./docker_entrypoint.sh