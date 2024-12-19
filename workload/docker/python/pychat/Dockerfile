FROM python:3.9.20

# update the package lists
RUN apt-get update -y && apt-get install -y --no-install-recommends netcat-openbsd net-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/*



WORKDIR /

# COPY ./scripts/start.sh /start
COPY ./workload/docker/python/pychat/src/start.py /start

COPY ./sdk/python/dist/spear*.whl /tmp/
RUN pip install /tmp/spear*.whl
RUN rm /tmp/spear*.whl

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl --fail http://localhost:8080/ || exit 1

RUN useradd -ms /bin/bash myuser

USER myuser

CMD ["sleep", "infinity"]
