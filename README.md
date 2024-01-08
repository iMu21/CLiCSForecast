To run this project in your device, run these commands one by one from cmd.
https://github.com/iMu21/CLiCSForecast.git
cd CLiCSForecast
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
