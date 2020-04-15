select `firstName`,`lastName`,`email` from `employees`;



select * from `employees` where officeCode=1

select * from `employees` where officeCode=2
select * from `employees` where officeCode=3
select * from `employees` where officeCode=4
select * from `employees` where officeCode=5
select * from `employees` where officeCode=6
select * from `employees` where officeCode=7



-- qn4

select `officeCode`,count(*) from `employees` group by `officeCode`;

--qn4b

select `customerNumber`,avg(`amount`) from `payments` group by `customerNumber`;

--qn4c

select `customerNumber`,avg(`amount`) from `payments` 
group by `customerNumber` 
having avg(`amount`)>10000;

-- qn4d

select `customerNumber`,count(*) from `orders` 
group by `customerNumber`
order by count(*) DESC;

-- qn5


select `firstName`,`lastName`,`email`,`city` from `employees` 
    join `offices` on `employees`.`officeCode` =`offices`.`officeCode`;


--qn5b

select `customers`.`customerNumber`,`country`,avg(`amount`) from `customers` 
    join `payments` on `customers`.`customerNumber` =`payments`.`customerNumber`
    where `country` = 'USA'
    group by `customers`.`customerNumber`
    having avg(`amount`)>10000;

select * from `customers` 
    join `payments` on `customers`.`customerNumber` =`payments`.`customerNumber`
    where `country` = 'USA';

-- qn6

select * from `orders`
where `comments` like '%FedEx%';


-- qn7

select `orders`.`customerNumber`,`customerName`,`orderNumber`,`orderDate` from `orders` 
join `customers` on `orders`.`customerNumber` = `customers`.`customerNumber`
where `orders`.`customerNumber`='124';



--qn8

select `customerNumber`,sum(`amount`) from `payments`
group by `customerNumber`

select `customers`.`customerNumber`,`customerName`,sum(`amount`)  from `customers`
join `payments` on `customers`.`customerNumber` =`payments`.`customerNumber`
group by `customers`.`customerNumber`


--11

select * from `orderdetails`
where `orderNumber` = '10101';

--12

select * from `orders` 
join `orderdetails` on `orders`.`orderNumber` = `orderdetails`.`orderNumber`
where `customerNumber` ='103'
