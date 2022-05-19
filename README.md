# Description
A practical application of a Human Resources department database created using Python, PostgreSQL, and Django.

An exercise in creating a relational database.  Using the exercise practice example in the url below as a guide.

https://www.w3resource.com/postgresql-exercises/

## Application State

Currently deployed on Heroku.  You can view it using the link below.

https://radiant-headland-38660.herokuapp.com/regions/

*Note: You can use the endpoints in the table below to navigate through the Django application.

Uses Django REST Framework for user authentication.  You can use the super user information below to use the application.

Username: guest1
Password: guest123

## Technologies Used
- Python
- Django
- Django Rest Framework
- PostgreSQL

## Contribution Guidelines

> If you identify bugs, submit an issue on the Git repo. Please detail the bug in your issue. If you know how to fix it, feel free to note the methods you would use. You could also submit a pull request with suggested code to fix it.

## Future Improvements

Adding Django authentication so the data that is available is from the user who created it instead of letting any user modify the existing data.

## API Route Paths

| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | /regions/ | Read all regions |
| GET | /regions/:id | Read one region |
| POST | /regions/ | Create one region |
| PUT | /regions/:id | Update one region |
| DELETE | /regions/:id | Delete one region |
| GET | /countries/ | Read all countries |
| GET | /countries/:id | read one country |
| POST | /countries/ | Create one country |
| PUT | /countries/:id | Update one country |
| DELETE | /countries/:id | Delete one country |
| GET | /locations/ | Read all locations |
| GET | /locations/:id | Read one location |
| POST | /locations/ | Create one location |
| PUT | /locations/:id | Update one location |
| DELETE | /locations/:id | Delete one location |
| GET | /departments/ | Read all departments |
| GET | /departments/:id | Read one department |
| POST | /departments/ | Create one department |
| PUT | /departments/:id | Update one department |
| DELETE | /departments/:id | Delete one department |
| GET | /jobs/ | Read all jobs |
| GET | /jobs/:id | Read one job |
| POST | /jobs/ | Create one job |
| PUT | /jobs/:id | Update one job |
| DELETE | /jobs/:id | Delete one job |
| GET | /employees/ | Read all employees |
| GET | /employees/:id | Read one employee |
| POST | /employees/ | Create one employee |
| PUT | /employees/:id | Update one employee |
| DELETE | /employees/:id | Delete one employee |
| GET | /job_histories/ | Read all Job Histories |
| GET | /job_histories/:id | Read one Job History |
| POST | /job_histories/ | Create one Job History |
| PUT | /job_histories/:id | Update one Job History |
| DELETE | /job_histories/:id | Delete one Job History |