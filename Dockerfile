# VS Code Python Development Container
FROM python:3.10-slim-buster

# Flask server port
EXPOSE 5000

# Jupyter Lab server port
EXPOSE 8888

# SQLite3 server port 
# EXPOSE NNNN

# Default working directory
WORKDIR /workspaces/100daysofcode/days

# Install Git, core packages for GCC, Python 3 development and SQLite3
RUN apt-get update && \
    apt-get install -y git \
                       gcc \
                       python3-dev \
                       sqlitebrowser

# Install X Virtual Frame Buffer (Xvfb) and xclip to support Pyperclip
RUN apt-get install -y xvfb xclip

# Copy Python pip requirements file
COPY requirements.txt requirements.txt

# Install Python packages from PyPI
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/workspaces/100daysofcode/days

# Start a bash shell
CMD ["/bin/bash"]
