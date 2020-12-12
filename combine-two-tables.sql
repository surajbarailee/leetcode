# Write your MySQL query statement below
select p.FirstName, p.LastName, addr.city, addr.state
from person p
left join address addr
on p.personid = addr.personid