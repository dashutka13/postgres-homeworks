-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id varchar(100) NOT NULL PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100) NOT NULL,
	employee_id int,
	order_date date,
	ship_city varchar(100) NOT NULL
);
