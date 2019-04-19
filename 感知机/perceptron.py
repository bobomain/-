import numpy as np

def creatDataSet( ):
    group=np.array([[3,3],[4,3],[1,1]])
    label=[1,1,-1]
    return group,label

def update( x , y ):
    global w , b
    for i in range( len( x ) ):
        w[ i ] += y * x[ i ]
    b = b + y
    
def cal( x , y ):
    global w , b
    result=0
    for i in range( len( x ) ):
        result += w[ i ] *  x[ i ]
    result += b
    result *= y
    return result

def perceptron_func( group , label ):
    global w , b
    isFind = False
    n=group.shape[0]
    x_col=group.shape[1]
    w = [0] * x_col
    b = 0
    while isFind == False:
        for i in range( n ):
            if cal(group[ i ] , label[ i ]) <= 0:
                update(group[ i ] , label[ i ])
                print(i+1,w,b)
                break
            elif i == n - 1:
                print(i+1,w,b)
                isFind = True

g , l = creatDataSet( )
print('x   w    b')
perceptron_func(g,l)
