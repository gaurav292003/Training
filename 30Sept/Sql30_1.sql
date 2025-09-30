Create database if not exists RetailNF;
Use RetailNF;

Create Table BadOrders(
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT,
customer_name VARCHAR(50),
customer_city VARCHAR(50),

products_ids VARCHAR(200),
products_names VARCHAR(200),
unit_prices VARCHAR(200),
quantities VARCHAR(200),
order_total DECIMAL(10,2)
);

INSERT INTO BadOrders VALUES
-- order_id, date, cust, name, city,     pids,      pnames,                   prices,        qtys,    total
(101, '2025-09-01', 1, 'Rahul', 'Mumbai', '1,3',    'Laptop,Headphones',      '60000,2000',  '1,2',   64000.00),
(102, '2025-09-02', 2, 'Priya', 'Delhi',  '2',      'Smartphone',             '30000',       '1',     30000.00);


Create Table Orders_1NF(
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT,
customer_name VARCHAR(50),
customer_city VARCHAR(50)
);

Create Table OrderItems_1NF(
order_id INT,
line_no INT,
product_id INT,
product_name VARCHAR(50),
unit_price DECIMAL(10,2),
quantity INT,
Primary KEY(order_id, line_no),
foreign key(order_id) references Orders_1NF(order_id)
);

Insert into Orders_1NF
Select order_id, order_date, customer_id, customer_name, customer_city FROM BadOrders;


Insert Into OrderItems_1NF VALUES
(101,1,1,'Laptop', 60000,1),
(101,2,3,'Headphones',2000,2);

Insert Into OrderItems_1NF VALUES
(102,1,2,'Smartphone', 3000,1);

Create Table Customers_2NF(
customer_id INT primary key,
customer_name VARCHAR(50),
customer_city VARCHAR(50)
);

Create Table Orders_2NF(
order_id INT primary key,
order_date DATE,
customer_id INT,
foreign key (customer_id) references Customers_2NF(customer_id)
);

Create Table Products_2NF(
product_id INT primary key,
product_name VARCHAR(50),
category VARCHAR(50),
list_price DECIMAL(10,2)
);

CREATE TABLE OrderItems_2NF (
  order_id INT,
  line_no INT,
  product_id INT,
  unit_price_at_sale DECIMAL(10,2),  -- historical price
  quantity INT,
  PRIMARY KEY (order_id, line_no),
  FOREIGN KEY (order_id) REFERENCES Orders_2NF(order_id),
  FOREIGN KEY (product_id) REFERENCES Products_2NF(product_id)
);

-- Seed dimension tables (from what we saw in BadOrders/OrderItems_1NF)
INSERT INTO Customers_2NF VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi');
 
INSERT INTO Products_2NF VALUES
(1, 'Laptop',     'Electronics', 60000),
(2, 'Smartphone', 'Electronics', 30000),
(3, 'Headphones', 'Accessories',  2000);
 
INSERT INTO Orders_2NF VALUES
(101, '2025-09-01', 1),
(102, '2025-09-02', 2);
 
INSERT INTO OrderItems_2NF VALUES
(101, 1, 1, 60000, 1),
(101, 2, 3,  2000, 2),
(102, 1, 2, 30000, 1);

Create table Cities(
city_id INT primary key,
city_name Varchar(50),
state varchar(50)
);

Create Table Customers_3NF(
customer_id INT primary key,
customer_name varchar(50),
city_id INT,
foreign key (city_id) references Cities(city_id)
);


Create table Products_3NF LIKE Products_2NF;
Insert into Products_3NF Select * from Products_2NF;

Create table Orders_3NF LIKE Orders_2NF;
Create table OrderItems_3NF LIKE OrderItems_2NF;

Insert into Cities Values
(10,'Mumbai','Maharashtra'),
(20,'Delhi','Delhi');

Insert into Customers_3NF Values
(1,'Rahul', 10),
(2,'Priya', 20);


Insert into Orders_3NF Select * from Orders_2NF;
Insert into OrderItems_3NF Select * from OrderItems_2NF;






