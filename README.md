
1) Start a virtualenvironment: 
`python3 -m venv venv`
`source venv/bin/activate` (for Mac)

2) Open the docker desktop UI 

3) From the root directory:
 `docker-compose build` 

4) `docker-compose up`
   
5) Open browser and go to url: *http://127.0.0.1:8000/*
   Check the  {"message": "Hello World"} appears

----Connecting PGAdmin to the Database-----

6) Go to URL: *http://127.0.0.1:5050*
   Login with: username = admin@admin.com, password = password

7) Right-click on 'servers' in the left column and select register. In the register - server box use the name: DB then under the 'Connection' tab fill the following: 
   i) host name: db
   ii) Port: 5432
   iii) Maintenance Databse: postgres
   iv) Username: postgres
   v) Password: password 

----Creating a Migration----

8) From the root directory inside the venv use the below: 
   `docker-compose run app alembic revision --autogenerate -m "New Migration"`
   to create a migration

9) Then run:
    `docker-compose run app alembic upgrade head`
   to push the migration 

10) Go back to the PGadmin and the patient table will be visible - click servers, Databases, patient_db, schemas and under tables the patient table is visible when you right click and select 'view/edit data' 'all rows'. The table and columns should be visible by now. 

----Adding Patient----

11) Go to URL: *http://127.0.0.1:8000/docs*

13) Select POST /add-patient/ Add Patient. Click the 'Try it out' button. 

12) Key in the patient values in the Reqeust Body box eg. 

{
   "reference number: 231,
   "name: "Mr T Rotario", 
   "date_of_birth", "3/2/1982",
   "address", "352 The Glades, Ashby Town"
}

13) Press the blue "Execute" button underneath and ensure that the server response underneath records a 200. 

14) Return to URL: *http://127.0.0.1:5050* and refresh - your patient record should be recorded in your table. 

---Displaying All Patients

15) Go to URL: *http://127.0.0.1:8000/docs* and select the GET /patients Get Patients button. Click "Execute" and wait for the 200 response - within the response body should be all the patients you have recorded previously. 

Key Commands

pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head

docker-compose build
docker-compose up