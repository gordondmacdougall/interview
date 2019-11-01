# Requirements
- Python 2.7.10 + virtualenv
- Docker + DockerCompose
- Node version v6.9.4 (suggest using nvm for installation)

# Setup

## DB
- `docker-compose up -d`
- import base.sql into DB for a basic setup

## Backend
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python app.py`

## Frontend
- `npm install`