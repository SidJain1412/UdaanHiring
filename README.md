# Udaan

## Siddharth Jain (RA1611003010649 SRM, CSE)

All given APIs have been implemented. 


Python (Flask) has been used for the backend.

HTML+CSS have been used for the frontend.

### Screenshots are attached in images folder.

### Instructions to run the program:

1. Unzip the file.
2. Make sure you have python3+ with pip installed.
3. Open a terminal in the unzipped folder.
4. Execute `pip install -r requirements.txt` to install dependencies.
5. Once executed, execute `python run.py`
6. Navigate to `127.0.0.1:5000` to open the website

### Features:

1. Database is included (using SQLAlchemy)
2. Worker email is checked using regular expressions for validity
3. If an asset already exists, it's count will be incremented when added again
4. Duplicates are checked for all insertions
5. Validating count of assets (>0)
6. APIs are functional (test using Postman or some similar application)
7. Store date and time of creation of all data

API List:

- `127.0.0.1:5000/add_asset`:
  + Method="POST"
  + Returns add asset form page with relevant alert
  + Adds asset to the database
  + If asset already exists, increments its count
  
- `127.0.0.1:5000/allocate_task`:
  + Method="POST"
  + Allocates task to a worker based on task and asset id
  + Allocates a date and time to complete the task before
  
- `127.0.0.1:5000/add_worker`:
  + Method="POST"
  + Adds worker name, email, and mobile number
  + Validates Email ID
  
- `127.0.0.1:5000/assets/all`:
  + Method="GET"
  + Returns JSON containing all assets (names and counts)
  
- `127.0.0.1:5000/add_task`:
  + Method="POST"
  + Adds a task
  + Adds its name and frequency of performing (validating frequency)
  
- `127.0.0.1:5000/get_tasks_for_workers/<worker_id>`:
  + Method="GET"
  + Returns JSON of all tasks assigned to a worker
