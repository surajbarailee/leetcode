# Write your MySQL query statement below
SELECT max(Salary) as SecondHighestSalary from Employee 
where Salary NOT IN (SELECT max(Salary) from Employee)