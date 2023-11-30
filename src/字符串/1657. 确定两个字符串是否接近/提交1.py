from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 字符串长度不同无法靠替换转换
        if len(word2) != len(word1):
            return False
        # 构建2个字符集的哈希表
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        # 如果字符集相同，能只靠操作1进行转换完成
        if counter1 == counter2:
            return True
        # 如果包含字符不同，返回False
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        # 检查相同频次字符数量
        return Counter(counter1.values()) == Counter(counter2.values())

# 题目描述：
# 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串接近 ：
# 操作 1：交换任意两个 现有 字符。
# 例如，abcde -> aecdb
# 操作 2：将一个现有字符的每次出现转换为另一个现有字符，并对另一个字符执行相同的操作。
# 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
# 你可以根据需要对任意一个字符串多次使用这两种操作。
# 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。