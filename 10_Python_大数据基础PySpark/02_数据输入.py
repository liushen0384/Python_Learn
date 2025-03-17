'''

Spark数据输入

'''

# Pyspark支持多种数据的输入，输入完成后会的到一个RDD类对象（弹性分布式数据集 Resilient Distributed Datasets）
# PySpark处理数据都是以RDD对象为载体

# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") # 链式调用

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf = conf)

# 通过parallelize方法将python对象加载到spark内成为RDD对象
# rdd1 = sc.parallelize([1,2,3,4,5,6])
# rdd2 = sc.parallelize((1,2,3,4,5,6))
# rdd3 = sc.parallelize({1,2,3,4,5,6})
# rdd4 = sc.parallelize("123456")
# rdd5 = sc.parallelize({"kry1": 1, "key2": 2})

# 查看RDD类对象中的数据内容，使用collection()方法
# print(rdd1.collect() , rdd2.collect(), rdd3.collect(), rdd4.collect(), rdd5.collect())

#通过textFlie方法，将文件中的数据读取到RDD类对象中
rdd = sc.textFile("C:\DSoftware\pythonfile\helloworld.txt")
print(rdd.collect())

# 关闭Spark
sc.stop()