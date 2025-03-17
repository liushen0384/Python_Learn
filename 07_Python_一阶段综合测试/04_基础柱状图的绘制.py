"""
绘制一个基础折线图

"""
import json
from pyecharts.charts import Bar, Timeline
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
from pyecharts.globals import ThemeType

# 构建一个基础柱状图对象1
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "日本"])  # 添加x轴数据
bar1.add_yaxis("GDP", [20, 30, 20],label_opts=LabelOpts(position="right"))  # 添加y轴数据
bar1.reversal_axis()  # 反转x、y轴

# 构建一个基础柱状图对象2
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "日本"])  # 添加x轴数据
bar2.add_yaxis("GDP", [50, 30, 20],label_opts=LabelOpts(position="right"))  # 添加y轴数据
bar2.reversal_axis()  # 反转x、y轴

# 构建一个基础柱状图对象
bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "日本"])  # 添加x轴数据
bar3.add_yaxis("GDP", [10, 30, 60],label_opts=LabelOpts(position="right"))  # 添加y轴数据
bar3.reversal_axis()  # 反转x、y轴

# 创建一个时间线对象
timel = Timeline({"theme": ThemeType.INFOGRAPHIC})

timel.add(bar1, "1")
timel.add(bar2, "2")
timel.add(bar3, "3")  # 将各个点位的柱状图放入时间线

# 设置自动播放设置
timel.add_schema(
    play_interval=500,  # 播放间隔
    is_timeline_show=True,  # 时间线是否显示
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否轮询
)

# 通过时间线绘图
timel.render("基础时间线柱状图.html")
