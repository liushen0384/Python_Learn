"""
序列指内容连续、有序、可以使用下标索引的数据容器
列表、元组、字符串均可视为序列
序列的切片： 从一个序列中，取出一个子序列


"""

# 序列的切片
id = "410923199901297253"
id_br = id[6: 14: 1]
id2 = id[::-2][::-1]
id3 = id[::-1]  #倒叙序列
print(id_br, id2, id3)