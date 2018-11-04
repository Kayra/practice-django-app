# Django Application Tutorial

This is the code written while following the [official Django tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/).

## Set up

### Mac installation instructions

```bash
# Install homebrew 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update

# Install python
brew install python

# Create a virtual environment for Python
python3 -m venv venv

# Source the virtual environment
source venv/bin/activate

# Install the Python dependencies
pip install -r requirements.txt
```

### Running the local development server

```bash
# Source the virtual environment
source venv/bin/activate

# Run the local development server
python mysite/manage.py runserver
```

The application can now be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/polls/34/vote/)

## Utility commands

### Creating an admin account

```bash
# Source the virtual environment
source venv/bin/activate

# Create a super user
python mysite/manage.py createsuperuser
```

You can now use the credentials you entered to visit the [admin panel.](http://127.0.0.1:8000/admin)

### Running tests

```
# Source the virtual environment
source venv/bin/activate

# Run the tests for the `polls` app
python mysite/manage.py test polls
```