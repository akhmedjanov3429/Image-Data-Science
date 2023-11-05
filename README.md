# Sardor Akhmedjonov
# CS207 Programming Assignment #1
# November 1, 2023
# Compiled on Apple(Macbook Pro 2021) with standard Python interpreter and Jupyter
# Before running, ensure the required Python packages are installed:
# Install notebook matplotlib numpy using pip, or follow the instructions in the readme file.
# All images are already in the folders, and their directories are hardcoded to be uploaded to specific folders in the "output_images" dir. 
# All images are in.png format, as it was difficult to generate in.raw format in Python. I suggest running this README file with "make -f README"
# Generate and check if the code is working. You will notice that the images are generated in the precise locations for the output folders.
# Run this file with "make -f README"

PYTHON=python
JUPYTER=jupyter nbconvert --execute --to notebook --inplace

all: env_setup problem1 problem2 problem3 test_problem1 test_problem2 test_problem3

# Setup the environment by installing required Python packages
env_setup:
	@echo "Setting up the environment"
	@$(PYTHON) -m pip install notebook matplotlib numpy

# Problem1/2/3.ipynb are designed to solve problems with their subproblems from the homework1
# Problem 1
prob1:
	@echo "Running Problem 1 Notebook" # Notebook generates results for all testing images of problem 1
	@$(JUPYTER) Problem1.ipynb
	@echo "Notebook Problem1.ipynb has been run. Check the 'output_images' directory for output images."

# Problem 2
prob2:
	@echo "Running Problem 2 Notebook" # Notebook generates results for all testing images of problem 2
	@$(JUPYTER) Problem2.ipynb
	@echo "Notebook Problem2.ipynb has been run. Check the 'output_images' directory for output images."

# Problem 3
prob3:
	@echo "Running Problem 3 Notebook" # Notebook generates results for all testing images of problem 3
	@$(JUPYTER) Problem3.ipynb
	@echo "Notebook Problem3.ipynb has been run. Check the 'output_images' directory for output images."

# Inputs for AI generated images can be found in 'AI_images_input' directory with corresponding Problem folders
# Problem 1/2/3_testing_ai.ipynb codes are designed to test with AI images in "AI_images_input" dir.
# Test Problem 1
test_prob1:
	@echo "Running Problem 1 Testing Notebook" # Notebook generates results for all AI generated testing images of problem 1
	@$(JUPYTER) Problem1_testing_ai.ipynb
	@echo "Testing Notebook Problem1_testing_ai.ipynb has been run. Check the 'AI_images_output' directory for output images."

# Test Problem 2
test_prob2:
	@echo "Running Problem 2 Testing Notebook" # Notebook generates results for all AI generated testing images of problem 2
	@$(JUPYTER) Problem2_testing_ai.ipynb
	@echo "Testing Notebook Problem2_testing_ai.ipynb has been run. Check the 'AI_images_output' directory for output images."

# Test Problem 3
test_prob3:
	@echo "Running Problem 3 Testing Notebook" # Notebook generates results all AI generated testing images of problem 3
	@$(JUPYTER) Problem3_testing_ai.ipynb
	@echo "Testing Notebook Problem3_testing_ai.ipynb has been run. Check the 'AI_images_output' directory for output images."
