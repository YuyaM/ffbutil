# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019] [Yuya Miki]
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
##################################################

"""
Created on Mon Jul 10 15:33:23 2017

@author: yuyam
"""

# This is code for reading FFBs HISTORY & SAMPLX file.
###################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate
###################################
# Font
line_of_axes = 1.0
plt.rcParams.update({
    'axes.grid': True,
    'font.family': 'Arial',
    'font.size': 12.0,
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'legend.edgecolor': 'black',
    'legend.fancybox': False,
    'legend.framealpha': 1.0,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'axes.linewidth': line_of_axes,
    'xtick.major.width': line_of_axes,
    'ytick.major.width': line_of_axes,
    'xtick.minor.width': line_of_axes,
    'ytick.minor.width': line_of_axes,
})
inch2mm = 2.54
# 1. [inches] single-column figure size
width = 8.0 / inch2mm
# golden ratio
# height = width / 1.618
# same ratio
height = width
fontsizefig = 8.0
extension = ".jpg"
fig_dpi = 300
# print("W,H", width, height)


class samplx:
    '''
    This class is utility for samplx in FrontFlow/blue
    '''

    def __init__(self):
        print("Init readdata")

    def read_source(self, file_in):
        '''
        read_source(filename_input)
        This function read source file of samplx
        You should specify the filename you want to read.
        '''
        self.f_data = pd.read_csv(file_in, skiprows=1, header=None, delim_whitespace=True, skipinitialspace=True)
        self.f_data.columns = ["x", "y", "z"]

    def remove_duplicate(self, string):
        '''
        remove_duplicate(direction)
        This function duplicates the source data.
        You should input the direction('x', 'y', 'z').
        '''
        self.f_data = self.f_data.drop_duplicates([string])

    def get_source(self, string):
        '''
        get_source(direction)
        This function returns the data of the source.
        You should input the direction('x', 'y', 'z').
        '''
        if string == 'x':
            res = np.array(self.f_data['x'])
        elif string == 'y':
            res = np.array(self.f_data['y'])
        elif string == 'z':
            res = np.array(self.f_data['z'])
        return res

    def read(self, file_in):
        '''
        read_samplx(filename_input):
        This function read result file of samplx.
        You should specify the filename of the result file you want to read.
        '''
        # x,y,z,u,v,w,p,pp
        self.data = np.loadtxt(file_in, skiprows=0)
        self.x = self.data[:, 0]
        self.y = self.data[:, 1]
        self.z = self.data[:, 2]
        self.u = self.data[:, 3]
        self.v = self.data[:, 4]
        self.w = self.data[:, 5]
        self.p = self.data[:, 6]
        if(np.shape(self.data)[1] > 6):
            self.k = self.data[:, 7]
        # self.value = self.data[:, 3:]

    def get(self, string):
        '''
        get(value):
        This function returns the data of the samplx.
        You should input which value you want.
        ('x', 'y', 'z', 'u', 'v', 'w', 'p', 'k').
        '''
        if string == 'x':
            res = np.array(self.x)
        elif string == 'y':
            res = np.array(self.y)
        elif string == 'z':
            res = np.array(self.z)
        elif string == 'u':
            res = np.array(self.u)
        elif string == 'v':
            res = np.array(self.v)
        elif string == 'w':
            res = np.array(self.w)
        elif string == 'p':
            res = np.array(self.p)
        elif string == 'k':
            res = np.array(self.k)
        return res

    def plot(self, str0, str1):
        '''
        plot(str0, str1):
        This function returns the data of the samplx.
        You should input which value you want.
        ('x', 'y', 'z', 'u', 'v', 'w', 'p', 'k').
        '''
        string = []
        string.append(str0)
        string.append(str1)
        result = []

        for i in range(2):
            if string[i] == 'x':
                res = np.array(self.x)
            elif string[i] == 'y':
                res = np.array(self.y)
            elif string[i] == 'z':
                res = np.array(self.z)
            elif string[i] == 'u':
                res = np.array(self.u)
            elif string[i] == 'v':
                res = np.array(self.v)
            elif string[i] == 'w':
                res = np.array(self.w)
            elif string[i] == 'p':
                res = np.array(self.p)
            elif string[i] == 'k':
                res = np.array(self.k)
            elif string[i] == 'xd':
                res = np.array(self.xd)
            elif string[i] == 'yd':
                res = np.array(self.yd)
            elif string[i] == 'zd':
                res = np.array(self.zd)
            elif string[i] == 'ud':
                res = np.array(self.ud)
            elif string[i] == 'vd':
                res = np.array(self.vd)
            elif string[i] == 'wd':
                res = np.array(self.wd)
            elif string[i] == 'pd':
                res = np.array(self.pd)
            elif string[i] == 'kd':
                res = np.array(self.kd)
            else:
                res = np.array(self.value)
            result.append(res)
        plt.plot(result[0], result[1], '.-k', label="Present")
        # plt.show()

    def xlog(self):
        plt.xscale('log')

    def ylog(self):
        plt.yscale('log')

    def show(self):
        plt.show()

    def define(self, res):
        self.value = res

    def calc_delta(self, viscosity, inner_scale):
        # check
        umax = max(self.u)
        print(umax, 'umax')
        # self.u = self.u / umax
        # utau_wall
        utau2 = np.sqrt(viscosity * self.u[1] / self.y[1])
        utau = utau2
        # if flag:
        #     utau1 = np.sqrt(0.50 * surfcf1 / umax**2)
        #     print('URLES utau1, utau2', utau1, utau2)
        #     utau = utau1
        # else:
        #     utau = utau2

        dtheta = self.u * (1 - self.u)
        theta = scipy.integrate.simps(dtheta, self.y)
        self.retheta = theta / viscosity
        vislen = viscosity / utau
        # uinf = 1.0
        uinf = umax
        tck = scipy.interpolate.interp1d(self.u, self.y, kind='zero')
        delta99 = tck(0.99)
        if inner_scale == "yes":
            rep_U = utau
            rep_L = vislen
        else:
            rep_U = uinf
            rep_L = delta99
        rep_SC = (rep_U**3) / rep_L
        rep_U2 = rep_U**2
        self.xd = self.x / rep_L
        self.yd = self.y / rep_L
        self.zd = self.z / rep_L
        self.ud = self.u / rep_U
        self.vd = self.v / rep_U
        self.wd = self.w / rep_U
        self.pd = self.p / rep_SC
        self.kd = self.k / rep_U2
        return [rep_U, rep_L, rep_SC, rep_U2]

    def mean_spanwise_cp(self, savename, rms_flag):
        '''
        def mean_spanwise_cp(self, savename, rms_flag):
        average each x
        make figure(x: x/C, y: Cp,Cp')

        Input
        savename : filename
        ex) fig.png fig.jpg fig.tiff
        rms_flag : 0 Cp
                 : 1 Cp'(RMS)
        Output   : figure
        magic = 1.008930411365E0
        '''
        print(savename)
        unique_x = np.unique(self.x)
        CpP = np.zeros_like(unique_x)
        CpM = np.zeros_like(unique_x)
        # print(unique_x)
        for i in range(unique_x.size):
            # print(unique_x[i])
            CpP[i] = 2.0 * self.p[((self.data[:, 1] >= 0.0) & (self.data[:, 0] == unique_x[i]))].mean()
            CpM[i] = 2.0 * self.p[((self.data[:, 1] <= 0.0) & (self.data[:, 0] == unique_x[i]))].mean()
        plt.figure(figsize=(width, height), dpi=fig_dpi)
        plt.plot(unique_x, CpP, '-k', label="Present")
        if(rms_flag == 0):
            plt.plot(unique_x, CpM, '-k')
            plt.plot(self.yc, self.mean, 'or', label="Exp.", markerfacecolor='#ffffff')
        plt.xlim([0.0, 1.0])
        if(rms_flag):
            plt.ylim([0.0, 0.3])
            plt.ylabel("$C_p'(RMS)$")
            plt.plot(self.yc, self.rms, 'or', label="Exp.", markerfacecolor='#ffffff')
        else:
            plt.ylim([1.5, -4.0])
            plt.ylabel("$C_p$")
        plt.xlabel("x/C")
        plt.legend(loc='best', fancybox=False, framealpha=1.0, edgecolor='black', fontsize=10)
        plt.savefig(savename, dpi=fig_dpi, bbox_inches="tight")
        plt.clf()
