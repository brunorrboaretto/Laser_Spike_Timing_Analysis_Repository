import numpy as np 
import scipy.io

Gain=100

for C in range(5):
    cur = 25.5 + 0.5*C;
    for f in range(1,71):
        fp_in = 'Sinusoidal_full_TS/Gain_%d/idis_cur-%.1f_f-%d000000_Gain-%d_th-1.5.mat' % (Gain,cur,f,Gain)
        print('Reading file: Sinusoidal_full_TS/Gain_%d/idis_cur-%.1f_f-%d000000_Gain-%d_th-1.5.mat' % (Gain,cur,f,Gain))
        mat = scipy.io.loadmat(fp_in)
        data = mat['idi_out']
        data = data[0]
        fp_out = 'Sinusoidal_full_TS/gain_%.3d_cur-%.1f_f-%.2d.dat' % (Gain,cur,f)
        fp = open(fp_out,'w')
        for i in range(len(data)):
            fp.write('%lf\n' % data[i])
        print('Extracting file:Sinusoidal_full_TS/gain_%.3d_cur-%.1f_f-%.2d.dat' % (Gain,cur,f))
print('Done')

