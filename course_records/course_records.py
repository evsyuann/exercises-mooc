class Course:
    def __init__(self, grade: int, credits: int):
        self._grade = grade
        self._credits = credits

    @property
    def grade(self):
        return self._grade

    @property
    def credits(self):
        return self._credits

    @grade.setter
    def grade(self, value):
        self._grade = value


class CoursesInfo:
    def __init__(self):
        self.courses = {}

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        if self.courses.get(course) == None:
            self.courses[course] = Course(grade, credits)
        else:
            if grade >= self.courses[course].grade:
                self.courses[course].grade = grade

    def get_data(self):
        course = input("course: ")
        if self.courses.get(course) == None:
            print("no entry for this course")
        else:
            print(
                f"{course} ({self.courses[course].credits} cr) grade {self.courses[course].grade}"
            )

    def total_information(self):
        total_courses = len(self.courses)
        total_credits = 0
        total_grades = 0
        for course in self.courses.values():
            total_credits += course.credits
            total_grades += course.grade
        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {(total_grades/total_courses):.1f}")

    def grade_distribution(self):
        grades = [0] * 5
        for course in self.courses.values():
            grades[course.grade - 1] += 1
        print("grade distribution")
        for i in range(5,0,-1):
            x = "x"* grades[i-1]
            print(f"{i}: {x}")


class Application:
    def __init__(self):
        self.courses_info = CoursesInfo()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break

            if command == "1":
                self.courses_info.add_course()

            if command == "2":
                self.courses_info.get_data()

            if command == "3":
                self.courses_info.total_information()
                self.courses_info.grade_distribution()


application = Application()
application.execute()

