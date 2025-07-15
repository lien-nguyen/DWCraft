#!/bin/bash
set -e

echo "Pruning unused Docker data and clearing logs..."

# Docker cleanup
docker system prune -af
docker image prune -af

# Remove old log files (older than 7 days) from /srv/build2teach/logs
find /srv/build2teach/logs -type f -name "*.log" -mtime +7 -delete

echo "Docker and log file cleanup completed."
