# 小易喜欢的单词具有以下特性：
# 
# 1.单词每个字母都是大写字母
# 2.单词没有连续相等的字母
# 3.单词没有形如“xyxy”(这里的x，y指的都是字母，并且可以相同)这样的子序列，子序列可能不连续。
# 
# 例如：
# 小易不喜欢"ABBA"，因为这里有两个连续的'B'
# 小易不喜欢"THETXH"，因为这里包含子序列"THTH"
# 小易不喜欢"ABACADA"，因为这里包含子序列"AAAA"
# 小易喜欢"A","ABA"和"ABCBA"这些单词
# 
# 给你一个单词，你要回答小易是否会喜欢这个单词

import re

if __name__ == "__main__":

    # 正则
    re_1 = re.compile(r"[^A-Z]+")
    re_2 = re.compile(r"([A-Z])\1")
    re_3 = re.compile(r"([A-Z])[A-Z]*([A-Z])[A-Z]*\1[A-Z]*\2")
    # 输入
    abc = input('输入单词:')
    # 判断
    if re_1.search(abc) or re_2.search(abc) or re_3.search(abc):
        print("小明不喜欢")
    else:
        print("小明喜欢")
