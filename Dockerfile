FROM alpine:latest

RUN apk add --no-cache coreutils git python3 py3-requests

COPY retrieve_contributors.py /retrieve_contributors.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
