# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个缓存装饰器类，主要将内存操作转变为磁盘文件操作
"""
模块介绍
-------

这是一个缓存装饰器类，主要将内存操作转变为磁盘文件操作

设计模式：

    无

关键点：    

    （1）装饰器 

主要功能：            

    （1）缓存                                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os
from functools import wraps,partial
from Raiser.cache_operator import *
import numpy as np 



####### 缓存装饰器 ##########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                              ###
### 主要功能：                                                            ###
### （1）缓存装饰器                                                       ###
############################################################################



###### 缓存装饰器 #####################################################################
######################################################################################



class CacheDecorator(object):
    """
    类介绍：

        这是一个缓存装饰器类，主要技术采用装饰器模式，主要功能包括为函数运算提供高速大空间缓存功能。
    """

    
    def __init__(self,hdf5_name,cachepath = None):
        """
        属性功能：

            定义一个初始化方法功能

        参数：
            hdf5_name (str): hdf5文件名
            cachepath (str): 缓存工作路径
        """

        self.hdf5_name = hdf5_name
        if cachepath == None:
            self.cachepath = self.get_default_cachepath()
        else:
            self.cachepath = cachepath


    def get_default_cachepath(self):
        """
        方法功能：

            定义一个获取默认缓存路径的方法

        参数：
            无

        返回：
            无
        """

        pwd_path = os.getcwd()

        return pwd_path


    def hdf5_run(self,func = None,storage_name = None,message = None,version_name = None):
        """
        方法功能：
            
            定义一个以hdf5为后端缓存优化计算函数的装饰器方法

        参数：
            func (object): 目标函数
            storage_name (str): 结果存储名称
            message (str): 其他信息
            version_name (str): 版本信息

        返回：
            wrapper (object): 装饰过的函数对象
        """

        if func is None:
            return partial(self.hdf5_run,storage_name = storage_name,message = message)
        wrapper_storage_name = storage_name if storage_name else "result"
        wrapper_message = message if message else "no message"
        wrapper_version_name = version_name if version_name else '01'
        @wraps(func)
        def wrapper(*args,**kwargs):
            ### 收集参数
            kwargs_list = list(kwargs.keys())
            func_kwargs = {}
            for i in kwargs_list:
                ### 读取数据
                tmp_data = Hdf5Operator.hdf5_read_ndarray(h5path = self.hdf5_name,
                                                          group_name = str(i),
                                                          version_name = wrapper_version_name)
                func_kwargs[i] = tmp_data
            ### 执行计算函数
            result = func(*args,**func_kwargs)
            ### 存入hdf5
            Hdf5Operator.hdf5_writer_ndarray(h5path = self.hdf5_name,
                                             group_name = wrapper_storage_name,
                                             version_name = wrapper_version_name,
                                             ndarray_obj = result)
            print(result)
            ### 删除变量
            del result
            return "wrapper run done!"
        return wrapper



###################################################################################################################
###################################################################################################################        


