"""
绘制一个动态柱状图


"""
import json
from pyecharts.charts import Bar, Timeline
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
from pyecharts.globals import ThemeType

# 获取数据
f = open("C:/DSoftware/Python/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data = f.readlines()
f.close()

# 删除无用数据
data.pop(0)

# 将数据分隔，每年的数据为一组
data_year = {}  # 创建字典
for i in data:
    year = int(i.split(",")[0])  # 年份
    country = i.split(",")[1]  # 国家
    gdp = float(i.split(",")[2])  # float可以将科学计数法的字符串正确转换为数字
    try:
        data_year[year].append([country, gdp])
    except Exception:
        data_year[year] = [[country, gdp]]       # data_year[year]为空时会报错

# 取出字典中所有的key
keys = sorted(data_year.keys())

# 创建时间线
line = Timeline({"theme": ThemeType.INFOGRAPHIC})

# 根据年份绘制柱状图并放入时间线中
for year in keys:
    s = data_year[year]   # 取出对应年份的数据
    # 排序，基于匿名函数lambda
    s.sort(key=lambda cou: cou[1], reverse=True)  # 将数据按照gdp高低进行排序
    s = s[:8]  # 取出gdp前八的数据
    x_data = []
    y_data = []
    for j in s:
        x_data.append(j[0])
        y_data.append(j[1]/100000000)  # 构建x、y轴数据列表

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()  # 改变列表显示顺序
    bar.add_xaxis(x_data)  # 添加x轴数据
    bar.add_yaxis("GDP(亿)元", y_data, label_opts=LabelOpts(position="right"))  # 添加y轴数据
    bar.reversal_axis() # 反转x、y轴
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP排行")  # 为每年的柱状图添加标题
    )

    # 将柱状图放入时间线
    line.add(bar, str(year))
    # 设置自动播放以及播放间隔
    line.add_schema(
        play_interval=500,
        is_timeline_show=True,
        is_auto_play=True,
        is_loop_play=True
    )

# 生成时间线柱状图并设置标题
line.render("全球GDP前8国家.html")

