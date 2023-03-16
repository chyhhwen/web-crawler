drop database if exists stock;
create database stock default character set utf8 collate utf8_general_ci;
grant all on stock.* to 'staff'@'localhost' identified by 'password';
use stock;
CREATE TABLE data
(
    id int AUTO_INCREMENT PRIMARY KEY,
    sid varchar(255) not null,
    name varchar(255) not null,
    price varchar(255) not null,
    time varchar(255) not null
);

