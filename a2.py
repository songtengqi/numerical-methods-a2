#!/usr/bin/env python

from numpy import array, arange,log

'''
NOTE: You are not allowed to import any function from numpy's linear 
algebra library, or from any other library except math.
'''

'''
    Part 1: Warm-up (bonus point)
'''

def spaces_and_tabs():
    '''
    A few of you lost all their marks in A1 because their file 
    contained syntax errors such as:
      + Missing ':' at the end of 'if' or 'for' statements.
      + A mix of tabs and spaces to indent code. Remember that indendation is part
        of Python's syntax. Mixing tabs and spaces is not good because it
        makes indentation levels ambiguous. For this reason, files 
        containing a mix of tabs and spaces are invalid in Python 3. This
        file uses *spaces* for indentation: don't add tabs to it!
    Remember that you are strongly encouraged to check the outcome of the tests
    by running pytest on your computer and by checking Travis.
    Task: Nothing to implement in this function, that's a bonus point, yay!
          Just don't loose it by adding syntax errors to this file...
    Test: 'tests/test_spaces_and_tabs.py'
    '''
    return ("I won't use tabs in my code",
            "I will make sure that my code has no syntax error",
            "I will check the outcome of the tests using pytest or Travis"
            )

'''
    Part 2: Linear regression
'''

def problem_3_2_5():
    '''
        We will solve problem 3.2.5 in the textbook.
        Arrays 'year' and 'ppm' contain the annual atmospheric CO2 concentration
        in parts per million in Antarctica.
        Task: This function must return the average increase in ppm per year,
        obtained by fitting a straight line to the data.
        Test: Function 'test_problem' in 'tests/test_problem_3_2_5.py'
        Hint: Fitting is meant in the least-square sense.
        '''
    
    year = arange(1994, 2010)  # from 1994 to 2009
    ppm = array([356.8, 358.2, 360.3, 361.8, 364.0, 365.7, 366.7, 368.2,
                 370.5, 372.2, 374.9, 376.7, 378.7, 381.0, 382.9, 384.7])

    ## YOUR CODE HERE
    
    x_bar=sum(year)/len(year)
    y_bar=sum(ppm)/len(ppm)
    global b
    b=sum(ppm*(year-x_bar))/sum(year*(year-x_bar))
    global a
    a=y_bar-b*x_bar
    return b
    raise Exception("Not implemented")


def extrapolation_3_2_5():
    '''
    Task: Return the estimated atmospheric CO2 concentration in Antarctica 
          in 2020.
    Test: Function 'test_2020' in 'tests/test_problem_3_2_5.py'
    Hint: Use the result of the previous function.
    '''
    ## YOUR CODE HERE
    
    return a+b*2020
    
    raise Exception("Not implemented")


'''
    Part 3: Non-linear equations
'''

'''
    We will solve problem 4.1.19 in the textbook:
    "
        The speed v of a Saturn V rocket in vertical flight near the surface
        of earth can be approximated by:
            v = u*log(M0/(M0-mdot*t))-g*t
            (log base is e)
        where:
           * u = 2510 m /s is the velocity of exhaust relative to the rocket
           * M0 = 2.8E6 kg is the mass of the rocket at liftoff
           * mdot = 13.3E3 kg/s is the rate of fuel consumption
           * g = 9.81 m/s**2 is the gravitational acceleration
           * t is the time measured from liftoff
    "
'''

def f_and_df(t):
    '''
    Task: return a tuple containing (1) the value of the velocity v
          at time t, (2) the value of the derivative of v at time t.
    Parameter: 't' is the value at which the function and its derivative
               must be evaluated.
    Example: f_and_df(100) must be close to (636.3361111401882, 12.89952381017656)
    Test: function 'f_and_df' in 'tests/test_problem_4_1_19'
    Hint: to compute f', use the central approximation
    '''

    global u,M0,mdot,g
    u=2510
    M0=2.8E6
    mdot=13.3E3
    g=9.81
    
    ## YOUR CODE HERE

    v=u*log(M0/(M0-mdot*t))-g*t
    vder=u*mdot/(M0-mdot*t)-g
    
    return v,vder
    
    raise Exception("Not implemented")

def problem_4_1_19(v1, acc):
    '''
    Task: return the time in seconds when the rocket reaches velocity v1,
          with accuracy acc.
    Parameters:  'v1' is a float representing the velocity of the rocket in m/s.
                 'acc' is a float representing the accuracy of the solution.
    Example: problem_4_1_19(335, 0.1) = 70.877972
    Test: function 'test_problem' in 'tests/test_problem_4_1_9.py'
    Hint: plot the function to get a first guess at the solution.
    '''

    ## YOUR CODE HERE

    t1=0
    t2=65
    while abs(t2-t1)>acc:
        t1=t2
        f=u*log(M0/(M0-mdot*t1))-g*t1-v1
        fder=u*mdot/(M0-mdot*t1)-g
        t2=t1-f/fder
    return t2

    raise Exception("Not implemented")   

'''
    Part 4: Systems of non-linear equations
'''

'''
    We will solve problem 4.1.26 from the textbook:
        "
        The equation of a circle is: (x-a)**2 + (y-b)**2 = R**2
        where R is the radius and (a,b) are the coordinates of the center.
        Given the coordinates of three points p1, p2 and p3, find a, b
        and R such that the circle of center (a, b) and radius R passes
        by p1, p2 and p3.
        "
'''

