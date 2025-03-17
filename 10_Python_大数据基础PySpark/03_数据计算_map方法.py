'''

map计算方法

map算子能够接受一个函数，利用该函数对RDD类对象中的所有数据进行处理得到一个新的RDD类对象

函数参数必须满足(T) -> U ，即必须有一个传入参数和一个返回值，类型可以不相等

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
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# 创建一个函数，将数据放大十倍
# def fun1(input: int):
#     return input * 10
#
# # 利用map算子将rdd对象中所有数据进行处理
# rdd2 = rdd.map(fun1)

# 利用匿名函数进行数据处理
# rdd2 = rdd.map(lambda x: x * 10)

# 链式调用
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 9)

# 输出处理后的数据
print(rdd2.collect())

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()