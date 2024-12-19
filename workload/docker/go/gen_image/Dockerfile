FROM ubuntu:24.04

WORKDIR /

# COPY ./scripts/start.sh /start
COPY ./bin/start /start


HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl --fail http://localhost:8080/ || exit 1

RUN useradd -ms /bin/bash myuser

USER myuser

CMD ["sleep", "infinity"]
