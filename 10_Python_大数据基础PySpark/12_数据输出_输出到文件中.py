"""
将RDD类对象输出到文件中


"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 准备一个RDD对象
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])