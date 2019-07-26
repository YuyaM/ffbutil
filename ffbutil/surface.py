# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019] [Yuya Miki]
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
##################################################

from .history import history

class surface(history):
    '''
    This class is utility for history-file in FrontFlow/blue
    '''
    def __init__(self):
        '''
        '''
        # print("W,H", width, height)
        self.keyword = {
            "T":       "00",
            "FX":      "01",
            "FY":      "02",
            "FZ":      "03",
            "MX":      "04",
            "MY":      "05",
            "MZ":      "06",
        }

        self.keymean= {
            "T":       "TIME                              ",
            "FX":      "FLUID FORCE ACTING IN X DIRECTION ",
            "FY":      "FLUID FORCE ACTING IN Y DIRECTION ",
            "FZ":      "FLUID FORCE ACTING IN Z DIRECTION ",
            "MX":      "FLUID FORCE MOMENT ABOUT X-AXIS   ",
            "MY":      "FLUID FORCE MOMENT ABOUT Y-AXIS   ",
            "MZ":      "FLUID FORCE MOMENT ABOUT Z-AXIS   ",
        }
        #
        # Magic number
        # この変数はHISTORYファイルを出力する仕様によって決まる
        # numSolverDefinedHeader : Header
        # numSolverDefinedValue  : ソルバ定義されたデータ数
        #
        self.numSolverDefinedHeader = 1
        self.numSolverDefinedValue = 7
