
1) Start a virtualenvironment: 
`python3 -m venv venv`
`source venv/bin/activate` (for Mac)

2) Open the docker desktop UI 

3) From the root directory:
 `docker-compose build` 

4) `docker-compose up`
   
5) Open browser and go to url: *http://127.0.0.1:8000/*
   Check the  {"message": "Hello World"} appears

----
6) Go to URL: *http://127.0.0.1:5050*
   Login with: username = admin@admin.com, password = password

7) 




Key Commands

pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head

docker-compose build
docker-compose up