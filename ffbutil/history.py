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
# from scipy import signal
import scipy.signal
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



    def read(self, file_in):
        '''
        '''
        print("read HISTORY data. file=", file_in)
        self.f_in = file_in
        #
        # Magic number
        #
        skip1 = 5
        row1 = 28
        skip2 = skip1 + row1
        self.skip = row1
        #
        # READ FIRST COMMENTOUT ROWS NUMBER
        #
        f = open(self.f_in)
        skip_row = 0
        data_row = 0
        line = f.readline()
        skip_row = skip_row + 1
        print(skip_row, line.rstrip())
        while line:
            line = f.readline()
            if not line:
                break
            if(line[0] == "#"):
                skip_row = skip_row + 1
                print(skip_row, line.rstrip())
            else:
                data_row = data_row + 1
        f.close
        print(skip_row,  data_row)
        #
        # READ OTHERE VALUE
        #
        f1 = pd.read_csv(self.f_in, header=None, skiprows=skip1, nrows=row1, sep='#', skipinitialspace=True)
        #
        # READ POTISION
        #
        # row2 is data lenght
        row2 = skip_row - (skip1 + row1)
        col_names = ['#', 'dir', ';', 'X', 'Xvalue', 'Y', 'Yvalue', 'Z', 'Zvalue']
        f2 = pd.read_csv(self.f_in, header=None, skiprows=skip2, nrows=row2, names=col_names, skipinitialspace=True, delim_whitespace=True)
        f2 = f2.drop(['#', ';', 'X', 'Y', 'Z'], axis=1)
        f2 = f2.reset_index(drop=True)

        #
        # READ DATA
        #
        print(self.skip, row2)

        f3 = pd.read_csv(self.f_in, header=None, skiprows=skip_row, skipinitialspace=True, delim_whitespace=True)
        # f3 = f3.drop(np.arange(row1), axis=1)
        f3 = f3.T
        f3 = f3.reset_index(drop=True)

        #
        # self
        #
        self.f_other = f1
        self.f_data = f2
        self.output = f3
        self.NTIME = len(f3.columns)

    def plot(self, num, flaglog):
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
            title = self.f_other[1][number]
        elif type(num) is int:
            number = num + self.skip - 1
            title = self.f_data['dir'][num - 1]
        else:
            print('type of num need number or char.')

        try:
            plt.plot(self.output.loc[0, :], self.output.loc[number, :], '-ok')
            if(flaglog):
                plt.xscale('log')
                plt.yscale('log')
            plt.title(title)
            plt.show()
        except ValueError as error:
            print(error)

    # def plot(self, num, flaglog):
    #     '''
    #     plot(num, flaglog):
    #     This function can plot user-specified point value

    #     self.output.loc[0, :] is time
    #     num is number of point which you want to plot (1 ~).

    #     '''
    #     print(num + self.skip - 1)
    #     try:
    #         plt.plot(self.output.loc[0, :], self.output.loc[num + self.skip - 1, :], '-ok')
    #         if(flaglog):
    #             plt.xscale('log')
    #             plt.yscale('log')
    #         print(self.f_data['dir'][num - 1])
    #         title = self.f_data['dir'][num - 1]
    #         plt.title(title)
    #         plt.show()
    #     except ValueError as error:
    #         print(error)

    def do_FFT(self, num1, U):
        print("NTIME is ", self.NTIME)
        t = self.output.loc[0, :]
        # Y1
        y1 = self.output.loc[num1 + self.skip - 1, :]
        average = np.mean(y1)
        yf1 = y1 - average
        yfcorr1 = np.correlate(y1, y1, 'same')
        n = self.NTIME
        dt = t[1] - t[0]
        freq = np.linspace(0, 1.0 / dt, n)
        wave_n = 2.0 * np.pi * freq / U
        F1 = np.fft.fft(yfcorr1)
        return wave_n, F1

    def calc_FFT(self, num1, num2, num3, U):
        w1, f1 = self.do_FFT(num1, U)
        w2, f2 = self.do_FFT(num2, U)
        w3, f3 = self.do_FFT(num3, U)
        e = f1 + f2 + f3
        k = np.sqrt(w1**2 + w2**2 + w3**2)
        # FIGURE
        plt.figure()
        plt.plot(k, e, '-ok', label='|F(k)|')
        # plt.xlim([0, max(k) / 2])
        plt.legend(loc="upper right")
        plt.xlabel("Wave number")
        plt.ylabel("Amp")
        plt.xscale('symlog')
        plt.yscale('symlog')
        plt.show()

    def calc_autoCOR(self, num1):
        t = self.output.loc[0, :]
        n = self.NTIME
        dt = t[1] - t[0]
        freq = np.linspace(0, 1.0 / dt, n)
        wave_n = 2.0 * np.pi * freq / 1.0
        # Y1
        y1 = np.array(self.output.loc[num1 + self.skip - 1, :])
        average = np.mean(y1, axis=0)
        print("average", average)
        yf1 = y1 - average
        yfcorr1 = np.correlate(y1, y1, 'same')
        yfcorr1 = yfcorr1 / yfcorr1[0]
        print(yfcorr1)
        # FIGURE
        plt.figure()
        plt.plot(wave_n, yfcorr1, 'ok', label='|F(k)|')
        plt.legend(loc="upper right")
        plt.xlabel("wave number")
        plt.ylabel("R_ii")
        plt.xscale('symlog')
        plt.show()

    def calc_PSD(self, num):
        '''
        calc_PSD(num):
        This function can calculate Power Spectrum Density (PSD).
        You can specify the data-source of the function by "num" variable.
        If "num" is string, this function search the string from the keyword.
        If "num" is integer, this function use data from the user-specified data.
        '''
        if type(num) is str:
            number = int(self.keyword.get(num, '01'))
        elif type(num) is int:
            number = num + self.skip - 1
        else:
            print('type of num need number or char.')
        try:
            nperseg_default = 256
            print("NTIME is ", self.NTIME)
            print("Default overlap is ", self.NTIME / nperseg_default)
            t = self.output.loc[0, :]
            y = self.output.loc[number, :]
            n = self.NTIME
            dt = t[1] - t[0]
            fs = 1 / dt
            #
            freq1, P1 = scipy.signal.periodogram(y, fs)
            freq2, P2 = scipy.signal.welch(y, fs, nperseg=nperseg_default, window="hann")
            freq3, P3 = scipy.signal.welch(y, fs, nperseg=n / 2,           window="hann")
            freq4, P4 = scipy.signal.welch(y, fs, nperseg=n / 8,           window="hann")
            #
            plt.figure()
            plt.plot(freq1, 10 * np.log10(P1), "-b",              label="periodogram")
            plt.plot(freq2, 10 * np.log10(P2), "-r", linewidth=2, label="nseg=256")
            plt.plot(freq3, 10 * np.log10(P3), "-c", linewidth=2, label="nseg=512")
            plt.plot(freq4, 10 * np.log10(P4), "-y", linewidth=2, label="nseg=128")
            plt.legend(loc="upper right")
            plt.xlabel("Frequency[Hz]")
            plt.ylabel("Power/frequency[dB/Hz]")
            # plt.xlim([20, max(freq2) / 2])
            plt.xscale('log')
            plt.show()
            df = 1 / dt / n
            rms = np.sqrt(np.sum(P2) * df)
            print("RMS is ", rms)
        except ValueError as error:
            print(error)
