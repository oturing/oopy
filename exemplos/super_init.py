
class X(object):
    def __init__(self):
        print 'X.__init__'
        
class Y(X):
    def __init__(self):
        print 'Y.__init__'
        
class Z(Y):
    pass
    
class W(X, Y):
    pass
    
x = X()

y = Y()

z = Z()

w = W()
