# -*- coding:utf-8 -*-
# @FileName  :format_csv.py
# @Time      :2024/3/12 18:06
# @Author    :Daisy
# @Brief Introduction    : 格式化csv用例报错

import csv
import codecs
import os


def format_csv(input_file, output_file):
    # 参数检查
    if not os.path.exists(input_file):
        print(f"输入文件 {input_file} 不存在")
        return
    if os.path.exists(output_file):
        print(f"输出文件 {output_file} 已存在，将被覆盖")

    try:
        with codecs.open(input_file, 'r', 'gbk') as infile, codecs.open(output_file, 'w', 'utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # 处理文件
            row_count = 0
            for row in reader:
                writer.writerow(row)
                row_count += 1
                if row_count % 1000 == 0:  # 每处理1000行打印一次进度
                    print(f"格式化完成 {row_count} 行")

    except FileNotFoundError:
        print(f"输入文件 {input_file} 未找到")
    except PermissionError:
        print(f"没有足够的权限读取 {input_file} 或写入 {output_file}")
    except (UnicodeDecodeError, UnicodeEncodeError) as e:
        print(f"编码转换错误: {e}")


# 使用示例
input_file = r'C:\Users\Xu\PycharmProjects\pythonProject2\test\红冲乱码.csv'
output_file = r'C:\Users\Xu\PycharmProjects\pythonProject2\test\红冲乱码修复.csv'
format_csv(input_file, output_file)
