"""
reducebykey算子
是针对KV（二元元组）型RDD类对象，自动按照key分组，然后根据提供的聚合逻辑，完成组内数据的聚合操作

传入函数参数需要满足(V,V) -> V

"""

#导入Spark包
from pyspark import SparkConf, SparkContext

# 为Spark指定python程序位置
import os
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"

# 创建SparkContext对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") # 链式调用
sc = SparkContext(conf = conf)

# 创建RDD类对象
rdd = sc.parallelize([("liushen", 2) , ("liushen", 3) , ("shihao", 4), ("shihao", 8), ("liushen", 9)])

# 求柳神和十号的的得分总值
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())

# 关闭连结
sc.stop()
