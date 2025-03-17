"""
将RDD类对象转换为Python数据对象
collect算子： 将RDD对象内的数据全部转换为list对象

reduce算子： 将RDD对象的所有数据按照函数参数进行聚合，满足(T, T) -> T

take算子： 将RDD对象中的前n个数据取出

count算子： 计算RDD对象中有多少个元素

"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 准备一个RDD类对象
rdd = sc.parallelize([1, 2, 3])

# 将RDD对象转换为list
rdd_list = rdd.collect()
print(rdd_list, type(rdd))

# 将rdd对象内容进行累加
rdd_add = rdd.reduce(lambda a, b: a + b)
print(rdd_add)

# 取出RDD中的前两个数据
rdd_2 = rdd.take(2)
print(rdd_2)

#计算RDD对象中有多少个元素
rdd_n = rdd.count()
print(rdd_n)