.PHONY: setup run clean

# Target to install dependencies without using a virtual environment
setup:
	@echo "Installing dependencies..."
	python3 -m pip install --user --upgrade pip
	python3 -m pip install --user -r requirements.txt
	@echo "Dependencies installed."

# Target to run the Python script directly
run: setup
	@echo "Running the script..."
	python3 calculate_matrix.py

# Clean temporary files (e.g., __pycache__)
clean:
	@echo "Cleaning up temporary files..."
	rm -rf __pycache__
	rm -rf *.pyc
	@echo "Cleanup completed."
