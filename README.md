# Требования

* Python >= 3.8.5
* Django >= 3.0.3
* djangorestframework >= 3.11.1
* gunicorn >= 20.0.4
* coverage >= 5.2.1

# API

## GET /api/students/
Принимает: -

Возвращает:
```
[
    объект Student,
    объект Student,
    ...
]
```

## POST /api/students/
Принимает: объект **Student**

Возвращает: объект **Student**

## GET /api/students/{studentID}
Принимает: -

Возвращает: объект **Student**

## PATCH /api/students/{studentID}
Принимает: любой параметр объекта **Student**

Возвращает: объект **Student**

## DELETE /api/students/{studentID}
Принимает: -

Возвращает: -


# Структуры данных

## Student
```
{
    "id": Integer,
    "full_name": String,
    "birth_date": String (DD-MM-YYYY),
    "mark": Integer
}
```