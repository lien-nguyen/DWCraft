FROM python:3.14-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /build2teach

# Install system dependencies
RUN apt-get update && apt-get install -y && apt-get -y install gcc && apt-get clean 

# Install Python dependencies
COPY build2teach/requirements.txt /build2teach//
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /build2teach//
