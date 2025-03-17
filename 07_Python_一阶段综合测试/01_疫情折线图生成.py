"""
生成中美日三国的疫情折线图

"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts


# 读取美国数据
f_us = open("C:/DSoftware/Python/资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_date = f_us.read()
# 去掉不符合规范的开头
us_date = us_date.replace("jsonp_1629344292311_69436(", "")
# 去掉不符合规范的结尾
us_date = us_date[:-2]
# json转换为字典
dict_us = json.loads(us_date)
# 取出字典中的trend元素
trend_us = dict_us["data"][0]["trend"]
# 获取x轴日期数据,到2020年结束
us_x_date = trend_us["updateDate"][:314]
# 获取y轴数据，每日确诊人数
us_y_date = trend_us["list"][0]["data"][:314]

# 获取日本数据
f_jp = open("C:/DSoftware/Python/资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_date = f_jp.read()
# 去掉不符合规范的开头
jp_date = jp_date.replace("jsonp_1629350871167_29498(", "")
# 去掉不符合规范的结尾
jp_date = jp_date[:-2]
# json转换为字典
dict_jp = json.loads(jp_date)
# 取出字典中的trend元素
trend_jp = dict_jp["data"][0]["trend"]
# 获取x轴日期数据,到2020年结束
jp_x_date = trend_jp["updateDate"][:314]
# 获取y轴数据，每日确诊人数
jp_y_date = trend_jp["list"][0]["data"][:314]

# 获取印度数据
f_id = open("C:/DSoftware/Python/资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
id_date = f_id.read()
# 去掉不符合规范的开头
id_date = id_date.replace("jsonp_1629350745930_63180(", "")
# 去掉不符合规范的结尾
id_date = id_date[:-2]
# json转换为字典
dict_id = json.loads(id_date)
# 取出字典中的trend元素
trend_id = dict_id["data"][0]["trend"]
# 获取x轴日期数据,到2020年结束
id_x_date = trend_id["updateDate"][:314]
# 获取y轴数据，每日确诊人数
id_y_date = trend_id["list"][0]["data"][:314]

# 生成图表
# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴数据
line.add_xaxis(id_x_date)
# 给折线图对象添加y轴数据
line.add_yaxis("美国确诊人数", us_y_date)
line.add_yaxis("日本确诊人数", jp_y_date)
line.add_yaxis("印度确诊人数", id_y_date)


line.set_global_opts(
    title_opts=TitleOpts(title="美日印新冠确诊人数折线图", pos_left="center", pos_bottom="1%")
)
line.set_series_opts(
    label_opts=LabelOpts(is_show=False)
)

# 关闭文件
f_id.close()
f_jp.close()
f_us.close()

# 生成表格
line.render("美日印新冠确诊人数折线图.html")

