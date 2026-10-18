"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.

SCENARIO:
A small course-registration model. `Course` is the parent class (any class a school offers),
and `OnlineCourse` is the child class (a course that also has a platform and meeting links).
Courses hold a roster (a list) and a gradebook (a dict of lists), which gives us nested
mutable data for the shallow vs. deep copy demonstration.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Course:
    """A course with a code, title, credit count, and a roster of students."""

    # Class variables: shared by EVERY Course object (they live in Course.__dict__).
    school = "UMGC"
    max_credits = 6
    courses_created = 0          # running count of every Course/OnlineCourse made

    def __init__(self, code, title, credits=3):
        # --- Edge-case handling (part of TODO 6 extension) ---
        # Reject bad input up front so we never create a broken object.
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code cannot be empty.")
        if not isinstance(credits, int) or not 1 <= credits <= Course.max_credits:
            raise ValueError(f"Credits must be a whole number from 1 to {Course.max_credits}.")

        # Instance variables: unique to each object (they live in self.__dict__).
        self.code = code.strip().upper()
        self.title = title
        self.credits = credits
        self.roster = []                 # nested mutable data (list)
        self.gradebook = {}              # nested mutable data (dict of lists)

        # Update the shared counter through the CLASS, not self.
        # (self.courses_created += 1 would create a new instance variable instead!)
        Course.courses_created += 1

    def enroll(self, student):
        """Add a student to the roster. Ignores blanks and duplicates."""
        student = student.strip() if isinstance(student, str) else ""
        if not student:
            print(f"  [!] Skipped blank student name for {self.code}.")
            return False
        if student in self.roster:
            print(f"  [!] {student} is already enrolled in {self.code}.")
            return False
        self.roster.append(student)
        self.gradebook[student] = []
        return True

    def add_grade(self, student, score):
        """Record a score (0-100) for an enrolled student."""
        if student not in self.gradebook:
            print(f"  [!] Cannot grade {student}: not enrolled in {self.code}.")
            return False
        if not 0 <= score <= 100:
            print(f"  [!] Score {score} is out of range (0-100).")
            return False
        self.gradebook[student].append(score)
        return True

    def average(self, student):
        """Return a student's average, or None if they have no grades yet."""
        scores = self.gradebook.get(student, [])
        if not scores:              # edge case: avoid dividing by zero
            return None
        return sum(scores) / len(scores)

    def describe(self):
        """Return a readable summary of the course."""
        students = ", ".join(self.roster) if self.roster else "(no students yet)"
        return (f"{self.code}: {self.title} | {self.credits} credits | {self.school}\n"
                f"    Roster: {students}")

    def __repr__(self):
        return f"{type(self).__name__}({self.code!r}, roster={self.roster}, gradebook={self.gradebook})"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class OnlineCourse(Course):
    """A Course that is taught online. Inherits everything from Course and adds more."""

    # New class variables for the child class only.
    delivery_mode = "Online"
    default_platform = "LEO"

    def __init__(self, code, title, credits=3, platform=None, weeks=8):
        # Validate the child's own input FIRST. If we called super().__init__ first,
        # the parent would already have bumped courses_created before we raised the
        # error, so a failed object would still be counted.
        if not isinstance(weeks, int) or weeks <= 0:
            raise ValueError("An online course must run for at least 1 week.")

        # super().__init__ runs the parent's constructor, so we get code, title,
        # credits, roster, gradebook, and the input validation for free.
        super().__init__(code, title, credits)

        # New instance variables for the child class.
        self.platform = platform or OnlineCourse.default_platform
        self.weeks = weeks
        self.meeting_links = []

    def add_meeting_link(self, url):
        """New method: only online courses have meeting links."""
        if not url.startswith("http"):
            print(f"  [!] '{url}' does not look like a web link; not added.")
            return False
        self.meeting_links.append(url)
        return True

    def describe(self):
        """Overridden method: reuse the parent's summary, then add online details."""
        base = super().describe()
        return (f"{base}\n"
                f"    Mode: {self.delivery_mode} on {self.platform}, {self.weeks} weeks, "
                f"{len(self.meeting_links)} meeting link(s)")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    data_course = OnlineCourse("cmsc315", "Data Structures and Analysis")
    web_course = OnlineCourse("cmsc335", "Object-Oriented and Concurrent Programming", platform="Zoom")

    # 1) Class variable accessed through the CLASS itself.
    print(f"OnlineCourse.delivery_mode (through the class):  {OnlineCourse.delivery_mode}")

    # 2) Same class variable accessed through an OBJECT.
    #    Python looks in the object's __dict__ first, doesn't find it, then checks the class.
    print(f"data_course.delivery_mode (through an object):   {data_course.delivery_mode}")

    # 3) Add a new attribute to only ONE object after it was created.
    data_course.study_group = "Tuesdays 7pm"
    print(f"\nAdded 'study_group' to data_course only.")
    print(f"  hasattr(data_course, 'study_group'): {hasattr(data_course, 'study_group')}")
    print(f"  hasattr(web_course,  'study_group'): {hasattr(web_course, 'study_group')}")

    # 4) Shadowing: assigning a class variable's name through an object creates a NEW
    #    instance variable on that object. The class value is untouched.
    web_course.delivery_mode = "Hybrid"
    print(f"\nSet web_course.delivery_mode = 'Hybrid' (this shadows the class variable):")
    print(f"  web_course.delivery_mode:   {web_course.delivery_mode}")
    print(f"  data_course.delivery_mode:  {data_course.delivery_mode}")
    print(f"  OnlineCourse.delivery_mode: {OnlineCourse.delivery_mode}")

    # 5) Each object's own namespace.
    print("\ndata_course.__dict__ (instance namespace):")
    for key, value in data_course.__dict__.items():
        print(f"    {key}: {value}")
    print("web_course.__dict__ (instance namespace):")
    for key, value in web_course.__dict__.items():
        print(f"    {key}: {value}")

    # 6) The class namespaces. Filter out Python's built-in "dunder" entries for readability.
    def user_defined(cls):
        return [name for name in cls.__dict__ if not name.startswith("__")]

    print(f"\nOnlineCourse.__dict__ (child class namespace): {user_defined(OnlineCourse)}")
    print(f"Course.__dict__ (parent class namespace):      {user_defined(Course)}")
    print("  Note: 'school' is NOT in OnlineCourse.__dict__, yet data_course.school works:")
    print(f"  data_course.school = {data_course.school!r}  (found by searching up to Course)")
    print(f"  Lookup order (MRO): {[cls.__name__ for cls in OnlineCourse.__mro__]}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Course("cmsc315", "Data Structures and Analysis")
    original.enroll("Ana")
    original.enroll("Ben")
    original.add_grade("Ana", 90)

    # SHALLOW copy: makes a new Course object, but its attributes still point to the
    # SAME inner list and dict as the original. Only the outer "box" is new.
    shallow = copy(original)

    # DEEP copy: makes a new Course object AND new copies of every list/dict inside it,
    # all the way down. Nothing is shared with the original.
    deep = deepcopy(original)

    print("Before changing the original:")
    print(f"  original: {original!r}")
    print(f"  shallow:  {shallow!r}")
    print(f"  deep:     {deep!r}")

    # Modify the original's NESTED data (mutate the list and the dict in place).
    original.enroll("Cara")
    original.add_grade("Ana", 70)

    # Also reassign a simple top-level attribute to show that is NOT shared.
    original.title = "Renamed Course"

    print("\nAfter enrolling Cara, adding a grade for Ana, and renaming the original:")
    print(f"  original: {original!r}")
    print(f"  shallow:  {shallow!r}   <- sees Cara and Ana's 70 (shared list/dict)")
    print(f"  deep:     {deep!r}   <- unchanged (fully independent)")
    print(f"\n  Titles -> original: {original.title!r}, shallow: {shallow.title!r}, deep: {deep.title!r}")
    print("  The shallow copy kept the old title: reassigning an attribute replaces the")
    print("  original's reference only. Shared data only shows up when it is mutated in place.")

    # Identity checks prove what is shared.
    print(f"\n  original.roster is shallow.roster: {original.roster is shallow.roster}")
    print(f"  original.roster is deep.roster:    {original.roster is deep.roster}")


#
# TODO 6 (done): Student-created extension -- edge cases and validation
# My extension adds input validation and edge-case handling to the classes:
#   - empty course codes and out-of-range credits raise ValueError
#   - blank and duplicate student names are skipped with a message
#   - grading a student who is not enrolled, or an out-of-range score, is rejected
#   - average() returns None instead of crashing when there are no grades
#   - a shared class-level counter tracks how many courses have been created
# This function tests each of those cases.

def run_edge_case_tests():
    print("\n=== Edge Case Tests (Extension) ===")

    # Invalid constructor input: each should raise ValueError and be caught.
    bad_inputs = [
        ("", "No Code", 3),
        ("cmsc999", "Too Many Credits", 12),
        ("cmsc000", "Zero Credits", 0),
    ]
    for code, title, credits in bad_inputs:
        try:
            Course(code, title, credits)
            print(f"  FAIL: {title!r} should have been rejected")
        except ValueError as error:
            print(f"  Rejected {title!r}: {error}")

    try:
        OnlineCourse("cmsc401", "Zero Weeks", weeks=0)
    except ValueError as error:
        print(f"  Rejected 'Zero Weeks': {error}")

    # Empty structure: a brand-new course with nobody enrolled.
    empty = Course("math140", "Calculus I", 4)
    print(f"\n  Empty course describe():\n    {empty.describe()}")
    print(f"  Average for a student with no grades: {empty.average('Nobody')}")

    # Blank and duplicate names, ungraded/unknown students, bad scores, bad links.
    online = OnlineCourse("cmsc315", "Data Structures and Analysis", weeks=8)
    online.enroll("Ana")
    online.enroll("Ana")          # duplicate
    online.enroll("   ")          # blank
    online.add_grade("Zed", 88)   # not enrolled
    online.add_grade("Ana", 105)  # out of range
    online.add_grade("Ana", 95)
    online.add_grade("Ana", 85)
    online.add_meeting_link("not a link")
    online.add_meeting_link("https://example.com/cmsc315-office-hours")
    print(f"  Ana's average after two valid grades: {online.average('Ana'):.1f}")
    print(f"\n  Final online course:\n    {online.describe()}")

    # Shared class counter: only successfully created objects are counted.
    print(f"\n  Course.courses_created (shared by parent and child): {Course.courses_created}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Parent object (Course) ---")
    calculus = Course("math140", "Calculus I", 4)
    calculus.enroll("Ana")
    calculus.enroll("Ben")
    calculus.add_grade("Ana", 92)
    print(calculus.describe())
    print(f"Ana's average in {calculus.code}: {calculus.average('Ana')}")

    print("\n--- Child object (OnlineCourse) ---")
    data_structures = OnlineCourse("cmsc315", "Data Structures and Analysis", platform="LEO", weeks=8)
    data_structures.enroll("Ana")            # inherited method from Course
    data_structures.enroll("Cara")
    data_structures.add_grade("Cara", 88)    # inherited method
    data_structures.add_meeting_link("https://example.com/cmsc315-live")  # child-only method
    print(data_structures.describe())        # overridden method (adds the "Mode:" line)

    print("\n--- Inheritance checks ---")
    print(f"isinstance(data_structures, Course):       {isinstance(data_structures, Course)}")
    print(f"isinstance(calculus, OnlineCourse):        {isinstance(calculus, OnlineCourse)}")
    print(f"issubclass(OnlineCourse, Course):          {issubclass(OnlineCourse, Course)}")
    print(f"Child inherits parent's class var school:  {data_structures.school}")
    print(f"Parent has the child's add_meeting_link?:  {hasattr(calculus, 'add_meeting_link')}")

    demonstrate_namespaces()
    demonstrate_copying()
    run_edge_case_tests()


if __name__ == "__main__":
    main()
