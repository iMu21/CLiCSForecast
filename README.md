# Clone the repository
git clone https://github.com/iMu21/CLiCSForecast.git

# Navigate to the project directory
cd CLiCSForecast

# Create a virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Unix or MacOS

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
