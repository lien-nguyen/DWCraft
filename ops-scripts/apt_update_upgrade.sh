#!/bin/bash
set -e

echo "Starting system update..."
sudo apt update && sudo apt upgrade -y
echo "System update completed."
