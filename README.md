# knowledge-graph

# Day 1 打卡
第一次接触到了图数据库neo4j及其操作语言Cypher
感觉Cypher的语言风格似乎有点类似SQL（bushi

同时使用了批量导入了数据 \
bin/neo4j-admin import --nodes=import/nodes.csv --relationships=import/relations.csv   --delimiter=^ --database=jian.db

# Day 2 打卡
今天尝试把数据导入neo4j -- 一个3.7 MB的csv file竟然需要3.2小时，真的蛮惊讶的！

同时尝试使用了现成的代码来做knowledge query，对兔数据库的结构/数据导入和使用有了基本的了解。

# Day 3 打卡
今天就是把昨天的代码都详细讲解了一下，但是这些代码都没有注释，感觉增加了
大家的学习难度

# Task 4 (Day 4 and 5) 打卡
本部分是 how to understand a human user's query?
first, extract entity from the query -- 使用了AC tree来直接匹配实体，如果未能匹配成功，则寻找一个近似的实体。
"近似"是由 相同字符的个数 + 余弦相似度定义的。

second, 意图识别，特征是由TF-IDF表示，而意图则用naive bayes 来分类，where the prior is 
multi-nominal distriubution estimated by MLE。
 

# Task 5 (Day 6 and 7) 打卡
介绍了Cypher, which is a declaretive language similar to SQL. 
Python based knowledge-answer is to translate a human query into a Cypher query and 
then return the query results

