FROM ubuntu:24.04

# update the package lists
RUN apt-get update -y && apt-get install -y --no-install-recommends netcat-openbsd net-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /

# COPY ./scripts/start.sh /start
COPY ./bin/start /start

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl --fail http://localhost:8080/ || exit 1


RUN useradd -ms /bin/bash myuser

USER myuser

CMD ["sleep", "infinity"]
