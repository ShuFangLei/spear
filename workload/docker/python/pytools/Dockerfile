FROM python:3.12-slim-bookworm

# update the package lists
RUN apt-get update -y
RUN apt-get install -y netcat-openbsd net-tools

WORKDIR /

# COPY ./scripts/start.sh /start
COPY ./workload/docker/python/pytools/src/start.py /start

COPY ./sdk/python/dist/spear*.whl /tmp/
RUN pip install --no-cache-dir /tmp/spear*.whl
RUN rm /tmp/spear*.whl

CMD ["sleep", "infinity"]
