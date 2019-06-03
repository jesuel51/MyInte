k=root['SETTINGS']['PLOTS']['iview']
alpha_E=0.43
# font set
font={'family' : 'serif',
      'color'  : 'darkred',
      'weight' : 'normal',
      'size'   :32,}
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
grad=root['OUTPUTS']['TGYROOutput']['out.tgyro.gradient']['data'];
grad=array(map(list,zip(*grad)))
radius=grad[0][-p_tgyro-1:]
radius=[string.atof(item) for item in radius]
#print(radius)
root['SETTINGS']['TEMP']['radius']=radius
Gamma_E=grad[7][-p_tgyro-1:]
Gamma_E=[string.atof(item) for item in Gamma_E]
Gamma_P=grad[6][-p_tgyro-1:]
Gamma_P=[string.atof(item) for item in Gamma_P]
tgyro_max=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
rho=linspace(0,tgyro_max,p_tgyro+1)
if root['SETTINGS']['TEMP'].has_key('indexlin'):
    indexlin=root['SETTINGS']['TEMP']['indexlin']
    Gamma_max=root['SETTINGS']['TEMP']['Gamma_max']
if root['SETTINGS']['TEMP'].has_key('indexlin'):
    indexlin=[int(item) for item in indexlin]
    rholin=rho[indexlin]
    #plot(rholin,Gamma_max,'-bo',linewidth=3,markersize=16,label='$\gamma_{max}$')
    #semilogy(rholin,[alpha_E*item for item in Gamma_max],'-bo',linewidth=3,markersize=16,label='$\alpha_E$ $\gamma_{max}$')
    figure
    subplot(2,1,1)
    #plot(rho,Gamma_E,'-r*',linewidth=3,markersize=16,label='$\gamma_E$')
    semilogy(rho,[alpha_E*item for item in Gamma_E],'-r*',linewidth=3,markersize=16,label='$a_E$'+'$\gamma_E$')
    ax=gca()
    ax.set_ylim(1.e-3,5.e-1)
    semilogy(rholin, Gamma_max,'-bo',linewidth=3,markersize=16,label='$\gamma_{max}$')
    print(Gamma_max)
print(Gamma_E)
legend(loc=0,fontsize=24).draggable(True)
ax=plt.gca()
ax.set_xlabel('$rho$',fontdict=font)
xticks(fontsize=24,family='serif')
yticks(fontsize=24,family='serif')
#ylabel('a/cs*$\gamma_E$')
subplot(2,1,2)
q=root['INPUTSRec']['TGYRO'][int(k)]['input.profiles']['q']
rho=linspace(0,1,len(q))
plot(rho,abs(q),'-r*',linewidth=2,label='q')
xlabel('rho',fontsize=16)
ax.set_xlabel('$rho$',fontdict=font)
xticks(fontsize=24,family='serif')
yticks(fontsize=24,family='serif')
legend(loc=0,fontsize=24).draggable(True)
