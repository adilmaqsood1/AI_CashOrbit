#!/bin/bash

# Print Python and pip versions for debugging
which python || echo "Python not found"
which pip || echo "Pip not found"
python --version || echo "Python version command failed"
pip --version || echo "Pip version command failed"

# Ensure pip is available using python module
python -m pip --version || echo "Python -m pip failed"

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

echo "Build completed successfully!"