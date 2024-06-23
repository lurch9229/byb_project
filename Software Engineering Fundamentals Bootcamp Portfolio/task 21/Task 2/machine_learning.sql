-- List the names and surnames of all students doing the “DS03” course.
SELECT Student.first_name, Student.last_name
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.course_code = 'DS03';
