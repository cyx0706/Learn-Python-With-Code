# -*- coding:utf-8 -*-

# 配置文件
import os

# 测评结果输出文件(默认当前文件夹)
output_file = os.path.join(os.getcwd(), "out.txt")

# 标准答案测试文件夹路径(默认当前文件夹下的 “standard_answer_files”)
standard_answer_files_path = os.path.join(os.getcwd(), "standard_answer_files")

# 标准答案测试文件
standard_answer_files = {
    # key:问题的输入 value:标答输出
    "q1": {"q1_1.txt": "q1_1_out.txt", "q1_2.txt": "q1_2_out.txt"},
    "q2": {"q2_1.txt": "q2_1_out.txt"},
    "q3": {"q3_1.txt": "q3_1_out.txt"},
    "q4": {"q4_1.txt": "q4_1_out.txt"},
    "q5": {"q5_1.txt": "q5_1_out.txt", "q5_2.txt": "q5_2_out.txt"},
    "q6": {"q6_1.txt": "q6_1_out.txt"},
}

# 提交程序文件所在文件夹
raw_answer_files_path = os.path.join(os.getcwd(), "raw_answer_files")

# 格式 "name": ["q1.py", "q2.py", "q3.py"...]
# 注意和上面对应
raw_answer_files = {
    # key:提交人名, value:{题目: 答案的 py 文件}
    "小A": {
        "q1": "q1.py",
        "q2": "q2.py",
        "q3": "q3.py"
    },
    "小B": {
        "q1": "q1.py",
        "q2": "q2.py",
        "q3": "q3.py",
        "q4": "q4.py",
        "q5": "q5.py",
        "q6": "q6.py"
    },
}

if __name__ == "__main__":
    print(output_file)
    print(raw_answer_files_path)
    print(standard_answer_files_path)