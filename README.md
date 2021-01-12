# knowledge-graph

# Day 1 打卡
第一次接触到了图数据库neo4j及其操作语言Cypher
感觉Cypher的语言风格似乎有点类似SQL（bushi

同时使用了批量导入了数据 \
bin/neo4j-admin import --nodes=import/nodes.csv --relationships=import/relations.csv   --delimiter=^ --database=jian.db

# Day 2 打卡
今天尝试把数据导入neo4j -- 一个3.7 MB的csv file竟然需要3.2小时，真的蛮惊讶的！

同时尝试使用了现成的代码来做knowledge query，对兔数据库的结构/数据导入和使用有了基本的了解。
