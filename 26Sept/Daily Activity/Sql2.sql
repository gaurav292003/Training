Create database emp;
use emp;

create table employee(
	id int auto_increment primary key,
    name varchar(50) not null,
    age int,
    department varchar(50),
    salary Decimal(10,2)
);

insert into employee (name, age,department,salary)
Values
('Dev', 23,'IT', 45000),
('Neha',24,'Sales', 34000),
('Arjun',31,'IT', 70000),
('Priya',27,'Sales',45000);

Select name, department from employee;

Select name, department from employee where salary>50000;

Update employee
Set salary =48000
where id=4;

Delete from employee where id=2;

Select * from employee;



