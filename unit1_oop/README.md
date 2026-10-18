# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

---

## My Implementation

### Scenario
I modeled a small course-registration system:

- **`Course` (parent class):** any course a school offers. It has a code, title, credit count, a **roster** (list of students) and a **gradebook** (dict mapping each student to a list of scores). Methods: `enroll()`, `add_grade()`, `average()`, `describe()`.
- **`OnlineCourse` (child class):** inherits everything from `Course` and adds a platform (e.g. LEO, Zoom), a length in weeks, and a list of meeting links. It adds a new method, `add_meeting_link()`, and **overrides** `describe()`, calling `super().describe()` and then adding the online details.

### How each concept is shown

| Concept | Where | What the output shows |
|---|---|---|
| Inheritance | `main()` | An `OnlineCourse` uses `enroll()` and `add_grade()` without redefining them. `isinstance` and `issubclass` confirm the relationship. A plain `Course` does **not** get the child's `add_meeting_link`. |
| Class vs. instance namespace | `demonstrate_namespaces()` | `delivery_mode` reads the same through the class and through an object. `study_group` added to one object only exists on that object. Setting `web_course.delivery_mode = "Hybrid"` **shadows** the class variable on that one object without changing the class. `school` isn't in `OnlineCourse.__dict__` but still works, because Python searches up the MRO (`OnlineCourse → Course → object`). |
| Shallow vs. deep copy | `demonstrate_copying()` | After the original's roster and gradebook are changed, the **shallow** copy shows the changes (it shares the same list and dict, `original.roster is shallow.roster` is `True`). The **deep** copy is unchanged. Renaming the original's title does *not* affect the shallow copy, because reassigning an attribute is different from mutating shared data. |

### Extension (TODO 6): validation and edge cases
I added input checks and a test function, `run_edge_case_tests()`:

- Empty course code, credits outside 1–6, or 0 weeks → `ValueError`, caught and printed.
- Blank or duplicate student names → skipped with a message.
- Grading a student who isn't enrolled, or a score outside 0–100 → rejected.
- `average()` on a student with no grades returns `None` instead of dividing by zero.
- Meeting links that don't start with `http` are rejected.
- A shared class variable, `Course.courses_created`, counts every successfully created course, parent or child.

**Edge case I found:** at first, an `OnlineCourse` with 0 weeks was still being counted, because `super().__init__()` ran (and increased the counter) before the weeks check raised its error. I moved the child's validation **before** the `super()` call so failed objects are never counted. The final count is 7.

### Real-world use
This is the same pattern a learning-management system like LEO uses: a general "course" type shared by every class, with specialized versions (online, hybrid, lab) that reuse the core enrollment and grading code. Deep copying matters in practice. If you copied last semester's course as a template with a *shallow* copy, enrolling new students would also change last semester's roster.

### How to run
```
python unit1_discussion.py
```
