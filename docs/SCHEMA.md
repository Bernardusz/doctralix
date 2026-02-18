# Schema of Doctralix

## 1. User (Django default)

* username
* email
* password
* groups

## 2. Profile

> Purpose: Extend user identity

* user -> OneToOne(user)
* full_name
* created_at

## 3. Classroom

> Represent a class

* name
* wali_kelas -> OneToOne(User)

## 4. Subject

