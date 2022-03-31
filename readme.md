# How to run

1. `python manage runser`
2. `npm start --prefix frontend`

# Installations

1. python 3.9.7+
3. node.js
4. create env: `python3 -m venv kdw_env`
5. activate: `source  kdw_env/bin/activate`
6. run: `pm2 start npm --log  /home/developer/logs/kdw.log --name kdw-back -- run start-python`
7. or: `pip install -r requirements.txt`
8. run:  `npm install` from _frontend_  folder
9. create file _dbapi/config.py_ with authorization data for database by the example _dbapi/config.example.py_

# DB scripts

to create table role with history data

```
create table roles as
select users.id as user_id, role as role_id, (case when state = 3 then 4 else state end) as state, 2022 as year
from users left join speaker_user_reports on (users.id = speaker_user_reports.user_id AND
                         speaker_user_reports.id = (SELECT max(id)
                                                     FROM speaker_user_reports
                                                     WHERE speaker_user_reports.user_id = users.id))
where users.created_at > '2021-12-31'
```
