from Raiser.cache_operator import *
from Raiser.cache_decorator import *
import numpy as np 



### HDF5操作测试 ###########################################
### hdf5写入数据
print("########################################################################## 1")
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[1, 2], [3, 4], [5, 6]])
Hdf5Operator.hdf5_writer_ndarray(h5path = 'test_operator.h5',
                                 group_name = 'x',
                                 info = 'var x test',
                                 version_name = '01',
                                 ndarray_obj = x)
Hdf5Operator.hdf5_writer_ndarray(h5path = 'test_operator.h5',
                                 group_name = 'y',
                                 info = 'var y test',
                                 version_name = '01',
                                 ndarray_obj = y)                                 
### hdf5读取数据
print("########################################################################## 2")
tmp_x = Hdf5Operator.hdf5_read_ndarray(h5path = 'test_operator.h5',
                                       group_name = 'x',
                                       version_name = '01')         
# print(x,type(x))    
### 缓存装饰器测试 ############################################
### 获取当前路径
print("########################################################################## 3")
CacheDecorator = CacheDecorator(hdf5_name = 'test_operator.h5')
print(CacheDecorator.cachepath)
### 定义原始运行函数
print("########################################################################## 4")
@CacheDecorator.hdf5_run(storage_name = 'multi_array_result')
def multi_array(x,y):
    multi_array_result = np.dot(x,y)
    return multi_array_result                                                           
### 运行函数
multi_array_result = multi_array(x = 'x',y = 'y')