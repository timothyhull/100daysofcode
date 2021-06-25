# VS Code Python Development Container
FROM python:3.9-slim-buster

EXPOSE 8888

WORKDIR /workspaces

RUN apt-get update && \
    apt-get install -y git

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

ENV PYTHONPATH=/workspaces/100daysofcode/days

CMD ["/bin/sh"]
