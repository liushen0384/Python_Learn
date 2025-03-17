"""
生成全国疫情地图

"""

# 模块调用
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
from pyecharts.globals import ThemeType

# 获取数据
f_cn = open("C:/DSoftware/Python/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
cn_data = f_cn.read()
f_cn.close()

# 将json数据转换为字典
cn_dict_data = json.loads(cn_data)

# 取出各省份感染人数数据
cn_ares_data = cn_dict_data["areaTree"][0]["children"]

data = []
for i in cn_ares_data:
    data.append((i["name"] + "省", i["total"]["confirm"]))


# 生成地图对象
map = Map()

# 准备数据
# data = [
#     ("上海市", 199),
#     ("河南省", 299),
#     ("河北省", 10099),
#     ("山东省", 499),
#     ("浙江省", 599),
#     ("黑龙江省", 1980)
# ]

# 添加数据
map.add("全国疫情地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,   # 是否展示
        is_piecewise=True,   # 是否显示标签
        pieces=[
            {"min": 1, "max": 9, "lable": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "lable": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "lable": "100-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "lable": "500-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "lable": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "lable": "10000人以上", "color": "#990033"}
        ]  # 标签格式设置
    )
)

# 生成地图
map.render("全国疫情地图.html")