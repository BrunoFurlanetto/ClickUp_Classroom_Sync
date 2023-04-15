# Classroom-ClickUp Sync

This repository contains a Python script to synchronize Classroom and ClickUp data. The script uses the ClickUp API to create tasks in ClickUp based on Classroom assignments.

## Requirements

- Python 3.11 or higher
- pip
- alembic
- ClickUp API key
- Google Classroom API credentials

## Installation

1. Clone this repository
2. Install dependencies by running `pip install -r requirements.txt`
3. Create a `local_settings.py` file in the root directory with the following variables:
   ```
   clickup_email = your_clickup_email
   clickup_pass = your_clickup_pass
   clickup_api_key = your_clickup_api_key
   client_id = your_client_id
   client_secret = your_client_secret
   scopes = [your_scopes]
   ```
4. Run `alembic upgrade head` to create the necessary database tables
5. Run the script using `python main.py`

## Usage
In the first use, the user will be redirected to the Google account selection page, so that he can provide the necessary permissions for the use of his Classroom data.
