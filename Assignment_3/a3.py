#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None


    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])


    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])


    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])


    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)


        self.A = np.transpose(np.array(A))
        self.p = self.A

    def translate(self, dx, dy="none"):
        '''
        Function to translate the polygon

        This function takes 2 arguments: dx and dy

        This function returns the final coordinates
        '''
        if dy == "none":
           Shape.translate(self,dx,dx)
        else:
           Shape.translate(self,dx,dy)
        print(np.transpose(self.A))
        self.A = np.dot(self.T_t,self.A)
        print(np.transpose(self.A))
        return np.array(self.A[0]),np.array(self.A[1])



    def scale(self, sx, sy="none"):
        '''
        Function to scale the polygon

        This function takes 2 arguments: sx and sx

        This function returns the final coordinates
        '''
        if sy == "none":
           Shape.scale(self,sx,sx)
        else:
           Shape.scale(self,sx,sy)
        tx = 0
        ty = 0
        self.A = self.A.tolist()
        for x in self.A[0]:
            tx += x

        for x in self.A[1]:
            ty += x
        cx = tx/len(self.A[0])
        cy = ty/len(self.A[0])
        self.A = np.array(self.A)
        print(np.transpose(self.A))
        self.A = np.dot(self.T_s,self.A)
        print(np.transpose(self.A))
        self.A = self.A.tolist()
        ntx = 0
        nty = 0
        for x in self.A[0]:
            ntx += x

        for x in self.A[1]:
            nty += x
        self.A = np.array(self.A)
        cxn = ntx/len(self.A[0])
        cyn = nty/len(self.A[0])

        return self.translate(cx - cxn,cy - cyn)

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        '''
        Shape.rotate(self,deg)
        print(np.transpose(self.A))
        self.A = self.A.tolist()
        for x in self.A[0]:
            x += rx
        for x in self.A[1]:
            x += ry
        self.A = np.array(self.A)

        self.A = np.dot(self.T_r,self.A)

        self.A = self.A.tolist()
        for x in self.A[1]:
            x += -ry
        for x in self.A[0]:
            x += -rx
        self.A = np.array(self.A)
        print(np.transpose(self.A))
        return np.array(self.A[0]),np.array(self.A[1])

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        x_dim = max(self.A[0])
        if x_dim < max(self.p[0]):
            x_dim = max(self.p[0])

        y_dim = max(self.A[1])
        if y_dim < max(self.p[1]):
            y_dim = max(self.p[1])

        Shape.plot(self,x_dim,y_dim)
        plt.plot(self.p[0],self.p[1], linestyle = dashed)
        plt.plot(self.A[0],self.A[1], linestyle = solid)


class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.x = x
        self.p_x = self.x
        self.y = y
        self.p_y = self.y
        self.r = radius
        self.p_r = self.r
        self.c = np.array([self.x,self.y,1])

    def translate(self, dx, dy="none"):
        '''
        Function to translate the circle

        This function takes 2 arguments: dx and dy (dy is optional).

        This function returns the final coordinates and the radius
        '''
        if dy == "none":
           Shape.translate(self,dx,dx)
        else:
           Shape.translate(self,dx,dy)

        result = np.dot(self.T_t,self.c)
        self.x = result[0]
        self.y = result[1]
        return self.x,self.y,self.r

    def scale(self, sx):
        '''
        Function to scale the circle

        This function takes 1 argument: sx

        This function returns the final coordinates and the radius
        '''
        Shape.scale(self,sx,1)
        scale_c = np.dot(self.T_s,[self.r,1,1])
        self.r = scale_c[0]

        return self.x,self.y,self.r

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates and the radius
        '''
        Shape.rotate(self,deg)
        self.T_r = self.T_r.tolist()
        for x in self.T_r:
            for i in x:
                i = round(i,2)
        self.T_r = np.array(self.T_r)
        self.x += rx
        self.y += ry
        self.c = np.dot(self.T_r,self.c)
        self.x = self.c[0]
        self.y = self.c[1]
        return self.x,self.y,self.r

    def plot(self):
        '''
        Function to plot the circle

        This function should plot both the initial and the transformed circle

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        '''

        x_dim = self.x
        y_dim = self.y
        x_dim += self.r
        y_dim += self.r

        if x_dim < (self.p_x + self.p_r):
            x_dim < (self.p_x + self.p_r)
        if y_dim < (self.p_y + self.p_r):
            y_dim < (self.p_y + self.p_r)

        Shape.plot(self)
        plt.Circle((self.x,self.y), self.r, linestyle = solid)
        plt.Circle((self.p_x,self.p_y), self.p_r, linestyle = dashed)

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    v = input('verbose? 1 to plot, 0 otherwise: ')
    if v =='0':
        t = input('Enter the number of test cases: ')
        for i in range(t):
            shape = input('Enter type of shape (polygon = 0/circle = 1): ')
            if shape == "0":
                 n = input('Enter the number of sides: ')
                 M = []
                 for x in range(1,n+1):
                     lzt = list(map(float,input('enter (x{},y{}): '.format(n)).split()))
                     lzt.append(1)
                     for x in lzt:
                         x = round(x,2)
                     M.append(lzt)
                 M = np.array(M)
                 s = Polygon(M)
                 n_q = input('Enter the number of queries: ')
                 input('''Enter Query:
1) R deg (rx) (ry)
2) T dx (dy)
3) S sx (sy)
4) P''')
                 for i in range(n_q):
                    lst = list(map(int,input().split()))
                    if lst[0].lower() == "T".lower():
                        s.translate(','.join(lst[1:]))
                    if lst[0].lower() == "R".lower():
                        s.rotate(','.join(lst[1:]))
                    if lst[0].lower() == "S".lower():
                        s.scale(','.join(lst[1:]))
                    if lst[0].lower() == "P".lower():
                        s.plot()
                 s.plot()
            if shape == "1":
                  lqt = list(float,input("Enter centre coordinates and radius [x y r]: ").split())
                  for x in lqt:
                      x = round(x,2)
                  c = Circle(lqt[0],lqt[1],lqt[2])
                  n_q = input('Enter the number of queries: ')
                  input('''Enter Query:
 1) R deg (rx) (ry)
 2) T dx (dy)
 3) S sx
 4) P''')
                  for i in range(n_q):
                     lst = list(map(int,input().split()))
                     if lst[0].lower() == "T".lower():
                         c.translate(','.join(lst[1:]))
                     if lst[0].lower() == "R".lower():
                         c.rotate(','.join(lst[1:]))
                     if lst[0].lower() == "S".lower():
                         c.scale(','.join(lst[1:]))
                     if lst[0].lower() == "P".lower():
                         c.plot()
                  c.plot()
    if v =='1':
         t = input('Enter the number of test cases: ')
         for i in range(t):
             shape = input('Enter type of shape (polygon = 0/circle = 1): ')
             if shape == "0":
                  n = input('Enter the number of sides: ')
                  M = []
                  for x in range(1,n+1):
                      lzt = list(map(float,input('enter (x{},y{}): '.format(n)).split()))
                      lzt.append(1)
                      for x in lzt:
                          x = round(x,2)
                      M.append(lzt)
                  M = np.array(M)
                  s = Polygon(M)
                  n_q = input('Enter the number of queries: ')
                  input('''Enter Query:
 1) R deg (rx) (ry)
 2) T dx (dy)
 3) S sx (sy)
 4) P''')
                  for i in range(n_q):
                     lst = list(map(int,input().split()))
                     if lst[0].lower() == "T".lower():
                         s.translate(','.join(lst[1:]))
                         s.plot()

                     if lst[0].lower() == "R".lower():
                         s.rotate(','.join(lst[1:]))
                         s.plot()
                     if lst[0].lower() == "S".lower():
                         s.scale(','.join(lst[1:]))
                         s.plot()
                     if lst[0].lower() == "P".lower():
                         s.plot()
                  s.plot()
             if shape == "1":
                   lqt = list(float,input("Enter centre coordinates and radius [x y r]: ").split())
                   for x in lqt:
                       x = round(x,2)
                   c = Circle(lqt[0],lqt[1],lqt[2])
                   n_q = input('Enter the number of queries: ')
                   input('''Enter Query:
  1) R deg (rx) (ry)
  2) T dx (dy)
  3) S sx
  4) P''')
                   for i in range(n_q):
                      lst = list(map(int,input().split()))
                      if lst[0].lower() == "T".lower():
                          c.translate(','.join(lst[1:]))
                          c.plot()

                      if lst[0].lower() == "R".lower():
                          c.rotate(','.join(lst[1:]))
                          c.plot()
                      if lst[0].lower() == "S".lower():
                          c.scale(','.join(lst[1:]))
                          c.plot()
                      if lst[0].lower() == "P".lower():
                          c.plot()
                   c.plot()
