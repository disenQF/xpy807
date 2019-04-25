select s.sn, s.name, round(avg(score), 1) as avg_score
from SC
  JOIN Student s on (s.sn = sc.sn)
group by s.sn
HAVING avg(score) >= 60;
-- 聚合某一字段之后结果，作为条件，必须放在having子句中