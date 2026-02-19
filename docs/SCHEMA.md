# Schema of Doctralix

## Database Schema

### 1. User (Django default)

* username
* email
* password
* groups

### 2. Account

> Purpose: Extend user identity

* user → OneToOne(user)
* full_name
* created_at
* classroom = FK(classroom) → Per User there's only one classroom, But classroom can have many students.

### 3. Classroom

> Represent a class

* name
* wali_kelas → FK(User)
* slug

### 4. Subject

> Subject Taught in a Classroom

* name
* classroom
* teacher → ManyToMany(User) <!--Every Subject has many teachers-->
* slug

### 5. Assignment

> Task created by teacher

* title
* description
* file
* subject → FK(Subject)
* due_date
* created_at
* updated_at
* slug

### 6. Submission

> Student's submission for each assignment

* assignment → FK(Assignment)
* student → FK(User)
* file
* grade
* submitted_at
* id

## Group Schema

> All groups needed to based permission

### 1. Admin → Later Principal + Admin/IT (V1.0)

> A user that can create/read/update/delete every user

Permission:

* Can create user with any group
* Can read every user's information
* Can update every user's information
* Can delete every user's information

Tightly coupled Model:

* User (C/R/U/D)
* Account (C/R/U/D)
* Classroom (C/R/U/D)
* Subject (C/R/U/D)

Reasoning:

> Why would a principal/admins create(s) an assignment 🐧💀? We need people who can manage everything behind the scene.

### 2. Student (V1.0)

> A student can only create/read/update/delete his/her own submission

Permission:

* Can do CRUD operation with his/her own submission, and account

Tightly coupled Model:

* User (R/U → Himself/Herself) <!--Password only-->
* Account (R/U) + (R → Other people)
* Assignment (R)
* Submission (C/R/U/D)

Reasoning:

> A student is never allowed to delete his account and can only Read Assignment and CRUD Submission.

### 3. Teacher (V1.0)

> A teacher can only do CRUD operation on his/her own subject.

Permission:

* Can CRUD assignment on his/her own subject.

Tightly coupled Model:

* User (R/U → Himself/Herself)
* Account (R/U) + (R → Other people)
* Assignment (C/R/U/D)
* Submission (R)

Reasoning:

> A teacher, can't interfere with student's work, only give grades. He can do CRUD on his own Subject's assignment.

### 4. Wali Kelas (v1.0)

> A "Special teacher" who can guard, but not interfere in his/her classroom subjects.

Permission:

* Can read all his/her classroom's Subjects, Assigntment, and Submission.

Tightly coupled Model:

* User (R/U → Himself/Herself)
* Account (R/U) + (R → Other people)
* Assignment (R → His/Her Classroom)
* Submission (R → His/Her Classroom)

### 5. Principal (v2.0)

> Basically? An admin with unlimited power 💀🐧

Permission:

* Can create user with any group
* Can read every user's information
* Can update every user's information
* Can delete every user's information

Tightly coupled Model:

* User (C/R/U/D)
* Account (C/R/U/D)
* Classroom (C/R/U/D)
* Subject (C/R/U/D)

Reasoning:

> Why would a principal create an assignment 🐧💀? The principal can do everything, since he is the one managing the whole school, and is trusted doing so.

### 6. Admin/IT Staffs (v2.0)

> Can do everything but fire the principal 🐧💀

Permission:

* Can create user with any group
* Can read every user's information
* Can update every user's information
* Can delete every user's information

Tightly coupled Model:

* User (C/R/U/D) + (C/R/U → Principal)
* Account (C/R/U/D)
* Classroom (C/R/U/D)
* Subject (C/R/U/D)

Reasoning:

> Why would an IT create an assignment 🐧💀? IT Staffs need to be able to do heavy stuffs when people ask them to. However, every single action will be recorded to percent malicious act.
