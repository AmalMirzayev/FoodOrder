CREATE DATABASE IF NOT EXISTS courses;
USE courses;

CREATE TABLE IF NOT EXISTS Courses.card (
	ID BIGINT UNSIGNED auto_increment NOT NULL,
	card_number varchar(100) NOT NULL,
	expiration varchar(100) NOT NULL,
	cvc varchar(100) NOT NULL,
	holder varchar(100) NOT NULL,
	balance FLOAT NOT NULL,
	CONSTRAINT card_pk PRIMARY KEY (ID)
)
CREATE TABLE IF NOT EXISTS courses.menu (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	restaurant_id varchar(100) NOT NULL,
	name varchar(100) NOT NULL,
	price varchar(100) NOT NULL,
	available INT NOT NULL,
	CONSTRAINT menu_pk PRIMARY KEY (id)
)
CREATE TABLE IF NOT EXISTS courses.restaurant (
	id BIGINT UNSIGNED auto_increment NOT NULL,
	Name varchar(100) NOT NULL,
	City varchar(100) NOT NULL,
	available BOOL NOT NULL,
	CONSTRAINT restaurant_pk PRIMARY KEY (id)
)


