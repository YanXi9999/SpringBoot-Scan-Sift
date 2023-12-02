import argparse
import subprocess

def process_file(output_file):
    with open('tmp.txt', 'r',encoding='ansi') as file:
        lines = file.read().split('\n')
        #del lines[-1]
    j = 1
    while j < len(lines) - 1:
        
        if '页面长度为:' in lines[j] and '页面长度为:' in lines[j + 1 ]:
            # 解析冒号后的数字
            colon_index_first = lines[j].index('页面长度为:')
            first = lines[j][colon_index_first + 6:colon_index_first + 10].strip()
            colon_index_second = lines[j + 1].index('页面长度为:')
            second = lines[j + 1][colon_index_second + 6:colon_index_second + 10].strip()   

            while first == second  :
             del lines[j + 1]
             
             if '页面长度为' in lines[j+1] :
                colon_index_second = lines[j + 1].index('页面长度为:')
                second = lines[j + 1][colon_index_second + 6:colon_index_second + 10].strip()
             else :
                break
             if first != second :
                del lines[j]     
                j = j - 1
             if j == len(lines)-1 :
                  break

        j = j + 1
    with open(output_file, 'w') as file:
         for line in lines:
             file.write(line + '\n')



if __name__ == '__main__':
# 创建参数解析器
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", help="需要批量扫描url的txt文件")
    parser.add_argument("-p", "--python_version",default='python3', help="需要执行的python解释器")
    parser.add_argument("-o", "--output_file", help="筛选后输出的文件名")
    args = parser.parse_args()

# 获取输入和输出文件名
    input_file = args.input_file
    output_file = args.output_file
    python_version= args.python_version
# 检查文件名是否为空
    if input_file is None or output_file is None:
        print("请输入正确的文件名！")
        exit()
        
    with open("tmp.txt", "w",encoding="utf-8") as file:
    # 将文件内容清空
        file.truncate(0)

# 处理文件的逻辑
# 在这里添加你的代码逻辑，据输入文件和输出文件进行相应的处理
# 以下是一个示例，将输入文件内容复制到文件中
    cmd_command = '{} SpringBoot-Scan.py -f {} | findstr "信息泄露" > tmp.txt '.format(python_version,input_file)
    subprocess.run(cmd_command, shell=True)
    process_file(output_file)