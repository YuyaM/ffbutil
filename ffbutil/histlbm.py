# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019] [Yuya Miki]
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
        }

        self.keymean= {
            "TIME":       "TIME                              ",
        }
        #
        # Magic number
        # この変数はHISTORYファイルを出力する仕様によって決まる
        # numSolverDefinedHeader : Header
        # numSolverDefinedValue  : ソルバ定義されたデータ数
        #
        self.numSolverDefinedHeader = 1
        self.numSolverDefinedValue = 1
