"""
filter算子
通过特定的函数参数，将RDD中的数据进行过滤操作
函数参数需满足(T) -> bool 为true则保留，为false则舍弃

"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 创建一个RDD对象
rdd = sc.parallelize([("可莉", 90), ("九条裟罗", 80), ("雷电将军", 70), ("阿蕾奇诺", 60), ("芙宁娜", 50), ("班尼特", 40)])

# 通过filter算子筛选出等级大于70的角色
rdd2 = rdd.filter(lambda level: level[1] > 70)
print(rdd2.collect())

# 关闭连结
sc.stop()