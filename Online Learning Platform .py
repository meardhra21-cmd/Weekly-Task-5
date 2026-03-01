from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


class ProgrammingCourse(Course):
    def __init__(self, course_name, duration, language):
        super().__init__(course_name, duration)
        self.language = language

    def course_details(self):
        print("Programming Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Language Covered:", self.language)
        print("-" * 30)


class DesignCourse(Course):
    def __init__(self, course_name, duration, tool):
        super().__init__(course_name, duration)
        self.tool = tool

    def course_details(self):
        print("Design Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Tool Used:", self.tool)
        print("-" * 30)


class MarketingCourse(Course):
    def __init__(self, course_name, duration, specialization):
        super().__init__(course_name, duration)
        self.specialization = specialization

    def course_details(self):
        print("Marketing Course")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)
        print("Specialization:", self.specialization)
        print("-" * 30)


course1 = ProgrammingCourse("Python for Beginners", "3 Months", "Python")
course2 = DesignCourse("UI/UX Mastery", "2 Months", "Figma")
course3 = MarketingCourse("Digital Marketing Pro", "4 Months", "SEO & Ads")

course1.course_details()
course2.course_details()
course3.course_details()
