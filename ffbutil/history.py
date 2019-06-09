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
################################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
################################################################################


class history:
    '''
    This class is utility for history-file in FrontFlow/blue
    '''
    def __init__(self):
        '''
        '''
        # print("W,H", width, height)
        self.keyword = {
            "TIME":        "00",
            "MAXDIV":      "01",
            "AELMNU":      "02",
            "PRSITR":      "03",
            "PRSL2N":      "04",
            "FORC_X":      "05",
            "FORC_Y":      "06",
            "FORC_Z":      "07",
            "UEQITR":      "08",
            "VEQITR":      "09",
            "WEQITR":      "10",
            "TEQITR":      "11",
            "KEQITR":      "12",
            "EEQITR":      "13",
            "UEQL2N":      "14",
            "VEQL2N":      "15",
            "WEQL2N":      "16",
            "TEQL2N":      "17",
            "KEQL2N":      "18",
            "EEQL2N":      "19",
            "TEMPVI":      "20",
            "OVSERR":      "21",
            "TOTALV":      "22",
            "VF_MIN":      "23",
            "VF_MAX":      "24",
            "VOFCFL":      "25",
            "INLTFL":      "26",
            "OTLTFL":      "27",
        }

        self.keymean= {
            "TIME":        "TIME                                  ",
            "MAXDIV":      "MAXIMUM DIVERGENT                     ",
            "AELMNU":      "AVERAGE ELEMENT EDDY VISCOSITY        ",
            "PRSITR":      "ITERATIONS DONE FOR PRESSURE EQUATION ",
            "PRSL2N":      "L2-NORM RESIDUAL OF PRESSURE EQUATION ",
            "FORC_X":      "FLUID FORCE ACTING IN X DIRECTION ",
            "FORC_Y":      "FLUID FORCE ACTING IN Y DIRECTION ",
            "FORC_Z":      "FLUID FORCE ACTING IN Z DIRECTION ",
            "UEQITR":      "ITERATIONS DONE FOR U-EQUATION    ",
            "VEQITR":      "ITERATIONS DONE FOR V-EQUATION    ",
            "WEQITR":      "ITERATIONS DONE FOR W-EQUATION    ",
            "TEQITR":      "ITERATIONS DONE FOR T-EQUATION    ",
            "KEQITR":      "ITERATIONS DONE FOR K-EQUATION    ",
            "EEQITR":      "ITERATIONS DONE FOR E-EQUATION    ",
            "UEQL2N":      "L2-NORM RESIDUAL OF U-EQUATION    ",
            "VEQL2N":      "L2-NORM RESIDUAL OF V-EQUATION    ",
            "WEQL2N":      "L2-NORM RESIDUAL OF W-EQUATION    ",
            "TEQL2N":      "L2-NORM RESIDUAL OF T-EQUATION    ",
            "KEQL2N":      "L2-NORM RESIDUAL OF K-EQUATION    ",
            "EEQL2N":      "L2-NORM RESIDUAL OF E-EQUATION    ",
            "TEMPVI":      "VOLUME INTEGRATION OF TEMPRATURE  ",
            "OVSERR":      "MAX. OVERSET ERROR                ",
            "TOTALV":      "TOTAL VOLUME OF FIRST FLUID       ",
            "VF_MIN":      "MINIMUM VOLUME FRACTION           ",
            "VF_MAX":      "MAXMUM VOLUME FRACTION            ",
            "VOFCFL":      "MAXMUM COURANT NUMBER FOR VOF EQ. ",
            "INLTFL":      "FLUX ON INLET BOUNDARY  ",
            "OTLTFL":      "FLUX ON OUTLET BOUNDARY ",
        }



    def read(self, file_in, u00, l00):
        '''
        '''
        print("read HISTORY data. file=", file_in)
        #
        #
        self.f_in = file_in
        self.u00 = u00
        self.l00 = l00
        #
        # Magic number
        # この変数はHISTORYファイルを出力する仕様によって決まる
        # numSolverDefinedHeader : Header
        # numSolverDefinedValue  : ソルバ定義されたデータ数
        #
        numSolverDefinedHeader = 5
        numSolverDefinedValue = 28
        self.numSolverDefinedValue = numSolverDefinedValue
        #
        # READ FIRST COMMENTOUT ROWS NUMBER
        # ヘッダの数の検索 : numOfDataHeader
        # 記録されている時間ステップの検索 : numOfTimeStep
        # ファイルを実際に開いて読み込みテストを行う
        f = open(self.f_in)
        numOfDataHeader = 0
        numOfTimeStep = 0
        line = f.readline()
        numOfDataHeader = numOfDataHeader + 1
        print(numOfDataHeader, line.rstrip())
        while line:
            line = f.readline()
            if not line:
                break
            if(line[0] == "#"):
                numOfDataHeader = numOfDataHeader + 1
                print(numOfDataHeader, line.rstrip())
                criteriaData=line.split()
            else:
                numOfTimeStep = numOfTimeStep + 1
        f.close
        print("numOfDataHeader,numOfTimeStep is ", numOfDataHeader,  numOfTimeStep)
        #
        # READ default VALUE(Pre-defined Value)
        #
        preDefineHeader = pd.read_csv(self.f_in, header=None, skiprows=numSolverDefinedHeader, nrows=numSolverDefinedValue, sep='#', skipinitialspace=True)
        #
        # READ POTISION
        #
        # numUserDefinedValue is data lenght
        numUserDefinedValue = numOfDataHeader - (numSolverDefinedHeader + numSolverDefinedValue)
        if(len(criteriaData) == 9):
            col_names = ['#', 'dir', ';', 'X', 'Xvalue', 'Y', 'Yvalue', 'Z', 'Zvalue']
            flagSplit = 0
            flagNoUserDefinedData = 0
        elif(len(criteriaData) == 6):
            col_names = ['#', 'dir', ';', 'XV', 'YV', 'ZV']
            flagSplit = 1
            flagNoUserDefinedData = 0
        elif(len(criteriaData) == 2):
            flagNoUserDefinedData = 1
        else:
            flagNoUserDefinedData = 1
            pass
        if(flagNoUserDefinedData == 0):
            userDefinedHeader = pd.read_csv(self.f_in, header=None, \
                                            skiprows=numSolverDefinedHeader + numSolverDefinedValue, \
                                            nrows=numUserDefinedValue, \
                                            names=col_names, \
                                            skipinitialspace=True, \
                                            delim_whitespace=True)
            if(flagSplit == 0):
                userDefinedHeader = userDefinedHeader.drop(['#', ';', 'X', 'Y', 'Z'], axis=1)
                userDefinedHeader = userDefinedHeader.reset_index(drop=True)
            else:
                userDefinedHeader = userDefinedHeader.drop(['#', ';'], axis=1)
                userDefinedHeader = userDefinedHeader.reset_index(drop=True)
                userDefinedHeader["Xvalue"] = userDefinedHeader["XV"].str.split("=", expand=True)[1].astype(float)
                userDefinedHeader["Yvalue"] = userDefinedHeader["YV"].str.split("=", expand=True)[1].astype(float)
                userDefinedHeader["Zvalue"] = userDefinedHeader["ZV"].str.split("=", expand=True)[1].astype(float)
                userDefinedHeader = userDefinedHeader.drop(['XV', 'YV', 'ZV'], axis=1)
                userDefinedHeader = userDefinedHeader.reset_index(drop=True)
            #
            # READ DATA
            #
            print(self.numSolverDefinedValue, numUserDefinedValue)

        # 時系列データ
        timeSeries = pd.read_csv(self.f_in, header=None, skiprows=numOfDataHeader, skipinitialspace=True, delim_whitespace=True)
        # timeSeries = timeSeries.drop(np.arange(numSolverDefinedValue), axis=1)
        timeSeries = timeSeries.T
        timeSeries = timeSeries.reset_index(drop=True)

        #
        # self
        #
        self.preDefinedHeader = preDefineHeader
        if(flagNoUserDefinedData == 0):
            self.userDefinedHeader = userDefinedHeader
        self.numUserDefinedValue = numUserDefinedValue
        self.timeSeries = timeSeries
        self.NTIME = len(timeSeries.columns)
        nti = int(self.keyword.get("TIME", '01'))
        time=self.timeSeries.loc[nti, :] * (l00 / u00) 
        nfx = int(self.keyword.get("FORC_X", '01'))
        nfy = int(self.keyword.get("FORC_Y", '01'))
        nfz = int(self.keyword.get("FORC_Z", '01'))
        fx=self.timeSeries.loc[nfx, :] * (u00 * u00) 
        fy=self.timeSeries.loc[nfy, :] * (u00 * u00) 
        fz=self.timeSeries.loc[nfz, :] * (u00 * u00) 
        self.timeSeries.loc[nti, :] = time
        self.timeSeries.loc[nfx, :] = fx
        self.timeSeries.loc[nfy, :] = fy
        self.timeSeries.loc[nfz, :] = fz
        self.time=timeSeries.loc[0, :]

        if(flagNoUserDefinedData == 0):
            # 有次元化
            for i in range(np.size(userDefinedHeader.dir)):
              n = i+1
              number = n + self.numSolverDefinedValue - 1
              if(userDefinedHeader["dir"][i] == "PRESSURE"):
                  tmp=self.timeSeries.loc[number, :] * (u00 * u00) 
                  self.timeSeries.loc[number, :] = tmp
              elif(userDefinedHeader["dir"][i] == "VELOCITY-U"):
                  tmp=self.timeSeries.loc[number, :] * (u00) 
                  self.timeSeries.loc[number, :] = tmp
              elif(userDefinedHeader["dir"][i] == "VELOCITY-V"):
                  tmp=self.timeSeries.loc[number, :] * (u00) 
                  self.timeSeries.loc[number, :] = tmp
              elif(userDefinedHeader["dir"][i] == "VELOCITY-W"):
                  tmp=self.timeSeries.loc[number, :] * (u00) 
                  self.timeSeries.loc[number, :] = tmp


    def plot(self, num, flaglog, **kwargs):
        '''
        plot(num, flaglog):
        This function can plot initially defined value and
        user-specified point value.
        You need to specify "word" in the list below or
        number of point which you want to plot (1 ~).
        In addition, you should set flaglog.
        flaglog = 0 : figure is default.
        flaglog = 1 : figure is log scale.

        NAME     | num | NAME in FFB
        -------------------------------
        TIME        00   TIME
        MAXDIV      01   MAXIMUM DIVERGENT
        AELMNU      02   AVERAGE ELEMENT EDDY VISCOSITY
        PRSITR      03   ITERATIONS DONE FOR PRESSURE EQUATION
        PRSL2N      04   L2-NORM RESIDUAL OF PRESSURE EQUATION
        FORC_X      05   FLUID FORCE ACTING IN X DIRECTION
        FORC_Y      06   FLUID FORCE ACTING IN Y DIRECTION
        FORC_Z      07   FLUID FORCE ACTING IN Z DIRECTION
        UEQITR      08   ITERATIONS DONE FOR U-EQUATION
        VEQITR      09   ITERATIONS DONE FOR V-EQUATION
        WEQITR      10   ITERATIONS DONE FOR W-EQUATION
        TEQITR      11   ITERATIONS DONE FOR T-EQUATION
        KEQITR      12   ITERATIONS DONE FOR K-EQUATION
        EEQITR      13   ITERATIONS DONE FOR E-EQUATION
        UEQL2N      14   L2-NORM RESIDUAL OF U-EQUATION
        VEQL2N      15   L2-NORM RESIDUAL OF V-EQUATION
        WEQL2N      16   L2-NORM RESIDUAL OF W-EQUATION
        TEQL2N      17   L2-NORM RESIDUAL OF T-EQUATION
        KEQL2N      18   L2-NORM RESIDUAL OF K-EQUATION
        EEQL2N      19   L2-NORM RESIDUAL OF E-EQUATION
        TEMPVI      20   VOLUME INTEGRATION OF TEMPRATURE
        OVSERR      21   MAX. OVERSET ERROR
        TOTALV      22   TOTAL VOLUME OF FIRST FLUID
        VF_MIN      23   MINIMUM VOLUME FRACTION
        VF_MAX      24   MAXMUM VOLUME FRACTION
        VOFCFL      25   MAXMUM COURANT NUMBER FOR VOF EQ.
        INLTFL      26   FLUX ON INLET BOUNDARY
        OTLTFL      27   FLUX ON OUTLET BOUNDARY

        '''
        if type(num) is str:
            number = int(self.keyword.get(num, '01'))
            title = self.preDefinedHeader[1][number]
            nlabel = self.keymean.get(num, 'EMPTY')
        elif type(num) is int:
            number = num + self.numSolverDefinedValue - 1
            title = self.userDefinedHeader['dir'][num - 1]
            nlabel = title
            xval = str(self.userDefinedHeader['Xvalue'][num - 1])
            yval = str(self.userDefinedHeader['Yvalue'][num - 1])
            zval = str(self.userDefinedHeader['Zvalue'][num - 1])
            title = "X=" + xval + "Y=" + yval + "Z=" + zval
        else:
            print('type of num need number or char.')

        try:
            plt.plot(self.timeSeries.loc[0, :], self.timeSeries.loc[number, :], '-k')
            if(flaglog):
                plt.xscale('log')
                plt.yscale('log')
            plt.title(title)
            if(len(kwargs) == 2):
              print("yes")
              xlabel = kwargs.get("xaxis", '1')
              ylabel = kwargs.get("yaxis", '1')
              plt.xlabel(xlabel)
              plt.ylabel(ylabel)
            else:
              plt.xlabel("Time [-]")
              plt.ylabel(nlabel)

            if type(num) is str:

                plt.savefig("fig" + num + ".png", bbox_inches="tight", pad_inches=0.05)
            elif type(num) is int:
                plt.savefig("figPoint" + str(num) + ".png", bbox_inches="tight", pad_inches=0.05)
            plt.clf()
        except ValueError as error:
            print(error)


    def getvalue(self, num):
        if type(num) is str:
            number = int(self.keyword.get(num, '01'))
            title = self.preDefinedHeader[1][number]
        elif type(num) is int:
            number = num + self.numSolverDefinedValue - 1
            title = self.userDefinedHeader['dir'][num - 1]
        else:
            print('type of num need number or char.')

        return np.array(self.timeSeries.loc[number, :])

    def getvalues(self, num1, num2):
        if type(num1) is int:
            number1 = num1 + self.numSolverDefinedValue - 1
            number2 = num2 + self.numSolverDefinedValue - 1
            title = self.userDefinedHeader['dir'][num1 - 1]
            xval = self.userDefinedHeader['Xvalue'][num1 - 1 : num2]
            yval = self.userDefinedHeader['Yvalue'][num1 - 1 : num2]
            zval = self.userDefinedHeader['Zvalue'][num1 - 1 : num2]
        else:
            print('type of num need number or char.')

        return xval, yval, zval, np.array(self.output.loc[number1:number2, :])
