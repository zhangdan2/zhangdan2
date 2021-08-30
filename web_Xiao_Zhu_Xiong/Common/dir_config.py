import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

logs_dir =  os.path.join(base_dir,"Outputs/logs")

baogao_dir =  os.path.join(base_dir,"Outputs/reports")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")