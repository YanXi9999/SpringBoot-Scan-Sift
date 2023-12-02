# SpringBoot-Scan-Sift
SpringBoot-Scan的筛选脚本

在使用SpringBoot-Scan批量扫描时，经常会由于网站的容错处理等原因导致有很多误报  
此工具用于排除可能存在误报的网站  
使用说明：  

  -h, --help                 show this help message and exit  
  -f INPUT_FILE, --input_file INPUT_FILE  
                        需要批量扫描url的txt文件  
  -p PYTHON_VERSION, --python_version PYTHON_VERSION  
                        需要执行的python解释器  
  -o OUTPUT_FILE, --output_file OUTPUT_FILE  
                        筛选后输出的文件名    
  -p为选择需要执行的python解释器，因为很多人习惯改为python310等格式，如没有修改则为python。此选项默认为python3    
  -f为选择SpringBoot-Scan扫描后得到的文件    
 需要安装库：subprocess argparse
