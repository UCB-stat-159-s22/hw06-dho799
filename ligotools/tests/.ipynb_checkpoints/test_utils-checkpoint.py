from ligotools import readligo as rl
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
from ligotools.utils import *
from os.path import exists
from scipy.signal import butter, filtfilt
from os import remove

#whiten setup
fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
fs = 4096
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = 4*fs)
psd_H1 = interp1d(freqs, Pxx_H1)
dt_H1 = time_H1[1] - time_H1[0]

def test_whiten():
    test1 = whiten(strain_H1, psd_H1, dt_H1)
    assert len(test1) == 131072
    
def test_write_wavfile(): 
    test2 = whiten(strain_H1, psd_H1, dt_H1)
    write_wavfile("audio/test.wav", fs, test2)
    assert exists("audio/test.wav")
    remove("audio/test.wav")
    
def test_reqshift(): 
    test3 = whiten(strain_H1, psd_H1, dt_H1)
    test3_shift = reqshift(test3, 400.0, fs)
    assert len(test3_shift) == 131072

def test_plot_func(): 
    test4 = whiten(strain_H1, psd_H1, dt_H1)
    fband = [43.0, 300.0]
    bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
    normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
    strain_H1_whitenbp = filtfilt(bb, ab, test4) / normalization
    #plot_func(time_H1,1126259462.432373,0,'g','GW150914','H1','png',1126259462.44,strain_H1_whitenbp,0,0,0,999.743130306333,0,psd_H1, fs)
    assert exists('figures/'+'GW150914'+"_"+"H1"+"_matchfreq."+"png")
