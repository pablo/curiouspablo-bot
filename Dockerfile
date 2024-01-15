FROM python:3.11-bullseye AS base

# Maintainer
LABEL maintainer="Pablo Santa Cruz <pablo@roshka.com.py>"

WORKDIR /bot

# Install requirements
COPY requirements.txt /bot
RUN pip -q install --upgrade pip
RUN pip -q install -r /bot/requirements.txt

# Copy application
COPY . .

# run telegram bot
CMD ["python", "bot.py"]

