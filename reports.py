import sqlite3

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = StudentExerciseReports()
reports.all_students()


class cohortReports():
    """Reports for Cohort information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(f'{cohort[1]}')

cohort_report = cohortReports()
cohort_report.all_cohorts()


class exerciseReports():
    """Reports for Exercise information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ProgramLanguage
            from Exercise e
            """)

            all_exercise = db_cursor.fetchall()

            for exercise in all_exercise:
                print(f'{exercise[1]} {exercise[2]}')

exercise_report = exerciseReports()
exercise_report.all_exercises()


class InstructorReports():
    """Reports for Instructor information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_instructors(self):
        """Retrieve all instructors"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.CohortId,
                i.Specialty,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor[1], instructor[2], instructor[6])

instructor_report = InstructorReports()
instructor_report.all_instructors()


class JavaScriptReports():
    """Reports for JavaScript information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_javascript(self):
        """Retrieve all javascript"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ProgramLanguage
            from Exercise e
            """)

            all_javascript = db_cursor.fetchall()

            for exercise in all_javascript:
                if exercise[2] == "JavaScript":
                    print(f'{exercise[2]} {exercise[1]}')

javascript_report = JavaScriptReports()
javascript_report.all_javascript()


class PythonReports():
    """Reports for Python information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_python(self):
        """Retrieve all python"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ProgramLanguage
            from Exercise e
            """)

            all_python = db_cursor.fetchall()

            for exercise in all_python:
                if exercise[2] == "Python":
                    print(f'{exercise[2]} {exercise[1]}')

python_report = PythonReports()
python_report.all_python()


class DjangoReports():
    """Reports for Django information"""

    def __init__(self):
        self.db_path = "/users/blagg/workspace/sql/ch3/studentexercises.db"

    def all_django(self):
        """Retrieve all django"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.ProgramLanguage
            from Exercise e
            """)

            all_django = db_cursor.fetchall()

            for exercise in all_django:
                if exercise[2] == "Django":
                    print(f'{exercise[2]} {exercise[1]}')

django_report = DjangoReports()
django_report.all_django()