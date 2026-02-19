# Website Flow

## / (Index)

> Lives in accounts app, basically a shortcut to everything (Dashboard), and differ based on User Group you're in.

User group that can access:

* Admin (Principal + Admin) → Dashboard for important events and who needs immediate attention.
* Wali Kelas → Dashboard for monitoring your own students.
* Teacher → Dashboard for all the classes you're in
* Student → Dashboard for all assignments.

> If you're both Wali Kelas and Teacher, there will be a separate scrolling: Wali Kelas on top and Teacher below.

## /accounts/

> All the information about other people. (If you have access)

User group that can access:

* Admin → Unrestricted access to everyone, and every account.
* Wali Kelas → Unrestricted access to all his/her students.
* Teacher → Restricted access to all his/her students inside the subject (Can't see their personal information)
* Student → Restricted access to all his/her classmates.

## /accounts/:slug

> Get the specific information for other people. (If you have access)

User group that can access:

* Admin → Unrestricted access to everyone, and every account.
* Wali Kelas → Unrestricted access to all his/her students.

## /accounts/:slug/edit

> Edit the information for other people/yourself. (If you have access)

User group that can access:

* Admin
* Everyone → To their own account.

## /accounts/:slug/delete

> Delete other people. (If you have access)

User group that can access:

* Admin

## /classrooms/

> Get information for all classes (Like Wali Kelas, etc.)

User group that can access:

* Everyone

## /classrooms/:slug/

> Get information for specific classroom.
> All available subjects only inside your own specific class.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Student → Their own class

## /subjects/

> Show every subject you have access to.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject
* Student → Their own class

## /subjects/:slug/

> Show all assignments for this subject.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject
* Student → Their own class

## /calendar/

> Get the calendar showing every deadline.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject & Assignments
* Student → Their own assignments

## /assignments/

> Show all assignment you need to work on

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject & Assignments
* Student → Their own assignments

## /assignments/:slug/

> Show specific data about this assignment.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject & Assignments
* Student → Their own assignment

## /assignments/:slug/submissions/

> Show all submissions for this assignment

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject & Assignments
* Student → Their own assignment

## /assignments/:slug/submissions/:id/

> Show specific submissions for this assignment.

User group that can access:

* Admin
* Wali Kelas → Their own class
* Teacher → Teaching this subject & Assignments
* Student → Their own assignment

## /accounts/create

> Get the specific information for other people. (If you have access)

User group that can access:

* Admin

> Permission checks are happening in Views via decorators.
