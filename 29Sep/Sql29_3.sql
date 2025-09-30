Create Database RetailDB;
Use RetailDb;

Create Table Customers(
customer_id INT auto_increment Primary key,
name varchar(50),
city varchar(50),
phone varchar(15)
);

Create Table Products(
product_id INT auto_increment Primary Key,
product_name varchar(50),
category varchar(50),
price decimal(10,2)
);

Create table Orders(
order_id INT auto_increment Primary Key,
customer_id INT,
order_date Date,
Foreign key (Customer_id) References Customers(customer_id)
);

Create table OrderDetails(
order_detail_id INT auto_increment Primary Key,
order_id INT,
product_id INT,
quantity INT,
foreign key(order_id)references Orders(order_id),
foreign key(product_id) references Products(product_id)
);


INSERT INTO Customers (name, city, phone) VALUES
('Rahul', 'Mumbai', '9876543210'),
('Priya', 'Delhi', '9876501234'),
('Arjun', 'Bengaluru', '9876512345'),
('Neha', 'Hyderabad', '9876523456');


INSERT INTO Products (product_name, category, price) VALUES
('Laptop', 'Electronics', 60000.00),
('Smartphone', 'Electronics', 30000.00),
('Headphones', 'Accessories', 2000.00),
('Shoes', 'Fashion', 3500.00),
('T-Shirt', 'Fashion', 1200.00);


INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03'),
(1, '2025-09-04');


INSERT INTO OrderDetails (order_id, product_id, quantity) VALUES
(1, 1, 1),   -- Rahul bought 1 Laptop
(1, 3, 2),   -- Rahul bought 2 Headphones
(2, 2, 1),   -- Priya bought 1 Smartphone
(3, 4, 1),   -- Arjun bought 1 Shoes
(4, 5, 3);   -- Rahul bought 3 T-Shirts


DELIMITER $$

Create procedure GetAllProducts()
BEGIN
Select product_id, product_name, category, price from products;
END $$

DELIMITER ;

CALL GetAllProducts();


DELIMITER $$
Create procedure GetOrdersWithCustomers()
BEGIN
Select o.order_id, o.order_date, c.name AS customer_name
From Orders o
Join customers c ON o.customer_id=c.customer_id;
END $$
DELIMITER ;

CALL GetOrdersWithCustomers();


/*DELIMITER $$
create procedure GetFullOrderDetail()
BEGIN
Select o.order_id,
c.name as customer_name,
p.product_name,
od.quantity,
p.price,
(od.quantity*p.price)as total
From orders o
Join customers c on o.customer_id=c.customer_id
Join OrderDetails od on o.order_id= od.order_id
Join Products p on od.product_id = p.product_id;
END$$

DELIMITER ;

CALL GetFullOrderDetail();*/


Delimiter $$
create procedure GetCustomer_Order(IN cust_id INT)
BEGIN
Select o.order_id,
o.order_date,
p.product_name,
od.quantity,
p.price,
(od.quantity*p.price) AS total
From Orders o
Join OrderDetails od ON o.order_id=od.order_id
Join Products p ON od.product_id= p.product_id
where o.customer_id=cust_id;
END
Delimiter ;

Call GetCustomer_Order(1);
