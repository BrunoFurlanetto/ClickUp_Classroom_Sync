# Task Scheduling in Windows

In Windows it is necessary to make use of the task scheduler of the operating system 
itself and for that, the following steps must be followed.

Step 1: Open the Task Scheduler:
- Press `Win + R` to open the "Run" dialog. Type `taskschd.msc` and press Enter.

Step 2: Create a new Task:
- In the right panel, click on "Create Basic Task" to start the wizard.

Step 3: Name and Description:
- Enter a name and, optionally, a description for the task.

Step 4: Choose the Trigger Type:
- Select "At Startup" and click "Next".

Step 5: Select the action:
- Select "Start a program" and click "Next".

Step 6: Specify the Program to Run:
- In this step, you should specify the path to the **Pythonw** interpreter (which
   does not require the shell to be open to remain running) and the `main.py` script:
  - In "Program/Script" put the path to the `Pythonw.exe` file present in the 
    project's venv.
  - Now in "Add arguments", put "main.py".
  - Finally put in "Start in" the path of the `main.py` file.

The settings should look like the image below.

![Action configuration](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/action_configuration.jpg)

Step 7: Finish Configuration:
- Click "Finish" to create the task.

Step 8: Define Other Settings:
- You need adjust other settings, for this, click to right button in the task and go to
    properties and follow this configurations:

![Security options](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/security_options.jpg)

![Conditions](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/conditions.jpg)

![Configurations](https://github.com/BrunoFurlanetto/ClickUp_Classroom_Sync/blob/main/docs/configurations.jpg)

Step 9: Review Settings:
- Review the settings you've defined to ensure they are correct.
