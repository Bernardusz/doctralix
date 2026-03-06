from django.contrib.auth.models import User

def is_teacher(user: User) -> bool:
    return user.groups.filter(name="Teacher").exists()


def is_student(user: User) -> bool:
    return user.groups.filter(name="Student").exists()


def is_wali_kelas(user: User) -> bool:
    return user.groups.filter(name="Wali Kelas").exists()


def is_admin(user: User) -> bool:
    return user.groups.filter(name="Admin").exists()