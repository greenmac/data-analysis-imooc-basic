import numpy as np

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
    

if __name__ == '__main__':
    main()