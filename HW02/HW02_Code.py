import numpy as np 
import matplotlib.pyplot as plt
import numpy # import again
import numpy.linalg
import numpy.random
import hashlib


def generate_data(Para1, Para2, seed=0):
    """Generate binary random data

    Para1, Para2: dict, {str:float} for each class, 
      keys are mx (center on x axis), my (center on y axis), 
               ux (sigma on x axis), ux (sigma on y axis), 
               y (label for this class)
    seed: int, seed for NUMPy's random number generator. Not Python's random.

    """
    numpy.random.seed(seed)
    X1 = numpy.vstack((numpy.random.normal(Para1['mx'], Para1['ux'], Para1['N']), 
                       numpy.random.normal(Para1['my'], Para1['uy'], Para1['N'])))
    X2 = numpy.vstack((numpy.random.normal(Para2['mx'], Para2['ux'], Para2['N']), 
                       numpy.random.normal(Para2['my'], Para2['uy'], Para2['N'])))
    Y = numpy.hstack((Para1['y']*numpy.ones(Para1['N']),
                       Para2['y']*numpy.ones(Para2['N'])))
    X = numpy.hstack((X1, X2)) 
    X = numpy.transpose(X)
    return X, Y 


def plot_data_hyperplane(X, y, w, filename):
    """
    X: 2-D numpy array, each row is a sample, not augmented 
    y: 1-D numpy array, the labels 
    w: 1-by-3 numpy array, the last element of which is the bias term

    Examples
    --------------

    >>> X = numpy.array([[1,2], \
                         [4,5], \
                         [7,8]]) 
    >>> y = numpy.array([1,-1,1])
    >>> w = [1, 2, -10]
    >>> filename = "test.png"
    >>> plot_data_hyperplane(X, y, w, filename)
    >>> hashlib.md5(open(filename, 'rb').read()).hexdigest()
    '37f373b22ce2ebd3bae54b6a39810fc7'
    """

    # your code here
    x1 = X[y == +1]
    x2 = X[y == -1]
    #plt.plot(x1[:, 0], x1[:, 1], 'ro')
    #plt.plot(x2[:, 0], x2[:, 1], 'bo')
    #plt.show()

    x_ticks = numpy.array([numpy.min(X[:, 0]), numpy.max(X[:, 0])])
    y_ticks = -1 * (x_ticks * w[0] + w[2]) / w[1]
    plt.plot(x1[:, 0], x1[:, 1], 'ro')
    plt.plot(x2[:, 0], x2[:, 1], 'bo')
    plt.plot(x_ticks, y_ticks, 'k-')
    plt.xlim(numpy.min(X[:, 0]), numpy.max(X[:, 0]))
    plt.ylim(numpy.min(X[:, 1]), numpy.max(X[:, 1]))
    plt.savefig(filename)
    #plt.show()
    plt.close('all')


def plot_mse(x, y, filename):
    """
    X: 2-D numpy array, each row is a sample, not augmented 
    y: 1-D numpy array

    Examples
    -----------------
    >>> X,y = generate_data(\
        {'mx':1,'my':2, 'ux':0.1, 'uy':1, 'y':1, 'N':20}, \
        {'mx':2,'my':4, 'ux':.1, 'uy':1, 'y':-1, 'N':50},\
        seed=10)
    >>> plot_mse(X, y, 'test1.png')
    array([-1.8650779 , -0.03934209,  2.91707992])
    >>> X,y = generate_data(\
    {'mx':1,'my':-2, 'ux':0.1, 'uy':1, 'y':1, 'N':20}, \
    {'mx':-1,'my':4, 'ux':.1, 'uy':1, 'y':-1, 'N':50},\
    seed=10)
    >>> # print (X, y)
    >>> plot_mse(X, y, 'test2.png')
    array([ 0.93061084, -0.01833983,  0.01127093])
    """
    #w = np.array([0,0,0]) # just a placeholder

    # your code here
    #print(x, y)
    x_t = numpy.transpose(x)
    aug_x_t = numpy.vstack((x_t, numpy.ones(len(x_t[0]))))
    prod1 = numpy.matmul(aug_x_t, numpy.transpose(aug_x_t))
    prod2 = numpy.matmul(numpy.linalg.inv(prod1), aug_x_t)
    w = numpy.matmul(prod2, y)

    # Plot after you have w.
    plot_data_hyperplane(x, y, w, filename)

    return w


def plot_fisher(x, y, filename):
    """
    X: 2-D numpy array, each row is a sample, not augmented 
    y: 1-D numpy array

    Examples
    -----------------
    >>> X,y = generate_data(\
        {'mx':1,'my':2, 'ux':0.1, 'uy':1, 'y':1, 'N':20}, \
        {'mx':2,'my':4, 'ux':.1, 'uy':1, 'y':-1, 'N':50},\
        seed=10)
    >>> plot_fisher(X, y, 'test3.png')
    array([-1.61707972, -0.0341108 ,  2.54419773])
    >>> X,y = generate_data(\
        {'mx':-1.5,'my':2, 'ux':0.1, 'uy':2, 'y':1, 'N':200}, \
        {'mx':2,'my':-4, 'ux':.1, 'uy':1, 'y':-1, 'N':50},\
        seed=1)
    >>> plot_fisher(X, y, 'test4.png')
    array([-1.54593468,  0.00366625,  0.40890079])
    """

    w = np.array([0,0,0]) # just a placeholder

    # your code here
    #print(x, y)
    x1 = x[y == 1]
    x2 = x[y == -1]
    m1 = numpy.mean(x1, axis = 0)
    m2 = numpy.mean(x2, axis = 0)
    x1_t = numpy.transpose(x1)
    m1_t = numpy.transpose(numpy.array([m1]*len(x1)))
    x2_t = numpy.transpose(x2)
    m2_t = numpy.transpose(numpy.array([m2]*len(x2)))

    x_i = numpy.hstack((x1_t, x2_t))
    m_i = numpy.hstack((m1_t, m2_t))

    s_i = numpy.matmul((x_i-m_i), numpy.transpose(x_i-m_i))
    inc_w = numpy.matmul(numpy.linalg.inv(s_i), m1-m2)
    m = (m1+m2)/2
    w_b = -numpy.matmul(numpy.transpose(inc_w),m)
    w = numpy.hstack((inc_w, w_b))

    # Plot after you have w. 
    plot_data_hyperplane(x, y, w, filename)
    return w


if __name__ == "__main__":

    import doctest
    doctest.testmod()
