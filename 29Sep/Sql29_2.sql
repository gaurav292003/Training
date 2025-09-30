Create database SchoolDb;
Use schoolDb;

Create table Teachers(
teacher_id INT auto_increment Primary Key,
name varchar(50),
subject_id INT,
foreign key (subject_id ) references Subjects(subject_id)
);

Create table Subjects(
subject_id INT auto_increment primary key,
subject_name varchar(50)
);

INSERT INTO Subjects (subject_name) VALUES
('Mathematics'),   -- id = 1
('Science'),       -- id = 2
('English'),       -- id = 3
('History'),       -- id = 4
('Geography');     -- id = 5 (no teacher yet)

INSERT INTO Teachers (name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English


Select t.name, t.subject_id , s.subject_name
From Teachers t
Inner Join Subjects s
ON t.subject_id= s.subject_id;

Select e.name, e.salary , d.dept_name
From Employees e
Left Join Departments d
ON e.dept_id= d.dept_id;

Select e.name, e.salary , d.dept_name
From Employees e
Right Join Departments d
ON e.dept_id= d.dept_id;

Select e.name, e.salary , d.dept_name
From Employees e
Left Join Departments d
ON e.dept_id= d.dept_id
UNION
Select e.name, e.salary , d.dept_name
From Employees e
Right Join Departments d
ON e.dept_id= d.dept_id;