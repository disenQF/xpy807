-- 18、查询各科成绩最高分、最低分和平均分：
-- 以如下形式显示：课程ID，课程name，最高分，最低分，平均分，
--        及格率，中等率，优良率，优秀率
--       及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90

SELECT cn, max(score), min(score), avg(score) from sc
GROUP BY cn;

select sn, cn, score,
       CASE score WHEN 80 then '优'
                  WHEN 90 then '特优'
                  ELSE '一般' end level
from sc;

select a.cn, c.name,
  max(a.score) max_sc,
  min(a.score) min_sc,
  avg(a.score) avg_sc,
  sum(a.s1)/count(a.sn)   s1_rate,
  sum(a.s2)/count(a.sn)   s2_rate,
  sum(a.s3)/count(a.sn)   s3_rate,
  sum(a.s4)/count(a.sn)   s4_rate
from
  (SELECT sn, cn, score,
         CASE WHEN score >= 60 THEN 1 ELSE 0 end s1,
         CASE WHEN score >= 70 and score < 80  THEN 1 ELSE 0 end s2,
         if(score >=80 and score <90, 1, 0) s3,
         if(score >=90,1, 0) s4
  from SC ) a
  JOIN Course c on (c.cn = a.cn)
GROUP BY a.cn, c.name;


SELECT * from student
WHERE
month(age) = '12';

