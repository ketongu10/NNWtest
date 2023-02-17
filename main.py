from Utils.Clibs.fib.fib import Fib
import NNW.simpleNNW as nw
import numpy as np
from time import time
from NNW.vistest import *

if __name__ == '__main__':
    network = DrawNN([2, 8, 8, 8])
    network.draw()
    """data = np.array([
        [-2, -1],  # Alice
        [25, 6],  # Bob
        [17, 4],  # Charlie
        [-15, -6],  # Diana
    ])

    all_y_trues = np.array([
        1,  # Alice
        0,  # Bob
        0,  # Charlie
        1,  # Diana
    ])

    # Тренируем нашу нейронную сеть!
    network = nw.OurNeuralNetwork()
    t0 = time()
    network.train(data, all_y_trues)
    print("total time %.3f s" % (time()-t0))

    emily = np.array([-7, -3])  # 128 фунтов, 63 дюйма
    frank = np.array([20, 2])  # 155 фунтов, 68 дюймов
    print("Emily: %.3f" % network.feedforward(emily))  # 0.951 - F
    print("Frank: %.3f" % network.feedforward(frank))  # 0.039 - M"""





