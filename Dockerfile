# Container image that runs your code
FROM cdevqualitia/awscli:latest

COPY conv-cfn/ /tmp/conv-cfn/
RUN ls && cd /tmp/conv-cfn && python3 setup.py install

COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
