# NumPy 入門
# https://tutorials.chainer.org/ja/08_Introduction_to_NumPy.html
import numpy as np


def hoge01():
    a = np.array([ 1, 2, 3])
    # attribute
    print('Shape:', a.shape)
    # dimensionality, number of dimensions
    print('Rank:', a.ndim)

    print('--------------------------------')

    b = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
    print('Shape:', b.shape)
    print('Rank:', b.ndim)
    print('Size', b.size)

    print('--------------------------------')
    # 形を指定して、要素が全て 0 で埋められた ndarray を作る
    c = np.zeros(( 3, 3))
    print(c)
    # 形を指定して、要素が全て 1 で埋められた ndarray を作る
    d = np.ones(( 2, 3))
    print(d)
    # 形と値を指定して、要素が指定した値で埋められた ndarray を作る
    e = np.full(( 3, 2), 9)
    print(e)# arrayの表示結果が他と違う . がついてない
    # 指定の大きさの単位行列
    f = np.eye(5)
    print(f)
    # 形を指定して、 0 ~ 1 の間の乱数で要素を埋めた ndarray を作る
    g = np.random.random((4, 5))
    print(g)
    # 3 から始まり 10 になるまで 1 ずつ増加する数列を作る（10 は含まない）
    a01 = np.arange(3, 10, 1)
    print(a01)
    print('--------------------------------')

# 8.3. 多次元配列の要素を選択する
def hoge02():
    a = np.random.random((4, 5))
    # 4x5行列から 1,2を抽出
    val = a[0, 1]
    print(a)
    print(val)
    print('--------------------------------')
    # 8.3.2. スライスによる要素の選択
    # 4 x 5 行列 a の真ん中の 2 x 3 = 6 個の値を取り出す
    center = a[1:3, 1:4]
    print(center)    
#    center = a[0:3, 0:4]
#    print(center)
    print('Shape of e:', a.shape)
    print('Shape of center:', center.shape)




call_list = [
    hoge01,
    hoge02
]


if __name__ == '__main__':
    call_list[1]()
