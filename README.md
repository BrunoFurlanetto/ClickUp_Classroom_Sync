# Google Classroom - ClickUp Synchronization Documentation

## Overview

These documents are intended to help students utilize the Google Classroom - 
ClickUp synchronization system. The goal of this step-by-step guide is to walk
you through the process of setting up and running the project on your own 
machine, allowing you to automate data transfer between Google Classroom and 
ClickUp.

## Prerequisites

1. Python 3.11 or higher.
2. ClickUp API Credentials.
3. MySQL.

## Step 1: Project Configuration

1. Clone the project repository:

```bash
git clone https://github.com/your-username/google-classroom-clickup-sync.git

cd google-classroom-clickup-sync
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Step 2: API Credentials Configuration

1. Google Classroom Credentials:
   - The first time you use the system, it will redirect you to the Google 
     authorization screen. After that, you won't need to provide these 
     permissions again.

2. ClickUp Credentials:
   - For ClickUp, follow the instructions presented in the ClickUp API 
     documentation:
     - Log in to ClickUp.
     - Click on your avatar in the bottom-left corner and select "Apps".
     - Under "API Token", click "Generate".
     - You can copy and paste your personal API token whenever needed!
   - At this point, create a `.env` file and save the generated token in it:
     ```
     clickup_api_key = '<YOUR_API_TOKEN>'
     ```

## Step 3: Additional Configuration

1. At this point, you need to create and configure a MySQL database, and then 
   save the URL of your database in the `.env` file:
   ```
   url_db = 'mysql+pymysql://user:password@localhost/db_name'
   ```
   Replace all data in the URL with the corresponding information of your
   database.

2. Run the necessary migrations on the database:
   ```bash
   alembic upgrade head
   ```

3. In the 'Spaces' table of the database, register the ID and name of the 
   space within ClickUp to which the lists related to the classes must be registered.
   - Open the space you want to use in your web browser.
   - In the browser's address bar, you will see the Space URL, which is
      typically something like `https://app.clickup.com/1234567/v/l/123456/`.
      The Space ID is the set of characters after the last slash ("/"), so in this example, the Space ID would be `123456`. It may also appear as `https://app.clickup.com/1234567/v/l/4-123456-1/`, and in this case, take only the middle number.

## Step 4: Task Scheduling

To schedule the execution of the Python synchronization script for Google
Classroom with ClickUp on Windows, you can use the system's Task Scheduler. Here's a summarized step-by-step guide:

Step 1: Open the Task Scheduler:
- Press `Win + R` to open the "Run" dialog. Type `taskschd.msc` and press Enter.

Step 2: Create a new Task:
- In the right panel, click on "Create Basic Task" to start the wizard.

Step 3: Name and Description:
- Enter a name and, optionally, a description for the task.

Step 4: Choose the Trigger Type:
- Select "At Startup" and click "Next".

Step 5: Specify the Program to Run:
- In this step, you should specify the path to the Pythonw interpreter (which
   does not require the shell to be open to remain running) and the `main.py` script.

Step 6: Define Other Settings (Optional):
- You can adjust other settings, such as running the task only when a user is
   logged in, setting privileges, and more.

Step 7: Review Settings:
- Review the settings you've defined to ensure they are correct.

Step 8: Finish Configuration:
- Click "Finish" to create the task.

To ensure that the scheduling settings are correct, run the task and see if
the status remains "Running".

From this point on, the synchronizer is working and should start along with 
Windows. The system checks it right at startup and every day between 2 PM and 
8 PM. It will only launch a synchronization notification if there's a 
difference between the local database and the remote systems; otherwise, it 
will run silently.

## Final Remarks

With this step-by-step guide, you have configured and executed the Google 
Classroom - ClickUp synchronization system. Now, you can automate the data 
transfer between platforms and optimize class and task management.

If you have any questions or encounter issues, feel free to refer to the 
project documentation or contact the maintenance team. Enjoy using the system 
to enhance your student experience!