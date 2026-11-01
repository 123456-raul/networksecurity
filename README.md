### This is my Network Security Projects for Phising Data


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### Run locally

Copy `.env.example` to `.env` and fill in the values, then:

venv/python.exe test_mongodb.py   (check the MongoDB connection)

venv/python.exe push_data.py      (run once only, each run inserts the rows again)

venv/python.exe -m uvicorn app:app --port 8000

Open http://localhost:8000/docs. `/train` trains and uploads to S3, `/predict` takes a CSV such as `valid_data/test.csv`.
