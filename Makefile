# Define variables
ENV_DIR = venv
PYTHON = $(ENV_DIR)/bin/python
PIP = $(ENV_DIR)/bin/pip

# Default target
all: setup

# Create a virtual environment and install dependencies
setup:
	python3 -m venv $(ENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the script
run: setup
	$(PYTHON) calculate_matrix.py

# Clean up environment
clean:
	rm -rf $(ENV_DIR)
