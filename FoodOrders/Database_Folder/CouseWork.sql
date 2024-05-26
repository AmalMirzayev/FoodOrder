CREATE DATABASE IF NOT EXISTS course;
USE course;
-- course.card definition

CREATE TABLE IF NOT EXISTS `card` (
  `ID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `card_number` varchar(100) NOT NULL,
  `expiration` varchar(100) NOT NULL,
  `cvc` varchar(100) NOT NULL,
  `holder` varchar(100) NOT NULL,
  `balance` float NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- course.menu definition

CREATE TABLE  IF NOT EXISTS `menu` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `restaurant_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `available` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- course.restaurant definition

CREATE TABLE  IF NOT EXISTS `restaurant` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `available` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;