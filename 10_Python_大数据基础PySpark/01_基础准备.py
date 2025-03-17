#导入Spark包
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app") # 链式调用

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf = conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()