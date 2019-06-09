# -*- coding: utf-8 -*-
##################################################
# Copyright (c) [2019] [Yuya Miki]
# 
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
##################################################
# This is code for reading FFBs HISTORY & SAMPLX file.
#
import ffbutil as fb
import argparse

#
# Parser setting
#
program_name = 'plot_history'
parser = argparse.ArgumentParser(prog=program_name)
parser.add_argument('inputfile',
                    help='inputfile')
parser.add_argument('--version',
                    version='%(prog)s 1.0.0',
                    action='version',
                    default=False)

#
# Main
#
args = parser.parse_args()
file_input = args.inputfile
f1 = fb.history()
f1.read(file_input)
#
# You can specify points to plot.
#
# f1.plot(1, True)
#
# You can specify any contents in FFB's HISTORY data to plot.
#
# NAME     | num | NAME in FFB
# -------------------------------
# TIME        00   TIME
# MAXDIV      01   MAXIMUM DIVERGENT
# AELMNU      02   AVERAGE ELEMENT EDDY VISCOSITY
# PRSITR      03   ITERATIONS DONE FOR PRESSURE EQUATION
# PRSL2N      04   L2-NORM RESIDUAL OF PRESSURE EQUATION
# FORC_X      05   FLUID FORCE ACTING IN X DIRECTION
# FORC_Y      06   FLUID FORCE ACTING IN Y DIRECTION
# FORC_Z      07   FLUID FORCE ACTING IN Z DIRECTION
# UEQITR      08   ITERATIONS DONE FOR U-EQUATION
# VEQITR      09   ITERATIONS DONE FOR V-EQUATION
# WEQITR      10   ITERATIONS DONE FOR W-EQUATION
# TEQITR      11   ITERATIONS DONE FOR T-EQUATION
# KEQITR      12   ITERATIONS DONE FOR K-EQUATION
# EEQITR      13   ITERATIONS DONE FOR E-EQUATION
# UEQL2N      14   L2-NORM RESIDUAL OF U-EQUATION
# VEQL2N      15   L2-NORM RESIDUAL OF V-EQUATION
# WEQL2N      16   L2-NORM RESIDUAL OF W-EQUATION
# TEQL2N      17   L2-NORM RESIDUAL OF T-EQUATION
# KEQL2N      18   L2-NORM RESIDUAL OF K-EQUATION
# EEQL2N      19   L2-NORM RESIDUAL OF E-EQUATION
# TEMPVI      20   VOLUME INTEGRATION OF TEMPRATURE
# OVSERR      21   MAX. OVERSET ERROR
# TOTALV      22   TOTAL VOLUME OF FIRST FLUID
# VF_MIN      23   MINIMUM VOLUME FRACTION
# VF_MAX      24   MAXMUM VOLUME FRACTION
# VOFCFL      25   MAXMUM COURANT NUMBER FOR VOF EQ.
# INLTFL      26   FLUX ON INLET BOUNDARY
# OTLTFL      27   FLUX ON OUTLET BOUNDARY
#
f1.plot("FORC_Z", False)
f1.plot("MAXDIV", False)
f1.plot("OVSERR", False)
