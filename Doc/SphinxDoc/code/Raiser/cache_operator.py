# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个hdf5操作类，提供hdf5文件的相关读写操作
"""
模块介绍
-------

这是一个hdf5操作类，提供hdf5文件的相关读写操作

设计模式：

    无

关键点：    

    （1）无 

主要功能：            

    （1）hdf5读写操作                                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from tables import *



####### HDF5操作类 ##########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                              ###
### 主要功能：                                                            ###
### （1）读写操作                                                         ###
############################################################################



###### HDF5操作类 #####################################################################
######################################################################################



class Hdf5Operator(object):
    """
    类介绍：

        这是一个Hdf5操作类，主要技术采用hdf5和pytables，主要功能有创建hdf5数据组，向hdf5文件写入和读取的操作。
    """


    @staticmethod
    def hdf5_writer_ndarray(info = "no infomation",**kwargs):
        """
        方法功能：

            定义一个hdf5写入数据的方法

        参数：
            h5path (str): hdf5文件路径
            group_name (str): 数据组名称
            version_name (str): 数据版本
            ndarray_obj (object): ndarray对象

        返回：
            无
        """

        ### 收集参数
        h5path = kwargs['h5path']
        group_name = kwargs['group_name']
        version_name = 'data' +  '_' + kwargs['version_name']
        ndarray_obj = kwargs['ndarray_obj']
        ### 打开文件流,以追加的模式打开
        h5file = open_file(filename = h5path,mode = 'a')
        ### 创建数据组
        try:
            data_group = h5file.create_group(where = "/",name = group_name,title = info)        
        except:
            data_group = "/{}".format(group_name)
        ### 压缩算法选择
        filters = Filters(complevel = 5,complib = 'blosc')
        ### 在数据组下写入数据对象
        try:
            h5file.create_earray(where = data_group,name = version_name,obj = ndarray_obj,filters = filters)
        except:
            pass
        ### 关闭文件流
        h5file.close()
        print("----------------- hdf5 write data successful!")


    @staticmethod
    def hdf5_read_ndarray(**kwargs):
        """
        方法功能：

            定义一个hdf5读取数据的方法

        参数：
            h5path (str): hdf5文件路径
            group_name (str): 数据组名称
            version_name (str): 数据版本

        返回：
            data_ndarray (ndarray): ndarray数据
        """        
        ### 收集参数
        h5path = kwargs['h5path']
        group_name = kwargs['group_name']
        version_name = 'data' +  '_' + kwargs['version_name']
        where_path = '/{}'.format(group_name)
        ### 打开文件流
        h5file = open_file(filename = h5path,mode = 'r')
        ### 获取数据索引
        data_reader = h5file.get_node(where = where_path,name = version_name)
        ### 获取数据帧
        data_ndarray = data_reader.read()
        ### 关闭文件流
        h5file.close()
        print("----------------- hdf5 read data successful!")

        return data_ndarray



###############################################################################################
###############################################################################################


