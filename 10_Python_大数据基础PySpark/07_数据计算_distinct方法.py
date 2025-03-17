"""
distinct算子
对RDD类对象进行去重操作，无需传入参数

"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 创建一个RDD对象
rdd = sc.parallelize([1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 7, 7, 7])

# 进行去重
rdd2 = rdd.distinct()
print(rdd2.collect())

# 关闭连接
sc.stop()