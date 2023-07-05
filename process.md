First step is to set up the database for the users,
a database named geoalert
with tables for users info, location info, todo list

## Users

`[id, name, mail, password, created_at, updated_at]`

## Todo

`[id, user_id(foreign key referenci), title, description, due_date, completed(boolean), created_at, updated_at]`

## Location

`[id, user_id(foreign key), name, address, latitude, longitude, created-at, updated-at]`

## LocationReminder

```[id, user-id, location-id, todo-id, radius(in metres), activated(boolean), created-at, updated-at]

```
