# 

# 情况说明

查询每门科目的前3名。

对于查询的结果，一般有两种情况。

表所有数据为：

![image-20200830171608567](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/20200830204926.png)

情况1：对于分数相同的人，其后面的人 紧跟着名次排，直到排够名次3，就不再往后取了。

![image-20200830170431328](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200830170431328.png)

情况2：对于分数相同的人，若当前相同名次的人数大于或等于 3， 则相同分数其后面的人不再参于top3了。



![image-20200830170939339](https://cdn.jsdelivr.net/gh/winter60/my_figurebed/data/image-20200830170939339.png)



**在情况2中 ，为什么”李四 - java“ 这行没有了呢？**

可以这样理解，在情况2中相当于使用了**名次空缺**， 分数相同的人其后面那个人，的名次为 **前面的人数+1** ， 这里的 ”李四-java“这行，他的名次应当是 **5** ， 所有top3自然取不到  ”李四-java“这行。

#  # 查询方法

## 情况1方法：

```mysql
# 方法1
SELECT 		T1.*
FROM 		score_t T1
WHERE		(SELECT COUNT(distinct score) FROM score_t WHERE T1.subject = subject AND T1.score < score) < 3
ORDER BY 	subject,score DESC;
-- 思路：
-- 1. 通过子查询的方式 ， 查询每条记录中 对应科目比他分数高的 
-- 2. 如果比自己还高的 小于3 ，那么自己就是属于top3



# 方法2
 SELECT		T1.*
FROM 		score_t T1
LEFT JOIN	(SELECT DISTINCT subject, score FROM score_t) T2
ON 			T1.subject = T2.subject
AND 		T1.score < T2.score
GROUP BY 	name,subject,score
HAVING		COUNT(1) < 3
ORDER BY 	subject,score DESC;

-- 思路：
-- 1. 找到所有科目对应分数的所有情况 （去重）
-- 2. 和原表关联后， 且比当前 记录 对应科目比自己分数
-- 3. 分组后 找出 次数小于3的
-- 注意： 使用 distinct 去重 和不使用， 区别于并列名次 是否算同一个名额

# 方法3
select t.name,t.subject,t.score,t.rank from (
	select name,subject,score,
	@r:= if(@psub = subject, if(@psco = score, @r, @r + 1), 1) rank ,
	@psub:= subject , @psco:= score 
	from score_t, (select @psub:=null, @psco:=null, @r:=0) init
	order by subject,score desc
) t where t.rank <=3;
-- 思路：
-- 使用 临时变量， 相同的分数 保持名次不变，否则+1



# 方法4
select t1.name,t1.subject,t1.score, count(distinct t2.score)  rank from score_t t1 -- 
left join score_t t2
on t1.subject = t2.subject and t2.score >= t1.score
group by t1.subject,t1.name,t1.score
having count(distinct t2.score) <= 3
order by subject,score desc ,rank;
-- 和方法2思路一样 ， 只是使用 写法不同
```



## 情况2方法：

```mysql
# 方法1：  
SELECT 		T1.*
FROM 		score_t T1
WHERE		(SELECT COUNT(1) FROM score_t WHERE T1.subject = subject AND T1.score < score) < 3
ORDER BY 	subject,score DESC;

 

# 方法2    
 SELECT		T1.*
FROM 		score_t T1
LEFT JOIN	(SELECT subject, score FROM score_t) T2
ON 			T1.subject = T2.subject
AND 		T1.score < T2.score

GROUP BY 	name,subject,score
HAVING		COUNT(1) < 3
ORDER BY 	subject,score DESC


# 方法3
select t.name,t.subject,t.score,t.rank from (
	select name,subject,score,
	@allorder:= if(@psub = subject, @allorder + 1, 1),
	@r:= if(@psub = subject, if(@psco = score, @r, @allorder), 1) rank ,	
	@psub:= subject , @psco:= score
	from score_t, (select @psub:=null, @psco:=null, @r:=0, @allorder:=0) init
	order by subject,score desc
) t where t.rank <=3


# 方法4
select t1.name,t1.subject,t1.score  from score_t t1 -- 
left join score_t t2
on t1.subject = t2.subject and t2.score > t1.score
group by t1.subject,t1.name,t1.score
having count(*) <  3
order by subject,score desc 

```

情况2和情况 写法都是对应的， 需要注意的是 并列名次，后面的人 是否需要保持名次空缺。那么统计的时候就需要根据情况去重。

# 数据创建

```mysql
CREATE TABLE score_t(
name 		VARCHAR(10),
subject		VARCHAR(10),
score		INT(10)
);

INSERT INTO score_t VALUES
("张三","java",71),
("李四","java",82),
("王五","java",90),
("赵六","java",98),
("孙七","java",90),
("陈八","java",90),
("张三","python",81),
("李四","python",92),
("王五","python",93),
("赵六","python",97),
("刘九","python",93),
("孙七","python",70);
```

参考链接：

https://blog.csdn.net/weixin_44497013/article/details/107317719

https://leetcode-cn.com/problems/department-top-three-salaries/solution/mysqlzi-ding-yi-bian-liang-shi-xian-fen-lei-pai-xu/

