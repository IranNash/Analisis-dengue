install:
	pip install --upgrade pip &&\
		pip install -r requierements.txt

format:
	black *.py

lint:
	pylint --disable=R,C Analisis_descriptivo.py

test:  
	pytest -vv --cov=Analisis_descriptivo test_Analisis_descriptivo.py
	
all: install lint test
