# Build script for Vercel deployment

# Make script executable
chmod +x build_files.sh

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

echo "Build completed successfully!"