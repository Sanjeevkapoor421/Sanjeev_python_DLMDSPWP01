# Makefile

.PHONY: install run all

# Install dependencies  and requirements.txt
install:
	python3 -m venv myenv
	source myenv/bin/activate 
	pip install -r requirements.txt

# Run Python script
run:
	python src_sanjeev/main.py

# Combined target: install + run
all: install run

