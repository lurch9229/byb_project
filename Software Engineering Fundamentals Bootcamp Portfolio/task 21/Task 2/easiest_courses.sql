-- List the first names of all students that achieve a mark of 70 or above - along with the course name that they got a mark of 70 or above in.
SELECT Student.first_name, Course.course_name
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Student.mark >= 70;
