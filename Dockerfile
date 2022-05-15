# VS Code Python Development Container
FROM python:3.10-slim-buster

# Jupyter Lab server port
EXPOSE 8888

# Default working directory
WORKDIR /workspaces/100daysofcode/days

# Install core packages for GCC, Python 3 development
RUN apt-get update && \
    apt-get install -y git gcc python3-dev

# Install X Virtual Frame Buffer (Xvfb) and xclip to support Pyperclip
RUN apt-get install -y xvfb xclip && \
    Xvfb :99 -screen 0 1280x720x16 & export DISPLAY=:99

# Copy Python pip requirements file
COPY requirements.txt requirements.txt

# Install Python packages from PyPI
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/workspaces/100daysofcode/days

# Start a bash shell
CMD ["/bin/bash"]
