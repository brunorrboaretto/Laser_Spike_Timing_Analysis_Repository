import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import colorednoise as cn

print('Loading the ANN')
model = load_model('model.keras')
wl = 4
def perm_indices(ts, wl, lag):
	m = len(ts)-(wl-1)*lag
	indcs = np.zeros(m, dtype=int)
	for i in range(1, wl):
		st = ts[(i-1)*lag: m + ((i-1)*lag)]
		for j in range(i, wl):
			indcs += st > ts[j*lag: m+j*lag]
		indcs *= wl-i
	return indcs + 1

def predict_alpha (Serie):
    a1 = perm_indices(Serie, wl, 1)
    num_states = np.math.factorial(wl)
    hist = np.histogram(a1,num_states)
    P = 1.0*hist[0]/len(a1)
    P_data = np.array([P])

    S = 0.0
    for i in range(num_states):
      if P[i]!= 0.0:
        S-=(P[i]*np.log(P[i]))
        
    return [model.predict(P_data,verbose=0),S]

gain = 100
cur_list = [25.5,26.0,26.5,27.0,27.5]

S_list = np.zeros((5,70))
A_list = np.zeros((5,70))


for I in range(len(cur_list)):
  cur = cur_list[I]
  for F in range(1,71):

    data = np.loadtxt('Sinusoidal_full_TS/gain_%.3d_cur-%.1f_f-%.2d.dat' % (gain,cur,F)) 
    
    Serie = data
    Size = len(Serie)
    num_states = np.math.factorial(wl)
    alpha, S,= predict_alpha(Serie)
    S/=np.log(num_states)
    S_list[I][F-1] = S
    A_list[I][F-1] = alpha
    
    print('I=%f nu=%.2d alpha=%f' % (cur,F,float(alpha)))
#print(A_list)    

print('Generating Figure 4')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
sz1 = 21
sz2 = 18

fig = plt.figure()
gs = fig.add_gridspec(2,1)
ax_0 = fig.add_subplot(gs[0,0])
ax_1 = fig.add_subplot(gs[1,0])

X = np.linspace(1,70,70)
Y = np.linspace(25.5,27.5,5)
X, Y = np.meshgrid(X, Y)

colors = plt.cm.jet(np.linspace(.0, 1, 256))
mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)
surf = ax_0.pcolormesh(X,Y,A_list,cmap=mymap,vmin=-4)#,vmax=4)
cb = fig.colorbar(surf,pad=.06,ax=ax_0)
cb.set_label(label=r'$\alpha$',fontsize=sz1)
cb.ax.tick_params(labelsize=sz2)

mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)
surf = ax_1.pcolormesh(X,Y,S_list,cmap=mymap,vmin=0.85,vmax=1)
cb = fig.colorbar(surf,pad=.06,ax=ax_1)
cb.set_label(label=r'$H$',fontsize=sz1)
cb.ax.tick_params(labelsize=sz2)

ax_0.set_ylabel(r'$I$ (mA)',fontsize=sz1)
ax_1.set_xlabel(r'$\nu$ (MHz)',fontsize=sz1)
ax_1.set_ylabel(r'$I$ (mA)',fontsize=sz1)

ax_0.tick_params(axis='both', labelsize=sz2)
ax_1.tick_params(axis='both', labelsize=sz2)

ax_0.text(87,27.6,'(a)',fontsize=sz2)
ax_1.text(87,27.6,'(b)',fontsize=sz2)

plt.subplots_adjust(left=None, bottom=.2, right=None, top=None, wspace=.25, hspace=.25)
width = 28; height = 24;
fig.set_size_inches(width/2.54,height/2.54) #2.54 cm = 1 inches
#plt.subplots_adjust(left=None, bottom=.2, right=None, top=None, wspace=None, hspace=None)
plt.savefig('fig_4.png', dpi=256, bbox_inches='tight')


