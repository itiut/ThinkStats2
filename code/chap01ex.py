"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys
from collections import defaultdict

import nsfg
import thinkstats2

def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

def MakePregMap(preg_df):
    d = defaultdict(list)
    for i, caseid in preg_df.caseid.items():
        d[caseid].append(i)
    return d

def ValidatePregnum(resp_df, preg_df):
    caseid2pregindices = MakePregMap(preg_df)

    for i, pregnum in resp_df.pregnum.items():
        caseid = resp_df.caseid[i]
        indices = caseid2pregindices[caseid]
        if pregnum != len(indices):
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp_df = ReadFemResp()
    preg_df = ReadFemPreg()

    # http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
    assert len(resp_df) == 7643
    assert resp_df.pregnum.value_counts()[1] == 1267
    assert resp_df.pregnum.value_counts()[2] == 1432
    assert ValidatePregnum(resp_df, preg_df)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
