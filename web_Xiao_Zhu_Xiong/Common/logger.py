import logging
from logging.handlers import RotatingFileHandler
import os
import time
from Common import dir_config

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{}.log".format(curTime),backupCount=20,encoding='utf-8')

#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_2])

logging.info("开始记录日志")