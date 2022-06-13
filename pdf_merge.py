import os
from PyPDF2 import PdfFileMerger

file_merger = PdfFileMerger()

# 循环查找当前目录
for i in os.listdir('.'):
    # 过滤文件，判断以.pdf结尾的文件
    if i.endswith('.pdf'):
        # 合并pdf文件
        file_merger.append(i)

# 保存最终合并的pdf文件
file_merger.write('1.pdf')
