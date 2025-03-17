"""
通过pyspark完成以下目标
各个城市销售额排名，从大到小
全部城市，有哪些商品类别在售卖
北京市有哪些商品类别在售卖

"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 生成json数据的RDD类对象
rdd = sc.textFile("C:/DSoftware/pythonfile/Pyrhon_learn/10_Python_大数据基础PySpark/sold.txt")
dict_rdd = rdd.map(lambda x: json.loads(x))

# 计算各个城市的销售额排名，从小到大排序
# 生成新的KV型RDD对象
areaname_money_rdd = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))
# 计算各个城市的销售额排名并输出
city_money_rdd = areaname_money_rdd.reduceByKey(lambda a, b: a + b)     # 分组聚合求和
city_money_sort_rdd = city_money_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)    # 根据V值正序排序
print(f"各个城市的销售额排名为：{city_money_sort_rdd.collect()}")

# 全部城市，有哪些商品类别在售卖
# 将所有商品种类取出并去重
category_rdd = dict_rdd.map(lambda x: x["category"]).distinct()
print("全部在售的商品有：", category_rdd.collect())

# 北京市有哪些商品类别在售卖
# 取出北京市售卖的商品类型并去重
BJ_categoryall_rdd = dict_rdd.filter(lambda x: x["areaName"] == " 北京 ")
BJ_category_rdd = BJ_categoryall_rdd.map(lambda x: x["category"]).distinct()
print("北京售卖的商品有：", BJ_category_rdd.collect())

# 关闭spark
sc.stop()