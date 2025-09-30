Create database CompanyDB;
Use CompanyDB;

Create Table Departments(
dept_id INT auto_increment PRIMARY KEY,
dept_name Varchar(50) NOT NULL
);

Create table Employees(
emp_id INT auto_increment Primary Key,
name varchar(50),
age INT,
salary decimal(10,2),
dept_id INT,
foreign key (dept_id) references Departments(dept_id)
);

Insert into Departments(dept_name) values
('IT'),
('HR'),
('Finance'),
('Sales');

INSERT INTO Employees (name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, 3),   -- Finance
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales

TRUNCATE TABLE Employees;
TRUNCATE TABLE Departments;

INSERT INTO Departments (dept_name) VALUES
('IT'),         -- id = 1
('HR'),         -- id = 2
('Finance'),    -- id = 3
('Sales'),      -- id = 4
('Marketing');  -- id = 5  

ALTER TABLE Employees DROP FOREIGN KEY employees_ibfk_1;

INSERT INTO Employees (name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, NULL),-- 
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales

Select e.name, e.salary , d.dept_name
From Employees e
Inner Join Departments d
ON e.dept_id= d.dept_id;

Select e.name, e.salary, d.dept_name from Employees e
Left Join Departments d ON e.dept_id= d.dept_id;

Select e.name, e.salary, d.dept_name from Employees e
Right Join Departments d ON e.dept_id= d.dept_id;

Select e.name, e.salary, d.dept_name from Employees e
Left Join Departments d ON e.dept_id= d.dept_id
UNION
Select e.name, e.salary, d.dept_name from Employees e
Right Join Departments d ON e.dept_id= d.dept_id;





 