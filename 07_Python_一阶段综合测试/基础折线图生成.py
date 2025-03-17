"""
生成一个基础折线图
set_global_opts方法进行全局配置，可以更改图例等等配置
"""

# 导入pyecharts包
from pyecharts.charts import Line
# 导入配置包
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()

# 给折线图对象添加x轴数据
line.add_xaxis(["柳神", "石昊", "打神石"])

# 给折线图对象添加y轴数据
line.add_yaxis("GDP", [50, 60, 70])

# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="完美世界等级表", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成折线图
line.render()