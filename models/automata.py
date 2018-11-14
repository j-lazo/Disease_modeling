import numpy as np
import random
import copy
from matplotlib import pyplot as plt


class AutomataModel(object):

    def __init__(self, size, pop_suc, pop_inf, pop_rec):
        self.size = size
        self.pop_suc = pop_suc
        self.pop_inf = pop_inf
        self.pop_rec = pop_rec
        self.model = self.fill(self.lattice(self.size), self.pop_inf, self.pop_rec)

    def lattice(self, size):
        w = np.ones([size, size])
        return w

    def fill (self, m,  pop_inf, pop_rec):
        while pop_inf != 0:
            re_x = random.randint(0, len(m) - 1)
            re_y = random.randint(0, len(m) - 1)
            if m[re_x, re_y] != 2:
                m[re_x, re_y] = 2
                pop_inf -= 1

        while pop_rec != 0:
            re_x = random.randint(0, len(m) - 1)
            re_y = random.randint(0, len(m) - 1)
            if m[re_x, re_y] != 2 or m[re_x, re_y] != 3:
                m[re_x, re_y] = 3
                pop_rec -= 1

        return m


def count_neighbors(position_x, position_y, lim_min, lim_max, m):
    #print('neigbors', lim_min, lim_max)
    er = 0
    if position_x == lim_min:
        lower_limit_x = lim_min
    else:
        lower_limit_x = position_x -1

    if position_x == lim_max:
        up_limx = lim_max
    else:
        up_limx = position_x + 1

    if position_y == lim_min:
        low_limy = copy.copy(lim_min)
    else:
        low_limy = position_y - 1
    if position_y == lim_max:
        up_limy = lim_max
    else:
        up_limy = position_y + 1

    for i in range(lower_limit_x, up_limx):
        for j in range(low_limy, up_limy):
            if i == position_x and j == position_y:
                pass
            else:
                if m[i, j] == 2:
                    er = er+1
    #print('neighbors', er)
    return er


def simulate_SIR(lattice, prob_inf, prob_rec):
    m = copy.copy(lattice)
    lim_min = 0
    lim_max = len(m) - 1
    rand_x = random.randint(lim_min, lim_max)
    rand_y = random.randint(lim_min, lim_max)
    #print('rands',rand_x, rand_y)
    #print('lims',lim_min, lim_max)
    chosen = m[rand_x, rand_y]
    #print('chosen', chosen)
    R = count_neighbors(rand_x, rand_y, lim_min, lim_max, m)
    #print('R', R)
    #plt.figure(3)
    #plt.plot(rand_x, rand_y, 'ro')

    if chosen == 1:
        if random.random() < 1-(1-prob_inf)**R:
           # print(chosen,rand_x, rand_y)
            lattice[rand_x, rand_y] = 2
    elif chosen == 2:
       # print(chosen, rand_x, rand_y)
        if random.random() < prob_rec:
            lattice[rand_x, rand_y] = 3

    return [rand_x, rand_y]

def simulate_SIR2(lattice, prob_inf, prob_rec, prob_rrec):
    m = copy.copy(lattice)
    lim_min = 0
    lim_max = len(m) - 1
    rand_x = random.randint(lim_min, lim_max)
    rand_y = random.randint(lim_min, lim_max)
    #print('rands',rand_x, rand_y)
    #print('lims',lim_min, lim_max)
    chosen = m[rand_x, rand_y]
    #print('chosen', chosen)
    R = count_neighbors(rand_x, rand_y, lim_min, lim_max, m)
    #print('R', R)
    #plt.figure(3)
    #plt.plot(rand_x, rand_y, 'ro')

    if chosen == 1:
        if random.random() < 1-(1-prob_inf)**R:
           # print(chosen,rand_x, rand_y)
            lattice[rand_x, rand_y] = 2
    elif chosen == 2:
       # print(chosen, rand_x, rand_y)
        if random.random() < prob_rec:
            lattice[rand_x, rand_y] = 3

    elif chosen ==3:
        if random.random() < prob_rrec:
            lattice[rand_x, rand_y] = 1

    return [rand_x, rand_y]


def measure(m):
    unique, counts = np.unique(m, return_counts=True)
    d = dict(zip(unique, counts))

    if not 1 in d:
        d[1] = 0
    if not 2 in d:
        d[2] = 0
    if not 3 in d:
        d[3] = 0
    return d[1], d[2], d[3]


#if __name__ == '__main__':
#    A = AutomataModel(150, 22400, 100, 0)
#    tmax = 2
#    plt.figure()
#    for t in range(tmax):
#        ps, pi, pr = measure(A)
#        plt.imshow(A)
#        simulate_SIR(A)
