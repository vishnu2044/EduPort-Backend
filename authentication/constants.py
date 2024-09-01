# ------ User types section -------
ROLE_ADMIN = "Admin"
ROLE_INSTRUCTURE = "Instructor"
ROLE_STUDENT = "Student"
ROLE_STAFF = "Staff"

ROLES = [
    ROLE_ADMIN,
    ROLE_INSTRUCTURE,
    ROLE_STUDENT,
    ROLE_STAFF,

]

ROLE_CHOICES = (
    (ROLE_ADMIN, "admin"),
    (ROLE_INSTRUCTURE, "instructor"),
    (ROLE_STUDENT, "student"),
    (ROLE_STAFF, "staff"),
)
# ROLES_CAN_ASSIGN_USERS_TO_JOBS = (ROLE_SUPERVISOR, ROLE_ADMIN, ROLE_MANAGER)
# ------ End of User types section -------
