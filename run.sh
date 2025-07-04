#!/bin/bash

echo "Construyendo la imagen Docker sin caché..."
if ! docker compose build --no-cache; then
    echo "Error: No se pudo construir la imagen"
    exit 1
fi

echo "Iniciando los servicios con Docker Compose..."
if ! docker compose up; then
    echo "Error: No se pudieron iniciar los servicios"
    exit 1
fi