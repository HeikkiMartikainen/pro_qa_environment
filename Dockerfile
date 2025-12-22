# Use Microsoft's official Playwright image which includes Python, Node, and browsers
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

# Set up a non-root user for security
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID
# RUN groupadd --gid $USER_GID $USERNAME && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
# USER $USERNAME

# # Install Appium and its dependencies
# # We switch back to root temporarily to install system-level packages
# USER root
# RUN apt-get update && apt-get install -y nodejs npm
# RUN npm install -g appium
# USER $USERNAME

# Copy your project requirements file into the container
COPY requirements.txt .

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt