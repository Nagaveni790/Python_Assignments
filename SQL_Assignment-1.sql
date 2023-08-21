#Q1 Create linked in database and ATS table with Columns ID and Technology and List the IDs which possesses 
#mentioned skill 

create database linkedin;

use linkedin

Create table ATS(id int,technology varchar(20));

insert into ATS values(1,"SQL"),(1,"DS"),(1,"Tableau"),(1,"python"),(2,"python"),(2,"R");


#DS,SQL and python
Select id from ATS where technology in ("SQL","DS","Python"); 


#List the unique IDs which possesses mentioned skills

select id from ATS where technology = "SQL"
and id in (
select id from ATS where technology = "python"
and id in (
select id from ATS where technology = "DS"
)); 





#Q2.Create a database EcommerceWeb and table product_info with columns as Product_ID and Product_Name
#and second table Product_Info_Table with columns as User_ID, Product_ID and Liked_Date and write a query to return IDS of 
#the product_info that have 0 likes in product_info_likes table


Create database ecom;

create table product_info1(PrID int, Pro_name varchar(30));

create table product_info_likes(user_id int, PID int, like_date date);

insert into product_info1 values(1001,"Blog"),(1002,"Youtube"),(1003,"Education");

select * from product_info1;

insert into product_info_likes values(1,1001,'2023-08-19'),(1,1003,'2023-08-18');

select * from product_info_likes;


#Returns the product_id with 0 likes in product_info_likes table
SELECT PrID
FROM product_info1 pi
LEFT JOIN  product_info_likes pil 
ON pi.PrID = pil.PID 
Group By pi.PrID 
Having count(pil.PID) = 0;


