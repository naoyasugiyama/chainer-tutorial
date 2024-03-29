# NumPy 入門
# https://tutorials.chainer.org/ja/08_Introduction_to_NumPy.html
import numpy as np
import timeit

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
    # 先程の真ん中の 6 個の値を 0 にする
    a[1:3, 1:4] = 0
    print(a)


# 8.3.3. 整数配列による要素の選択
def hoge03():
    a = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    )
    print(a)

    # 1 行 2 列目：a[0, 1]
    # 3 行 2 列目：a[2, 1]
    # 2 行 1 列目：a[1, 0]
    # の 3 つの要素を選択して並べ、形が (3,) であるような ndarray を作りたいとします。
    print(np.array([a[0, 1], a[2, 1], a[1, 0]]) )
    print(a[[0, 2, 1], [1, 1, 0]])

    # 8.4. ndarray のデータ型

    # 整数（Python の int 型）の要素をもつリストを与えた場合
    x01 = np.array([1, 2, 3])
    print(x01.dtype)

    # 浮動小数点数（Python の float 型）の要素をもつリストを与えた場合
    x02 = np.array([1., 2., 3.])
    print(x02.dtype)

    x03 = np.array([1, 2, 3], dtype=np.float32)
    print(x03.dtype)

    x04 = np.array([1, 2, 3], dtype='float32')
    print(x04.dtype)

    x05 = np.array([1, 2, 3], dtype='f')
    print(x05.dtype)
    #一度あるデータ型で定義した配列のデータ型を別のものに変更するには、astype を用いて変換を行います。
    x05 = x05.astype(np.float64)
    print(x05.dtype)


# 8.5. 多次元配列を用いた計算
def hoge04():
    a = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    b = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    # 足し算
    print( a + b )
    # 引き算
    print( a - b )
    # 掛け算
    print( a * b )
    # 割り算
    print( a / b )

    # 要素ごとに平方根を計算する
    c = np.sqrt(b)
    print( c )
    # 要素ごとに値を n 乗する
    n = 2
    print( np.power(b, n) )
    # or 
    print( c ** n ) 
    print('---------------------------------')



# ブロードキャスト broadcast
# https://tutorials.chainer.org/ja/08_Introduction_to_NumPy.html
def hoge05():

    a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
    ])
    b = np.array([1, 2, 3])
    c = a + b
    print(c)

    # 積
    a = np.array([1, 2, 3])
    b = np.array([2, 2, 2])
    c = a * b
    print(c)
    # or 
    print( a * 2  )



    # ブロードキャストルール 2 つの配列の各次元が同じ大きさになっているか、どちらかが 1 であること

    # 0 ~ 9 の範囲の値をランダムに用いて埋められた (2, 1, 3) と (3, 1) という大きさの配列を作る
    d = np.random.randint(0, 10, (2, 1, 3))
    e = np.random.randint(0, 10, (3, 1))

    print('d:\n', d)
    print('\nd.shape:', d.shape)
    print('\ne:\n', e)
    print('\ne.shape:', e.shape)
    f = d + e
    print('\nd + e:\n', f)
    print('\n(d + e).shape:', f.shape)

    print('---------------------------------\n')

    # [] を利用した手動計算
    print('Original shape:', e.shape)
    e_expanded = e[np.newaxis, :, :]
    print('Added new axis to the top:', e_expanded.shape)
    e_expanded2 = e[:, np.newaxis, :]
    print('Added new axis to the middle:', e_expanded2.shape)

    print('e:\n', e)
    print('e_expanded:\n', e_expanded)
    print('e_expanded2:\n', e_expanded2)

    a = np.array([
        [0, 1, 2, 1, 0],
        [3, 4, 5, 4, 3],
        [6, 7, 8, 7, 6],
        [3, 4, 5, 4, 4],
        [0, 1, 2, 1, 0]
    ])

    b = np.array([1, 2, 3, 4, 5])

    # 結果を格納する配列を先に作る
    c = np.empty((5, 5))

    # jupyter... %%time
    for i in range(a.shape[0]):
        c[i, :] = a[i, :] + b
    print(c)

    c = a + b
    print(c)


# 8.7. 行列積 > jupter nodebook > introductoryNumpy.ipynbへ
def hoge06():
    print(0)




call_list = [
    hoge01,
    hoge02,
    hoge03,
    hoge04,
    hoge05,
    hoge06
]


if __name__ == '__main__':
    last = len(call_list) - 1
    call_list[last]()

