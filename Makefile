PROGRAM1=main
OPEN=10
CLOSE=18

default: $(PROGRAM1).py
	python3 $(PROGRAM1).py $(OPEN) $(CLOSE)

test: $(PROGRAM1).py 
	python3 -m pytest
