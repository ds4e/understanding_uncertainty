import random

class Mx:
    """ Basic version of a matrix class with no error handling. """

    ############ Constructor:
    
    def __init__(self, vals, rows = 1, cols = 1):
        if vals is None:
            self.rows = rows
            self.cols = cols
            self.m = [ [0]*cols for i in range(rows)]
        else:
            # Check all rows the same length
            self.rows = len(vals)
            self.cols = len(vals[0])
            self.m = vals

    ############ Class methods:

    def randInt(self,lower=-10,upper=10):
        for i in range(self.rows):
            for j in range(self.cols):
                self.m[i][j] = random.randint(lower,upper)

    def randFloat(self,lower=-10,upper=10):
        for i in range(self.rows):
            for j in range(self.cols):
                self.m[i][j] = random.uniform(lower,upper)

    def eye(self):
        self.m = [ [0]*self.cols for i in range(self.rows)]
        for i in range(self.rows):
                self.m[i][i] = 1


    ############ Class Functions:

    def t(A):
        At = Mx( vals=None, rows=A.cols, cols=A.rows )
        for i in range(A.rows):
            for j in range(A.cols):
                At.m[j][i] = A.m[i][j]
        return At

    def add(A,B):
        rws_A = A.rows
        cls_A = A.cols
        rws_B = B.rows
        cls_B = B.cols
        C = []
        for i in range(rws_A):
                C.append( [ A.m[i][j] + B.m[i][j] for j in range(cls_B)] )
        C = Mx(C)
        return C

    def sub(A,B):
        rws_A = A.rows
        cls_A = A.cols
        rws_B = B.rows
        cls_B = B.cols
        C = []
        for i in range(rws_A):
                C.append( [ A.m[i][j] - B.m[i][j] for j in range(cls_B)] )
        C = Mx(C)
        return C

    def mat_mul(A,B):
        rws_A = A.rows
        cls_A = A.cols
        rws_B = B.rows
        cls_B = B.cols
        C = []
        for i in range(rws_A):
            ith_row = []
            for j in range(cls_A):
                result = [ A.m[i][k]*B.m[j][k] for k in range(rws_B) ]
                ith_row.append( sum(result) )
            C.append(ith_row)
        C = Mx(C)
        return C
    
    def scalar_mul(s,A):
        C = []
        for i in range(A.rows):
            C.append([ s*A.m[i][j] for j in range(A.cols)])
        C = Mx(C)
        return C
    
    # def solve(A,b):
    #     return x

    ############ Operator overloading and interpreter cruft:

    def __add__(A, B): # +
        return Mx.add(A,B)
    
    def __sub__(A, B): # -
        return Mx.sub(A,B)

    def __invert__(A): # ~
        return Mx.t(A)
    
    def __mul__(A, B): # *
        A_is_mx = isinstance(A,Mx)
        B_is_mx = isinstance(B,Mx)
        if A_is_mx and B_is_mx:
            y = Mx.mat_mul( A, B )
        elif A_is_mx and not B_is_mx:
            y = Mx.scalar_mul( B, A )
        elif not A_is_mx and B_is_mx:
            y = Mx.scalar_mul( A, B )
        else:
            y = A*B
        return y

#    def __truediv__(A,b): # b/A
#        return Mx.solve(A,b)

    def __str__(self):
        # output = ''
        # for i in range(self.rows):
        #     output = output+str(self.m[i])+'\n'
        # return output
        return str(self.m)

    def __repr__(self):
        output = ''
        for i in range(self.rows):
            output = output+str(self.m[i])+'\n'
        return output
