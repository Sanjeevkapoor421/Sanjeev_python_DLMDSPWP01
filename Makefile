# Makefile

.PHONY: install run all

# Install dependencies  and requirements.txt
install:
	python3.12 -m venv myenv
	bash -c "source myenv/bin/activate && pip install -r requirements.txt"
	
# Run Python script
run:
	python3 src_sanjeev/main.py

# Combined target: install + run
all: install run

