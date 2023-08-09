# readNetCDF
nodejs + electron + python(netCDF4+flask)
## 启动
yarn start
## 背景
由于某些原因导致，需要查看netcdf软件内容。苦于没有适合的node包，于是只能借助python，
但是本人对python理解，也就照猫画虎，于是用python服务的方式来，达成js和python的通讯
利用python启动一个服务，利用electron的能力，用axios去调用服务，传入文件路径，python解析后，将结果返回
从而完成对文件的读取。加上electron的套壳能力，使之相结合