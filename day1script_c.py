# nodes.csv需要指定唯一ID和nam,
headers = [
    'unique_id:ID',  # 图数据库中节点存储的唯一标识
    'name',  # 节点展示的名称
    'node_type:LABEL',  # 节点的类型，比如Person和Location
    'property'  # 节点的其他属性
]

# relations.csv
headers = [
    'unique_id',  # 图数据库中关系存储的唯一标识
    'begin_node_id:START_ID',  # begin_node和end_node的值来自于nodes.csv中节点
    'end_node_id:END_ID',
    'begin_node_name',
    'end_node_name',
    'begin_node_type',
    'end_node_type',
    'relation_type:TYPE',  # 关系的类型，比如Friends和Married
    'property'  # 关系的其他属性
]