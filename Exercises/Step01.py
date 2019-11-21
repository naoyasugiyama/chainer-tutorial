# python chainer Tutorial 
# url : https://tutorials.chainer.org/ja/Exercise_Step_01.html#

import math

# 問2.1 (組み込み関数)
def sample01():
    a=[4, 8, 3, 4, 1]
    print(len(a))
    print(max(a))
    print(min(a))
    print(sum(a))
    a.sort()
    print(a)

# 問2.2 (演算)
def sample02():
    #5 float
    print( 1.2 + 3.8 )
    # 0 inter
    print( 10 // 100 )
    # false bool
    print( 1 >= 0 )
    # true bool
    print( 'Hello World' == 'Hello World' )
    # true bool
    print( not 'Chainer' != 'Tutorial' )
    # false  
    print( all([True, True, False]) )
    # true 
    print( any([True, True, False]) )
    # 3
    print(abs(-3))
    # 0 error 
    print( type(2 // 0) )

# 問2.3 (リストの基本操作)
def sample03():
    a = [4, 8, 3, 4, 1]
#    a.pop(0)  first
#    a.pop(-1) last
#    a.append(100)
    print(a)

# 問2.4 (リスト内包表記)
def sample04():
    a = [4, 8, 3, 4, 1]
    #squares = [ x % 2 for x in a ]
    #print(squares)
    #countOdd(a)
    removeEven(a)

def countOdd( data_list :list):
    squears = [ x % 2 for x in data_list ]
    print(squears.count(1))
    
def removeEven( data_list :list ):
    b = [ x for x in data_list if x % 2 != 0 ]
    print(b)

# 問2.5 (文字列)
def sample05():
#    number_s = [ str(x) for x in range(100) ]
#    result = ' '.join(number_s)
    print( ' '.join( [str(x) for x in range(100)] ) )
    print(" 1.0 / 7.0 is {0:.9f}".format( 1.0 / 7.0 ))

# 問2.6 (クラス)
class DataManager():
    def __init__(self, x, y, z):
        self.x, self.y ,self.z = x , y , z

    def add_x(self, delta ):
        self.x += delta
    
    def add_y(self, delta ):
        self.y += delta
    
    def add_z(self, delta ):
        self.z += delta 

    def sum(self):
        return self.x + self.y + self.z

def sample06():
    data_manager = DataManager( 2, 3, 5 )
    print( data_manager.sum() )
    data_manager.add_x(4)
    print( data_manager.sum() )
    data_manager.add_y(0)
    print( data_manager.sum() )
    data_manager.add_z(-9)
    print(data_manager.sum())

# 問2.7 (関数呼び出し)
def f(a):
#    print( "f(a):{%s}" % id(a) )
    a = [ 6, 7, 8 ]
#    print( "f(a):{%s}" % id(a) ) )

def g(a):
    a.append(1)

def somfunction():
    a0 = [1, 2, 3]
    print( "a0:[%s]" % id(a0) )
    f(a0) 
    print(a0) # print 1,2,3 
    # f(a) 関数 a= [ 6, 7, 8] のときにオブジェクトを生成している 変数 a0とは別になる
    # id()を使えばオブジェクトが同じかわかる


    a1 = [1, 2, 3]
    g(a1)
    print(a1) # 1,2,3,1　g()にリストを追加される
    # リスト型を関数の引数にするときは参照がわたされる

def sample07():
    somfunction()

# 問2.8 (制御構文)
# 2 ~ 100までの素数をリスト化
def sample08():

    max_num = 100
    primes = [ p for p in range( 2, max_num ) if check_prime03(p) ]
    print( primes )

def check_prime03( num ):
    if num == 1:
        return False

    for check in range( 2, int(math.sqrt(num)) + 1 ):
        if num % check == 0:
            return False

    return True







if __name__ == '__main__':
    sample08()