def f_4_1_26(x_data, y_data, x):
    '''
    The problem consists in finding the zero of a
    function of 3 variables (a, b and R). 
    Task: return an array containing the coordinates of f(x) such
          that the problem can be solved by finding a zero of f. 
          x is a vector representing (a, b, R).
    Parameters: + 'x_data' is an array of 3 coordinates representing the abscissa
                   of the input points.
                + 'y_data' is an array of 3 coordinates representing the ordinates
                   of the input points.
                + 'x' is an array of 3 coordinates representing (a, b, R)
    Example: f_4_1_26(array([0.5, 1, 1.5]),
                      array([2, 2.5, 2]),
                      array([1, 2, 0.5])) = [0, 0, 0]
    Test: function 'test_f' in 'tests/test_problem_4_1_26.py'
    '''
    ## YOUR CODE HERE

    arr=[]
    for i in range(len(x_data)):
        f=(x_data[i]-x[0])**2+(y_data[i]-x[1])**2-x[2]**2
        arr.append(f)
    return arr

    raise Exception("Not implemented")

def problem_4_1_26(x_data, y_data):
    '''
    Task: return a, b and R so that the circle of center (a, b) and radius
          R passes by the 3 points defined by x_data and y_data.
    Parameters: + 'x_data' is an array of 3 coordinates representing the abscissa
                   of the input points.
                + 'y_data' is an array of 3 coordinates representing the ordinates
                   of the input points.
    Example: problem_4_1_26(array([0.5, 1, 1.5]), array([2, 2.5, 2]))
             must return [1., 2., 0.5]
    Test: function 'test_problem' in 'tests/test_problem_4_1_26.py''
    Hint: use Newton-Raphson for systems of non-linear equations to find
          a zero of f_4_1_26.
    '''
    ## YOUR CODE HERE
    x1,x2,x3=x_data
    y1,y2,y3=y_data
    a=0.49
    f=1
    while abs(f)>0.001:
        a+=0.01
        b=(x1-x2)*(x1+x2-2*a)/(2*y1-2*y2)+(y2+y1)/2
        R=abs(((x1-a)**2+(y1-b)**2)**0.5)
        f=(x3-a)**2+(y3-b)**2-R**2
    return a,b,R
    
    
    raise Exception("Not implemented")

'''
    Part 5: Interpolation and Numerical differentiation
'''

'''
    We will solve problem 5.1.11 from the textbook:
        " 1. Use polynomial interpolation to compute f' and f'' at x using
          the data in x_data and y_data:
                x_data = array([-2.2, -0.3, 0.8, 1.9])
                y_data = array([15.180, 10.962, 1.920, -2.040])
          2. Given that f(x) = x**3 - 0.3*x**2 -
             8.56*x + 8.448, gauge the accuracy of the result."
'''

def interpolant_5_1_11():
    '''
    Task: return an array containing the coefficients of the polynomial
          of degree 3 interpolating the data points.
    Test: function 'test_interpolant' of 'tests/test_problem_5_1_11.py'
    Hint: use code from Chapters 2 and 3.
    '''
    ## YOUR CODE HERE

    
    x_data = array([-2.2, -0.3, 0.8, 1.9])
    y_data = array([15.180, 10.962, 1.920, -2.040])

    a = y_data.copy()
    m = x_data.size
    assert(m == y_data.size)
    for k in range(1, m): 
        for i in range(k, m): 
            a[i] = (a[i]-a[k-1])/(x_data[i]-x_data[k-1])
    a0,a1,a2,a3=a
    x0,x1,x2,x3=x_data
    c0=a0-a1*x0+a2*x0*x1-a3*x0*x1*x2
    c1=a1-a2*x1+a3*x1*x2-a2*x0+a3*x0*x2+a3*x0*x1
    c2=a2-a3*x2-a3*x1-a3*x0
    c3=a3
    return c0, c1, c2, c3
     
    raise Exception("Not implemented")

def d_dd_5_1_11(x):
    '''
    Task: return a tuple containing the value of f' and f'' at x.
    Parameter: x is the value at which f' and f'' must be computed.
    Test: function 'test_d_dd' of 'tests/test_problem_5_1_11.py'
    Example: d_dd_5_1_11(0) must return (8.56, -0.6).
    Hint: differentiate the interpolant returned by the previous function.
    '''
    ## YOUR CODE HERE

    a0,a1,a2,a3=interpolant_5_1_11()
    f1=a1+2*a2*x+3*a3*x**2
    f2=2*a2+3*2*a3*x
    return f1,f2
    
    raise Exception("Not implemented")

def error_5_1_11(x):
    '''
    Task: return a tuple containing the errors made by your previous
           approximation of f' and f'' at x.
    Parameter:  x is the value at which f' and f'' must be computed.
    Test: function 'test_error' of  'tests/test_problem_5_1_11.py'
    Example: error(0) must return
    Hint: differentiate x**3 - 0.3*x**2 - 8.56*x + 8.448 manually and compare
          the result to the output of the previous function.
    '''
    ## YOUR CODE HERE

    f1,f2=d_dd_5_1_11(x)
    e1=-8.56-f1
    e2=-0.6-f2
    return e1,e2

    raise Exception("Not implemented")
