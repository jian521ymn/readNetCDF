#!/usr/bin/python3
# encoding:utf-8
import flask,json
from netCDF4 import Dataset
import numpy 
import json
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__) 
 
# 'index'是接口路径，methods不写，默认get请求     
@api.route('/index',methods=['get']) 
# get方式访问
def index():
  path =flask.request.values.get('filePath')
  #创建nc文件中dimension
  nc_fid2=Dataset(path, 'r',format="NETCDF3_CLASSIC")
  print(nc_fid2.__dict__.keys())
  ren = {'msg':'成功访问首页','msg_code':200,"data": str(nc_fid2)}
  #json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
  return json.dumps(ren,ensure_ascii=False)
 
if __name__ == '__main__':
  api.run(port=8888,debug=True,host='127.0.0.1') # 启动服务
  # debug=True,改了代码后，不用重启，它会自动重启
  # 'host='127.0.0.1'别IP访问地址
