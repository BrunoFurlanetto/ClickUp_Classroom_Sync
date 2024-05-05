# Google Classroom - ClickUp Synchronization Documentation

## Overview

These documents are intended to help students utilize the Google Classroom -
ClickUp synchronization system. The goal of this step-by-step guide is to walk
you through the process of setting up and running the project on your own
machine, allowing you to automate data transfer between Google Classroom and
ClickUp.

To read the documentation in Portuguese [click here](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/readme-pt.md).

## Prerequisites

1. Python 3.11 or higher.
2. ClickUp API Credentials.

## Step 1: Project Configuration

1. Clone the project repository:

```bash
git clone https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync.git

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
    [documentation](https://clickup.com/api/developer-portal/authentication/):
        - Log in to ClickUp.
        - Click on your avatar in the bottom-left corner and select "Apps".
        - Under "API Token", click "Generate".
        - You can copy and paste your personal API token whenever needed!
    - At this point, create a `.env` file and save the generated token in it:
      ```
      clickup_api_key = '<YOUR_API_TOKEN>'
      ```

## Step 3: Additional Configuration

1. This project uses a local database in sqlite, aiming to reduce the number of
   requests made to the APIs. Thus, it is necessary to implement the migrations
   coming from alembic as follows

```bash
alembic upgrade head
```

2. After applying the migrations, it is necessary to register the ID and name of
   the space that will receive the new lists coming from Google Classroom (In the
   alpha version, it will be necessary to use third-party tools to be able to
   register).

    - In the 'Spaces' table of the database, register the ID and name of the 
        space within ClickUp to which the lists related to the classes must be
        registered.
        - Open the space you want to use in your web browser.
        - In the browser's address bar, you will see the Space URL, which is
            typically something like `https://app.clickup.com/1234567/v/l/123456/`.
            The Space ID is the set of characters after the last slash ("/"), so 
            in this example, the Space ID would be `123456`. It may also appear
            as `https://app.clickup.com/1234567/v/l/4-123456-1/`, and in this
            case, take only the middle number.

## Step 4: Task Scheduling

To schedule the execution of the Python synchronization script for Google
Classroom with ClickUp on Windows, you can use the system's Task Scheduler. For more
information [click here](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/task_scheduling_windows.md).

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

## Future features

This synchronizer is constantly evolving to meet the needs of users. Below are some 
of the features we are considering implement in the future:

1. **Graphical interface**: One of the first features being considered, is the
implementation of a graphical interface to facilitate both the registration of API 
KEYs and views of the latest tasks that were found on Google Classroom and which 
were added to ClickUp.
2. **Increase in notifications**: An increase in the number of notifications and not
just when sync starts.
3. **Urgent Check and WhatsApp Messages**: Lastly, it is being considered is the
implementation of a verification of activities already registered in the ClickUp and
with this the sending of messages via WhatsApp reminding you of the delivery date of
the activity. At this stage, the change of urgency status of the task according to
the proximity to the task delivery date.
