python -m pip install pytest pytest-asyncio


# Exercise 1
pytest -v test_python_gym.py::test_01_even_numbers

# Exercise 9
pytest -v test_python_gym.py::test_09_combine

# Everything relating to exercise 25
pytest -v -k "test_25"

# Async section
pytest -v -k "test_4"

# Finally:
pytest -v 
