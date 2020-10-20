# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019] [Yuya Miki]
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
##################################################

"""
@author: yuyam
"""

import numpy as np
import pandas as pd


class parmles3x:
    '''
    This class is utility for parameter file in FrontFlow/blue
    '''

    def __init__(self):
        print("Init class parmles3x")

    def read(self, file_in):
        '''
        def read(self, file_in):
        This function can read PARMLES3X.
        '''
        param = open(file_in)
        line = param.readlines()
        param.close()
        num_sharp = 0
        row_number = 0
        for string in line:
            row_number += 1
            if(num_sharp == 3 and string[0] != "#"):
                str_blank = line[row_number - 1]
                str_arr = str_blank.split()
                ITRANS = int(str_arr[0])
                IMODEL = int(str_arr[1])
                IFORM = int(str_arr[2])
                IPRESS = int(str_arr[3])
                FSMACH = float(str_arr[4])
            if(num_sharp == 7 and string[0] != "#"):
                str_blank = line[row_number - 1]
                str_arr = str_blank.split()
                VISCM = float(str_arr[0])
            if(num_sharp == 9 and string[0] != "#"):
                str_blank = line[row_number - 1]
                str_arr = str_blank.split()
                ISTART = int(str_arr[0])
                NTIME = int(str_arr[1])
                DT = float(str_arr[2])
            # Stage 2
            # HISTORY plot data is exist
            # after (#GIVE NSMPL  LSMPL  XSMPL  YSMPL ZSMPL)
            # num_sharp represents number of "#"
            if(num_sharp == 13):
                num = int(string[:])
                num_sharp = -1
                data = np.loadtxt(line[row_number:row_number + num])
                break
            # Stage 1
            if(string[0] == "#"):
                num_sharp += 1
        # print(data)
        print('ITRANS       : {} '.format(ITRANS))
        print('IMODEL       : {} '.format(IMODEL))
        print('IFORM        : {} '.format(IFORM))
        print('IPRESS       : {} '.format(IPRESS))
        print('FSMACH       : {} '.format(FSMACH))
        print('Restart flag       : {} '.format(ISTART))
        print('Viscosity (/nu)    : {viscosity} '.format(viscosity=VISCM))
        print('Number of step     : {} '.format(NTIME))
        print('Time per step (dt) : {} '.format(DT))
        print('Number of sampling : {} '.format(num))
        self.itrans = ITRANS
        self.imodel = IMODEL
        self.iform  = IFORM
        self.ipress = IPRESS
        self.fsmach = FSMACH
        self.istart = ISTART
        self.viscm  = VISCM
        self.ntime  = NTIME
        self.dt     = DT
        self.num    = NUM
        self.f_data = pd.DataFrame(data)
        self.f_data.columns = ["dir", "x", "y", "z"]
        self.f_data = self.f_data.drop_duplicates(["x", "y", "z"])
        # data contains array of [(1 2 3 4) X Y Z]
        # 1:U, 2:V, 3:W, 4:P

    def print_data(self, directions):
        '''
        def print_data(self, directions):
        # directions 'x', 'y', 'z'
        '''
        print(self.f_data[directions])

    def get_xyz(self, directions):
        '''
        get_xyz(self, directions):
        # directions 'x', 'y', 'z'
        '''
        return self.f_data[directions]

    def get_itrans():
        return self.itrans

    def get_imodel():
        return self.imodel

    def get_iform():
        return self.iform

    def get_ipress():
        return self.ipress

    def get_fsmach():
        return self.fsmach

    def get_istart():
        return self.istart

    def get_viscm():
        return self.viscm

    def get_ntime():
        return self.ntime

    def get_dt():
        return self.dt

    def get_num():
        return self.num

