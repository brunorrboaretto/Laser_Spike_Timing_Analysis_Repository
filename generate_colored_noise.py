import numpy as np
import colorednoise as cn

def perm_indices(ts, wl, lag):
	m = len(ts)-(wl-1)*lag
	indcs = np.zeros(m, dtype=int)
	for i in range(1, wl):
		st = ts[(i-1)*lag: m + ((i-1)*lag)]
		for j in range(i, wl):
			indcs += st > ts[j*lag: m+j*lag]
		indcs *= wl-i
	return indcs + 1

seed_in  = 0
seed_out = 50000
wl = 4

Size = 2**20

f1 = open('cn_a_data.dat', 'w')
f2 = open('cn_p_data.dat', 'w')

Sm = []
for seed in range(seed_in, seed_out):
    np.random.seed(seed)
    beta = np.random.rand()*8-4.0
    f1.write('%f\n' % beta)

    Serie = cn.powerlaw_psd_gaussian(beta, Size)
    a1 = perm_indices(Serie, wl, 1)
    num_states = np.math.factorial(wl)
    P = np.zeros(num_states) 
    for i in range(len(a1)): 
        P[a1[i]-1]+=1 

    P/=sum(P) 

    S = 0.0
    for i in range(num_states):
        f2.write('%f ' % P[i])
        if P[i]!= 0.0:
            S-=(P[i]*np.log(P[i]))
    f2.write('\n')
    print(seed,beta)
