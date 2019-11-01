# What do you have?
- Basic application running python backend/angular frontend + DB
- Database contains a table with companies and departments. Company can have multiple departments.
- Application allows for viewing and creating companies

# What do you need to do?
- Add an ability to list, add, remove employees of companies
- Don't worry about permissions
- Adjust existing code as you see fit to achieve the goal
- Database migration can be provided as a seperate SQL file

# How do you need to do it?
- Fork this repository
- Add commits in as clean format as you would normally do it
- Create a PR against this repo

# How do you start?
## Requirements
- Python 2.7.10 + virtualenv
- Docker + DockerCompose
- Node version v6.9.4 (suggest using nvm for installation)

## Setup
### DB
- `docker-compose up -d`
- import base.sql into DB for a basic setup

### Backend
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python app.py`

### Frontend
- `npm install`
- `gulp`