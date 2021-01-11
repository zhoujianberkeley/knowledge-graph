# step 1：导包
from py2neo import Graph, Node, Relationship

# step 2：构建图
g = Graph("http://localhost:7474",auth=("neo4j","xiaojianbao1996"))
# step 3：创建节点
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
# step 4：创建边
ab = Relationship(a, "KNOWS", b)
# step 5：运行
tx.create(ab)
tx.commit()
