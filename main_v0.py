# -*- coding: utf-8 -*-
"""
@author: jl
"""
import numpy as np
from solvers.rk4_N import*
import matplotlib.pyplot as plt
from models.exact_solutions import*
from solvers.rk2_N import rk2_N
from solvers.euler_method import*
from models.SIS_model import SIS_model
from models.SIR_model import SIR_model
from models.SIS_model2 import SIS_model2
from models.SIR_model2 import SIR_model2


def Real_case():
    pass

def test_SIR():

    rel_err_S = []
    rel_err_I = []
    ErrS = []
    ErrI = []

    N = 22500
    x01 = 22400/N
    x02 = 100/N
    x03 = 0/N
    x0 = [x01, x02, x03] # change this according to the entries of your model

    c_1 = 1.4
    c_2 = 0.2
    consts = [c_1, c_2] # change this according to the number of constants  of your model

    initial_time = 0
    final_time = 20
    total_number_of_steps = 50
    y = rk4_N(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)

    y1, y2, y3 = [], [], []
    for ye in y[1]:
        y1.append(ye[0])
        y2.append(ye[1])
        y3.append(ye[2])

    plt.figure()
    plt.title('Solution Using a RK4 model')
    plt.plot(y[0], y1, '-o', label='S')
    plt.plot(y[0], y2, '-o', label='I')
    plt.plot(y[0], y3, '-o', label='R')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.legend(loc='best')

    sir = SIR_sol(x01, x02, x03, c_1, c_2, final_time, total_number_of_steps)
    plt.figure()
    plt.title('Comparison of the analytical and numerical solution with $\\beta =1.4 $, $\gamma = 0.2$')
    plt.plot(sir[3], sir[0], '--b', label='S, analytical solution')
    plt.plot(sir[3], sir[1], '--r', label='I, analytical solution')
    plt.plot(y[0], y1, '-ob', label='S, RK4')
    plt.plot(y[0], y2, '-or', label='I, RK4')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.legend(loc='best')

    for c in range(5):

        y = rk4_N(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)
        sir = SIR_sol(x01, x02, x03, c_1, c_2, final_time, total_number_of_steps)

        y1, y2, y3 = [], [], []
        for ye in y[1]:
            y1.append(ye[0])
            y2.append(ye[1])
            y3.append(ye[2])

        plt.figure()
        plt.title('Analytical and numerical solution with $h$='+str(final_time/total_number_of_steps))
        plt.plot(sir[3], sir[0], '--b', label='S, analytical solution')
        plt.plot(sir[3], sir[1], '--r', label='I, analytical solution')
        plt.plot(y[0], y1, '-ob', label='S, RK4')
        plt.plot(y[0], y2, '-or', label='I, RK4')
        plt.xlabel('time')
        plt.ylabel('population')
        plt.legend(loc='best')

        rel_err_I.append((np.array(y1) - np.array(sir[0]))/np.array(sir[0]))
        rel_err_S.append((np.array(y2) - np.array(sir[1]))/np.array(sir[1]))

        plt.figure()
        plt.title('Relative Error with $h$='+str(final_time/total_number_of_steps))
        plt.plot(rel_err_I[c], '.-', label='I')
        plt.plot(rel_err_S[c], '.-', label='S')
        plt.xlabel('Step')
        plt.ylabel('Error')
        plt.legend(loc='best')

        if c > 0:
            ErrS.append(calc_error(y1_p, y1, 5))
            ErrI.append(calc_error(y2_p, y2, 5))
            plt.figure()
            plt.title('Error of the numerical method with $h$=' + str(final_time / total_number_of_steps))
            plt.plot(ErrS[c-1], '.-', label='S')
            plt.plot(ErrI[c-1], '.-', label='I')
            plt.xlabel('Step')
            plt.ylabel('Error')
            plt.legend(loc='best')

        y1_p = copy.copy(y1)
        y2_p = copy.copy(y2)

        total_number_of_steps = total_number_of_steps*2

    plt.figure()
    for i, err_el in enumerate(ErrS):
        plt.title('Error obtained using 4th order RK with different step sizes')
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), err_el, '.-', label='S, $h$ = {}'.format(final_time/(2*(len(err_el)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), ErrI[i], '.-', label='I, $h$ = {}'.format(final_time/(2*(len(err_el)-1))))
        plt.xlabel('Step')
        plt.ylabel('Error')
        plt.legend(loc='best')

    plt.figure()
    for i, err_el in enumerate(rel_err_S):
        plt.title('Relative Error for different step sizes')
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), err_el, '.-', label='S, $h$ = {}'.format(final_time/(2*(len(err_el)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), rel_err_I[i], '.-', label='I, $h$ = {}'.format(final_time/(2*(len(err_el)-1))))
        plt.xlabel('Step')
        plt.ylabel('Error')
        plt.legend(loc='best')

    for i, err_el in enumerate(ErrS):
        plt.figure()
        plt.title('Comparison of the errors')
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), err_el, '.-', label='S error ($h$ = {})'.format(final_time/(2*(len(err_el)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(err_el)), ErrI[i], '.-', label='I error ($h$ = {})'.format(final_time/(2*(len(err_el)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(rel_err_S[i+1])), rel_err_S[i+1], '+-', label='S, relative error($h$ = {})'.format(final_time/(2*(len(err_el)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(rel_err_I[i+1])), rel_err_I[i+1], '+-', label='I, relative error($h$ = {})'.format(final_time/(2*(len(err_el)-1))))
        plt.xlabel('Step')
        plt.ylabel('Error')
        plt.legend(loc='best')

    # this part is part is to play with the different values of your model, if you need it uncomment

    """
    #c_1s = [0.1, 0.3, 0.4, 0.6, 0.9, 1.4, 1.5, 1.9, 2.0, 2.1]
    #c_1s = [0.05, 0.1, 0.2, 0.5, 1.1, 1.4, 1.7, 1.9, 2.1, 2.5, 2.5]
    #c_1s = [2.0, 2.1, 2.3, 2.5, 2.9, 4.1]
    #c_1s = [0.1, 0.3, 0.4, 0.6, 0.9]
    #c2s = [0.0005, 0.01, 0.05, 0.1]


    c_1s = [0.1, 0.5, 0.9, 1.2, 1.4]
    c2s = [0.2]
    final_time = 10
    
    for c_2 in c2s:
        for c_1 in c_1s:

            consts[0] = c_1
            consts[1] = c_2
            j = rk4_N(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)
            g = rk2_N(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)
            e = euler_method(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)
            sir = SIR_sol(x01, x02, x03, c_1, c_2, final_time, total_number_of_steps)

            g1, g2, g3 = [], [], []
            j1, j2, j3 = [], [], []
            e1, e2, e3, = [], [], []
            for je in j[1]:
                j1.append(je[0])
                j2.append(je[1])
                j3.append(je[2])

            for ge in g[1]:
                g1.append(ge[0])
                g2.append(ge[1])
                g3.append(ge[2])

            for ee in e[1]:
                e1.append(ee[0])
                e2.append(ee[1])
                e3.append(ee[2])

            plt.figure()
            plt.title("".join(['c1 = ', str(c_1), ',', 'c2 = ', str(c_2)]))

            plt.plot(j[0], j1, 'xb')
            plt.plot(j[0], j2, 'xr')

            plt.plot(g[0], g1, '^b')
            plt.plot(g[0], g2, '^r')

            plt.plot(e[0], e1, 'ob')
            plt.plot(e[0], e2, 'or')

            plt.plot(sir[3], sir[0], '--b')
            plt.plot(sir[3], sir[1], '--r')
            plt.figure()
            plt.title('Exact Solution')
            plt.plot(sir[3], sir[0], '--b')
            plt.plot(sir[3], sir[1], '--r')
            """


def test_SIS():
    N = 22500
    x01 = 22400/N
    x02 = 100/N
    x03 = 0/N

    x0 = [x01, x02]

    initial_time = 0
    final_time = 20
    total_number_of_steps = 50

    c_1s = [0.1, 0.2, 0.3, 0.4, 0.6, 0.9, 1.1]
    c_1s = [0.9]
    c_2 = 0.01

    # to save the relative errors
    Errk2i = []
    Errk2s = []
    Errk4i = []
    Errk4s = []
    Erre2i = []
    Erre2s = []

    # to save the errors

    Ee_rk4s = []
    Ee_rk4i = []
    Ee_rk2s = []
    Ee_rk2i = []
    Ee_euls = []
    Ee_euli = []

    for i in range(5):
        for c_1 in c_1s:
            consts = [c_1, c_2]  # change this according to the number of constants  of your model
            consts[0] = c_1
            j = rk4_N(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)
            g = rk2_N(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)
            e = euler_method(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)

            g1, g2, g3 = [], [], []
            j1, j2, j3 = [], [], []
            e1, e2, = [], []
            for je in j[1]:
                j1.append(je[0])
                j2.append(je[1])

            for ge in g[1]:
                g1.append(ge[0])
                g2.append(ge[1])

            for ee in e[1]:
                e1.append(ee[0])
                e2.append(ee[1])

            plt.figure()
            plt.title('Simulation of the SIS model with $\\beta$ = ' + str(c_1) + ' and  $\gamma$ = ' + str(c_2))

            plt.plot(j[0], j1, 'xr', label='S, 4th order RK')
            plt.plot(j[0], j2, 'xb', label='I, 4th order RK')

            plt.plot(g[0], g1, '^r', label='S, 2nd order RK')
            plt.plot(g[0], g2, '^b', label='I, 2nd order RK')

            plt.plot(e[0], e1, 'or', label='S, forward Euler Method ')
            plt.plot(e[0], e2, 'ob', label='I, forward Euler Method')

            sis = SIS_sol(x01, x02, c_1, c_2, final_time, total_number_of_steps)
            plt.plot(sis[2], sis[0], '--r', label='S, exact solution')
            plt.plot(sis[2], sis[1], '--b', label='I, exact solution')
            plt.ylabel('Population')
            plt.xlabel('time')
            plt.legend(loc='best')

            # Calculating the relative error
            g1 = np.array(g1)
            g2 = np.array(g2)
            j1 = np.array(j1)
            j2 = np.array(j2)
            e1 = np.array(e1)
            e2 = np.array(e2)
            si0 = np.array(sis[0][:])
            si1 = np.array(sis[1][:])

            erk2i = (g1 - si0) / si0
            erk2s = (g2 - si1) / si1
            erk4i = (j1 - si0) / si0
            erk4s = (j2 - si1) / si1
            ee2i = (e1 - si0) / si0
            ee2s = (e2 - si1) / si1

            Errk2i.append(erk2s)
            Errk2s.append(erk2i)
            Errk4i.append(erk4s)
            Errk4s.append(erk4i)
            Erre2i.append(ee2s)
            Erre2s.append(ee2i)

            plt.figure()
            plt.title('Relative error of the SIS model with $\\beta$ = ' + str(c_1) + ' and  $\gamma$ = ' + str(c_2))
            plt.plot(sis[2], erk2i, '-*', label='S, 2nd order RK')
            plt.plot(sis[2], erk2s, '-*', label='I, 2nd order RK')
            plt.plot(sis[2], erk4i, '-*', label='S, 4th order RK')
            plt.plot(sis[2], erk4s, '-*', label='I, 4th order RK')
            plt.plot(sis[2], ee2i, '-*', label='S, Forward Euler Method')
            plt.plot(sis[2], ee2s, '-*', label='I, Forward Euler Method')
            plt.ylabel('Relative error')
            plt.legend(loc='best')

            if i > 0:

                E_rk4s = calc_error(js_p, j1, 5)
                E_rk4i = calc_error(ji_p, j2, 5)
                E_rk2s = calc_error(gs_p, g1, 3)
                E_rk2i = calc_error(gi_p, g2, 3)
                E_euls = calc_error(es_p, e1, 2)
                E_euli = calc_error(ei_p, e2, 2)

                Ee_rk4s.append(E_rk4s)
                Ee_rk4i.append(E_rk4i)
                Ee_rk2s.append(E_rk2s)
                Ee_rk2i.append(E_rk2i)
                Ee_euls.append(E_euls)
                Ee_euli.append(E_euli)

                plt.figure()
                plt.title('Error with $h$ = {}'.format(final_time/total_number_of_steps))
                plt.plot(E_euls, '-+', label='S, Euler Method')
                plt.plot(E_euli, '-+', label='I, Euler Method')
                plt.plot(E_rk2s, '-+', label='S, RK 2nd order')
                plt.plot(E_rk2i, '-+', label='I, RK 2nd order')
                plt.plot(E_rk4s, '-+', label='S, RK 4th order')
                plt.plot(E_rk4i, '-+', label='I, RK 4th order')
                plt.ylabel('Error')
                plt.xlabel('Step')
                plt.legend(loc='best')

            js_p = copy.copy(j1)
            gs_p = copy.copy(g1)
            es_p = copy.copy(e1)
            ji_p = copy.copy(j2)
            gi_p = copy.copy(g2)
            ei_p = copy.copy(e2)
            total_number_of_steps = int(total_number_of_steps * 2)
    plt.figure()
    plt.title('Calculation of the error for difference size steps using a 4th RK Method')
    for j, arr in enumerate(Ee_rk4s):
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), arr, '-.', label='S, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), Ee_rk4i[j], '-.', label='I, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.ylabel('Error')
        plt.xlabel('Step')
        plt.legend(loc='best')

    plt.figure()
    plt.title('Calculation of the error for difference size steps using a 2nd RK Method')
    for j, arr in enumerate(Ee_rk2s):
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), arr, '-.', label='S, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), Ee_rk2i[j], '-.', label='I, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.ylabel('Error')
        plt.xlabel('Step')
        plt.legend(loc='best')

    plt.figure()
    plt.title('Calculation of the error for difference size steps using Euler Method')
    for j, arr in enumerate(Ee_euls):
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), arr, '-.', label='S, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.plot(np.linspace(initial_time, final_time + 1, len(arr)), Ee_euli[j], '-.', label='I, $h$ = {}'.format(final_time/(2*(len(arr)-1))))
        plt.ylabel('Error')
        plt.xlabel('Step')
        plt.legend(loc='best')


    # to test the variable 2
    """c_1 = 0.2
    c_2s = [0.01, 0.05, 0.1, 0.5, 0.9, 1.1, 1.5]
    
    for c_2 in c_2s:
        consts = [c_1, c_2]  # change this according to the number of constants  of your model
        consts[0] = c_1
        j = rk4_N(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)
        g = rk2_N(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)
        e = euler_method(SIS_model, x0, consts, initial_time, final_time, total_number_of_steps)
    
        g1, g2, g3 = [], [], []
        j1, j2, j3 = [], [], []
        e1, e2, = [], []
        for je in j[1]:
            j1.append(je[0])
            j2.append(je[1])
    
        for ge in g[1]:
            g1.append(ge[0])
            g2.append(ge[1])
    
        for ee in e[1]:
            e1.append(ee[0])
            e2.append(ee[1])
    
        plt.figure()
        plt.title('Simulation of the SIS model with $\\beta$ = ' + str(c_1) + ' and  $\gamma$ = ' + str(c_2))
    
        plt.plot(j[0], j1, 'xr', label='S, 4th order RK')
        plt.plot(j[0], j2, 'xb', label='I, 4th order RK')
    
        plt.plot(g[0], g1, '^r', label='S, 2nd order RK')
        plt.plot(g[0], g2, '^b', label='I, 2nd order RK')
    
        plt.plot(e[0], e1, 'or', label='S, forward Euler Method ')
        plt.plot(e[0], e2, 'ob', label='I, forward Euler Method')
    
        sis = SIS_sol(x01, x02, c_1, c_2, final_time)
        plt.plot(sis[0], '--r', label='S, exact solution')
        plt.plot(sis[1], '--b', label='I, exact solution')
        plt.ylabel('Population')
        plt.xlabel('time')
        plt.legend(loc='best')"""


def calc_error(a_h, a_2h, m):
    a_2h= np.array([element for i, element in enumerate(a_2h) if i % 2 == 0])
    return (a_h - a_2h)/(2**m-1)



def main():
    test_SIR()

if __name__ == '__main__':
    main()
    plt.show()
