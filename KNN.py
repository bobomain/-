#-*-coding:utf-8 -*-
import numpy as np
import math

#训练集和类别
def creatDataSet( ):
    group = np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    label = ['A','A','B','B']
    return group,label

#确定输入实例以及k值
def inputData( ):
    test_data=np.array([ [1.1 , 0.3] ])
    K = 3
    return test_data,K

#归一化
def Normalization( group ):
    max = np.amax(group,axis=0)
    min = np.amin(group,axis=0)
    for i in range(len(group)):
        group[i][0] /= (max[ 0 ] - min[ 0 ])
        group[i][1] /= (max[ 1 ] - min[ 1 ])
    return group

#求输入实例与训练集中所有点的欧氏距离
def Distance( group ,dis ):
    test,K=inputData( )
    group = Normalization( group )
    for i in range(len(dis)):
        dis[i] = math.sqrt((group[i][0] - test[0][0]) ** 2 + (group[i][1] - test[0][1]) ** 2 )
    return dis,K,test

#找出输入实例的类别
def Classify_By_KNN( group , label ):
    size = len( label )
    dis = np.zeros( size )
    dis,k,test = Distance( group ,dis )
    sortedDistIndex=np.argsort(dis)
    countLabel={}
    for i in range(k):
        l=label[sortedDistIndex[i]]
        countLabel[l] = countLabel.get(l,0) + 1
    countMax=max(countLabel.values())
    for key,value in countLabel.items():
        if value == countMax:
            print("测试数据为:",test,"   分类结果为：",key)
    
g,l=creatDataSet( )
Classify_By_KNN( g , l )
