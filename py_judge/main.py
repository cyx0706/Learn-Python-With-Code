# -*- coding:utf-8 -*-

import subprocess
import os
import config

# import psutil


class LocalTest:
    """
    执行测试
    """
    def __init__(self):
        self.raw_answer_files_path = config.raw_answer_files_path
        self.standard_answer_files_path = config.standard_answer_files_path
        self.output_file = config.output_file
        self.standard_answer_files = config.standard_answer_files
        self.raw_answer_files = config.raw_answer_files

    def start(self):
        output_fp = open(self.output_file, 'w', encoding='utf-8', newline="\n")
        for name in self.raw_answer_files:

            output_fp.write(name + "开始测试\n")
            print("测试 " + name)
            raw_answers = self.raw_answer_files[name]  # raw_answers 存储待测文件
            temp = os.path.join(self.raw_answer_files_path, name)
            for q in raw_answers:
                output_fp.write("测试" + q + "\n")
                print("测试 " + q)
                # q 为题目的编号
                # 循环遍历测试每个标准输入和标准输出
                for std_in_file in self.standard_answer_files[q]:
                    # 拼接得到题目路径
                    q_path = os.path.join(self.standard_answer_files_path, q)

                    standard_input = open(os.path.join(q_path, std_in_file))
                    output_fp.write("标准输入:\n" + standard_input.read())
                    # 重新指回文件开始
                    standard_input.seek(0)
                    standard_output = open(os.path.join(q_path, self.standard_answer_files[q][std_in_file]),
                                           encoding="utf-8")
                    std_out_string = standard_output.read()  # 从文件读取完后保存为变量便于重复使用
                    output_fp.write("标准输出:\n" + std_out_string + "\n")

                    # 调用 shell 命令执行
                    child_proc = subprocess.Popen("python {}".format(os.path.join(temp, raw_answers[q])),
                                                  stdin=standard_input,
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.PIPE)
                    # print("pid:", child_proc.pid)
                    # 可以通过 pid 用 psutil 来查内存
                    # 获取输出
                    # 主线程等待子线程的完成, 此时会阻塞主线程
                    try:
                        # 获取输出通过 PIPE
                        shell_out_raw = child_proc.communicate(timeout=5)
                        shell_out = shell_out_raw[0].decode("utf-8")
                        shell_err = shell_out_raw[1].decode("utf-8")
                    except Exception as e:
                        print("TimeOut", e)
                        output_fp.write("超出5s时限\n")
                    else:

                        if child_proc.returncode != 0:
                            output_fp.write("程序出错\n")
                            output_fp.write(shell_err)
                        else:
                            # 删除最后的输出换行符\n和\r
                            shell_out = shell_out.rstrip('\n')
                            shell_out = shell_out.rstrip('\r')
                            output_fp.write("作答输出:\n" + shell_out + "\n")
                            if shell_out == std_out_string:
                                output_fp.write("通过\n")
                            else:
                                # 删去所有的换行符和空格再次比较
                                shell_out = shell_out.replace('\n', '').replace('\r', '').replace(' ', '')
                                std_out_string = std_out_string.replace('\n', '').replace(' ', '')
                                if shell_out == std_out_string:
                                    output_fp.write("格式错误 ")
                                else:
                                    pass
                                output_fp.write("未通过\n")
                    output_fp.write("\n")
                    output_fp.flush()  # 清空输出缓冲区立即写入文件
                    standard_output.close()
                    standard_input.close()
                    print(name + " 测试完成" + std_in_file)
        # 关闭文件指针
        output_fp.close()


if __name__ == "__main__":
    lt = LocalTest()
    lt.start()
