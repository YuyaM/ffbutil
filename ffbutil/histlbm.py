# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019-2021] [Yuya Miki]
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
##################################################

from .history import history

class histlbm(history):
    '''
    This class is utility for history-file in FrontFlowX
    '''
    def __init__(self):
        '''
        '''
        # print("W,H", width, height)
        self.keyword = {
            "TIME":       "00",
            "MAXRHO":     "01",
            "MAXVEL":     "02",
            "FORC_X":     "03",
            "FORC_Y":     "04",
            "FORC_Z":     "05",
        }

        self.keymean= {
            "TIME":       "TIME                              ",
            "MAXRHO":     "MAXIMUM DENSITY                   ",
            "MAXVEL":     "MAXIMUM VELOCITY                  ",
            "FORC_X":      "FLUID FORCE ACTING IN X DIRECTION ",
            "FORC_Y":      "FLUID FORCE ACTING IN Y DIRECTION ",
            "FORC_Z":      "FLUID FORCE ACTING IN Z DIRECTION ",
        }
        #
        # Magic number
        # この変数はHISTORYファイルを出力する仕様によって決まる
        # numSolverDefinedHeader : Header
        # numSolverDefinedValue  : ソルバ定義されたデータ数
        #
        self.numSolverDefinedHeader = 1
        self.numSolverDefinedValue = 3
