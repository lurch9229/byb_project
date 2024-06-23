-- List the marks of all students who have been taught by Julia Python.
SELECT Student.mark
FROM Student
INNER JOIN Course ON Student.stu_subject_code = Course.course_code
WHERE Course.teacher_name = 'Julia Python';
