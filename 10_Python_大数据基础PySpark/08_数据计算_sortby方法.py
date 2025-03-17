"""
sortby算子
对RDD类对象进行排序
rdd.sortby(func, ascending=false, numPartitions)
fun: (T) -> U告知rdd使用那个数据进行排序
ascending: true升序排序，false降序排序
numPartitions： 使用多少分区进行排序
"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 创建一个RDD对象
rdd = sc.parallelize([("可莉", 90), ("九条裟罗", 80), ("雷电将军", 70), ("阿蕾奇诺", 60), ("芙宁娜", 50)])

# 按照等级从大到小进行排序
rdd2 = rdd.sortBy(lambda a: a[1], ascending=True, numPartitions=1)
print(rdd2.collect())

# 关闭连接
sc.stop()