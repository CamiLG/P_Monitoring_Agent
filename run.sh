#!/bin/bash

echo "Building Docker image with no caché..."
if ! docker-compose build --no-cache; then
    echo "Error: Could not build the Docker image"
    exit 1
fi

echo "Starting Docker Compose..."
if ! docker-compose up; then
    echo "Error: Could not start Docker Compose"
    exit 1
fi