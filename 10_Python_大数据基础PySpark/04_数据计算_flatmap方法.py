'''

flatmap计算方法

flatmap算子就是在map算子的基础上增加了一个解除嵌套的功能

'''

#导入Spark包
from pyspark import SparkConf, SparkContext

# 为Spark指定python程序位置
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"

# 创建SparkContext对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") # 链式调用
sc = SparkContext(conf = conf)

# 创建一个RDD对象
rdd = sc.parallelize(['keli 90', 'zhongli 90', "hutao 00"])

# 通过map方法处理数据，会得到三个列表数据
# rdd2 = rdd.map(lambda x: x.split(" "))
# print(rdd2.collect())

# 通过flatmap算子处理
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()