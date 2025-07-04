# run.ps1

Write-Host "Building Docker image with no cache..."
try {
    docker compose build --no-cache
    if($LASTEXITCODE -ne 0) {
        Write-Host "Error: Could not build the Docker image"
        exit 1
    }   
} catch {
    Write-Error "Exception occurred while building Docker image: $_"
    exit 1
}

Write-Host "Starting Docker Compose..."
try {
    docker compose up
    if($LASTEXITCODE -ne 0) {
        Write-Host "Error: Could not start Docker Compose"
        exit 1
    }
} catch {
    Write-Error "Exception occurred while starting Docker Compose: $_"
    exit 1
} 