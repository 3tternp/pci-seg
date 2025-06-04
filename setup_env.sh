#!/bin/bash

# Step 1: Install python3-venv if not already installed
echo "[*] Installing python3-venv if missing..."
sudo apt update
sudo apt install -y python3-venv

# Step 2: Create virtual environment
echo "[*] Creating virtual environment in ./venv"
python3 -m venv venv

# Step 3: Activate virtual environment
echo "[*] Activating virtual environment and installing requirements"
source venv/bin/activate
