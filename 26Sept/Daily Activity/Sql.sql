Create database SchoolDB;

Use SchoolDB;

Create table student(
	id INT auto_increment primary key,
    name varchar(50),
    age int,
    course varchar(50),
    marks int
);

Insert into student(name, age, course, marks)
Values
('Priya', 22,'ML', 90),
('Arjun',20, 'Data Science',78);

Insert into student(name, age, course, marks)
Values
('Neha', 21,'AI', 91),
('Dev',20, 'Data Science',77);

Select * from student;

Select name, age from student where marks>80;

Select name, marks from student;

Update student 
Set marks = 94
where id= 1;

Select * from student;

Delete from student where id=3;