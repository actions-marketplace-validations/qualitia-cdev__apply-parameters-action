# Container image that runs your code
FROM alpine:latest

RUN apk add --no-cache bash python3

COPY conv-cfn/ /tmp/conv-cfn/
RUN ls && cd /tmp/conv-cfn && python3 setup.py install

COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
