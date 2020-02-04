import numpy as np
from numpy.linalg import *

def main():
    # 1
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    # 2
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))
    print('Rand:')
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print('RandInt:')
    print(np.random.randint(1, 10, 3))
    print(np.random.randn(2, 4))
    print('Choice:')
    print(np.random.choice([10, 20, 30, 2, 8]))
    print('Distribute:')
    print(np.random.beta(1, 10, 100))
    # 3 Array Opes
    lst = np.arange(1, 11).reshape([2, -1])
    print('Exp:', np.exp(lst))
    print('Exp2:', np.exp2(lst))
    print('Sqrt:', np.sqrt(lst))
    print('Sin:', np.sin(lst))
    print('Log:', np.log(lst))

    lst = np.array([
        [[1, 2, 3, 4], [4, 5, 6, 7]],
        [[7, 8 , 9, 10], [10, 11, 12, 13]],
        [[14, 15, 16, 17], [18, 19, 20, 21]]
    ])
    print('axis_0:\n', lst.sum(axis=0))
    print('axis_1:\n', lst.sum(axis=1))
    print('axis_2:\n', lst.sum(axis=2))
    print('axis_1_max:\n', lst.max(axis=1))
    print('axis_0_min:\n', lst.min(axis=0))
    
    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print('Add:', lst1 + lst2)
    print('Dot:', np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))
    
    print('Concatenate:', np.concatenate((lst1, lst2), axis=0))
    print('Vstack:', np.vstack((lst1, lst2)))
    print('Hstack:', np.hstack((lst1, lst2)))
    print('Split_2:', np.split(lst1, 2))
    print('Split_4:', np.split(lst1, 4))
    print('Copy:', np.copy(lst1, 4))
    
    # 4 liner
    print('Eye:\n', np.eye(3))
    lst = np.array([
        [1, 2],
        [3, 4]
        ])
    print('Inv:\n', inv(lst))
    print('T:\n', lst.transpose())
    print('Det:\n', det(lst))
    
if __name__ == '__main__':
    main()