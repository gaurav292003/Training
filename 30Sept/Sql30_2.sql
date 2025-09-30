CREATE DATABASE UniversityDB;
USE UniversityDB;
-- Students Table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);
-- Courses Table
CREATE TABLE Courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50),
credits INT
);
-- Enrollments Table
CREATE TABLE Enrollments (
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
grade CHAR(2),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Insert Students
INSERT INTO Students VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Arjun', 'Bengaluru'),
(4, 'Neha', 'Hyderabad'),
(5, 'Vikram', 'Chennai');
-- Insert Courses
INSERT INTO Courses VALUES
(101, 'Mathematics', 4),
(102, 'Computer Science', 3),
(103, 'Economics', 2),
(104, 'History', 3);
-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, 'A'),
(2, 1, 102, 'B'),
(3, 2, 103, 'A'),
(4, 3, 101, 'C'),
(5, 4, 102, 'B'),
(6, 5, 104, 'A');


Delimiter $$
Create procedure ListAllStudents()
BEGIN
select * from Students;
END$$
Delimiter ;

CALL ListAllStudents();


Delimiter $$
Create procedure ListAllCourses()
BEGIN
select * from Courses;
END$$
Delimiter ;

CALL ListAllCourses();

Delimiter $$
Create procedure GetStudentBy_City(IN cityName Varchar(50))
Begin
Select * from Students where city = cityName;
End$$
Delimiter ;

CALL GetStudentBy_City('Delhi');


Delimiter $$
Create procedure ListStudentsWithEnrollments()
Begin
select
s.student_id,
s.name as student_name,
s.city,
e.course_id,
e.grade
From Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id;
END$$

Delimiter ;

CALL ListStudentsWithEnrollments();


Delimiter $$
Create procedure GetStudentByCourse(IN courseInput INT)
BEGIN
Select
s.student_id, 
s.name as student_name,
s.city,
e.course_id,
e.grade
From Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = courseInput;
END$$
DELIMITER ;

CALL GetStudentByCourse(101)


DELIMITER $$
Create procedure CountStudents_In_Course()
BEGIN
SELECT 
c.course_id,
c.course_name,
COUNT(e.student_id) AS Total_Students
From Courses c
JOIN Enrollments e ON c.course_id = e.course_id
group by c.course_id, c.course_name
ORDER by Total_Students DESC;
END $$

CALL CountStudents_In_Course();

DELIMITER $$
Create Procedure ListStudentCourse_Grade()
Begin
select
s.student_id,
s.name as student_name,
c.course_name,
e.grade
From Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
ORDER BY s.student_id, c.course_name;
end$$

Delimiter ;
CALL ListStudentCourse_Grade();


Delimiter $$
Create Procedure GetCourseByStudent(IN studentInput INT)
BEGIN
SELECT 
s.student_id,
s.name,
c.course_name,
e.grade
FROM Students s
JOIN Enrollments e ON s.student_id=e.student_id
JOIN Courses c ON e.course_id= c.course_id
WHERE s.Student_id = studentInput;
END$$
DELIMITER ;

CALL GetCourseByStudent(1)

DELIMITER $$ 
CREATE procedure AvgGradePerCourse()
BEGIN
Select 
c.course_id,
c.course_name,
AVG(
	Case e.grade
		When 'A' THEN 4
		When 'B' THEN 3
		When 'C' THEN 2
		When 'D' THEN 1
		ELSE 0
	END
)As avg_grade_points
From Courses c
JOIN Enrollments e ON c.course_id= e.course_id
GROUP BY c.course_id, c.course_name;
END$$

DELIMITER ;

CALL AvgGradePerCourse()










