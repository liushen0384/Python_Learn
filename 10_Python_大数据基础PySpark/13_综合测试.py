"""
读取文件转换成 RDD ，并完成：
打印输出：热门搜索时间段（小时精度） Top3
打印输出：热门搜索词 Top3
打印输出：统计黑马程序员关键字在哪个时段被搜索最多
将数据转换为 JSON 格式

"""

# 导入Spark包，为Spark指定python程序位置，创建SparkContext对象
from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = "C:/Users/86185/AppData/Local/Programs/Python/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")     # 链式调用
sc = SparkContext(conf = conf)

# 取出数据
rdd = sc.textFile("C:/DSoftware/pythonfile/Python_learn/10_Python_大数据基础PySpark/search_log.txt")

# 打印输出：热门搜索时间段（小时精度） Top3
hottime_rdd = rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda a: a[1], ascending=False).\
    take(3)
print(hottime_rdd)

# 打印输出：热门搜索词 Top3
hotword_rdd = rdd.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda a: a[1], ascending=False).\
    take(3)
print(hotword_rdd)

# 打印输出：统计黑马程序员关键字在哪个时段被搜索最多
heima_hottime_rdd = rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2] == "黑马程序员").\
    map(lambda x: (x[0][0:2:1], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda a: a[1], ascending=False).\
    take(1)
print(heima_hottime_rdd)

# 将数据转换为 JSON 格式
def tr_json(list_data: list)-> dict:
    dic1 = {}
    dic1["时间"] = list_data[0]
    dic1["用户ID"] = list_data[1]
    dic1["关键词"] = list_data[2]
    dic1["未知1"] = list_data[3]
    dic1["未知2"] = list_data[4]
    dic1["网址"] = list_data[5]
    return dic1

json_list = rdd.map(lambda x: x.split("\t")).map(tr_json).take(3)
print(json_list)

# 关闭spark
sc.stop()