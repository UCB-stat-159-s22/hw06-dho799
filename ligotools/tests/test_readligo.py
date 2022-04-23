from ligotools import readligo as rl
import os

def test_read_frame():
    test1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnamelist = rl.read_frame(test1, 'H1')
    assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (qmask is not None) & (shortnameList is not None) & (injmask is not None)
    
def test_read_hdf5():
    test2 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(test2, 'H1')
    assert (strain is not None) & (gpsStart is not None) & (ts is not None) & (qmask is not None) & (shortnameList is not None) & (injmask is not None)
    
def test_loaddata_H1(): 
    test3 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, channel_dict = rl.loaddata(test3, 'H1')
    assert (strain is not None) & (time is not None) & (channel_dict is not None) 
    
def test_loaddata_L1():
    test4 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, channel_dict = rl.loaddata(test4, 'L1')
    assert (strain is not None) & (time is not None) & (channel_dict is not None) 