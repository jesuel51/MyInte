import numpy as np
k=root['SETTINGS']['PLOTS']['iview']
ncmp=root['SETTINGS']['PLOTS']['ncmp']
#nj=root['SETTINGS']['PHYSICS']['nj']
nj=root['INPUTS']['TGYROInput']['input.profiles']['N_EXP']
fs1=16
fs2=24
fs3=24
q=np.zeros([ncmp,nj])
Te=np.zeros([ncmp,nj])
Ti=np.zeros([ncmp,nj])
ne=np.zeros([ncmp,nj])
nhe=np.zeros([ncmp,nj])
w=np.zeros([ncmp,nj])
cur=np.zeros([ncmp,nj])
for kk in linspace(k,k+ncmp-1,ncmp):
    inputpro=root['INPUTSRec']['TGYRO'][kk]['input.profiles']
#    rho=root['OUTPUTSRec']['ProfileGenOutput'][kk]['rho']
#    q[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['q']
#    Te[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['Te']
#    Ti[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['Ti_1']
#    ne[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['ne']
#    w[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['omega0']
    rho=inputpro['rho']
    q[kk-k]=inputpro['q']
    Te[kk-k]=inputpro['Te']
    Ti[kk-k]=inputpro['Ti_1']
    ne[kk-k]=inputpro['ne']
    nhe[kk-k]=inputpro['ni_2']
    w[kk-k]=inputpro['omega0']
    cur[kk-k]=root['OUTPUTSRec']['ONETWOOutput'][int(kk)]['trpltout.nc']['curden']['data'][-1]/100.
#plt.close()
w=w/1.e3
linsyb=array(['-ro','-b*','-r*','-bo','-k*','-ko'])
nsyb=array([str(k),str(k+1),str(k+2),str(k+3),str(k+4),str(k+5)])
if q[1][1]<0:
    qsign=-1
else:
    qsign=1
plt.figure(figsize=[10,15])
wid=0.35
heigt=0.25
left1=0.1
left2=0.6
Rct1=[left1,0.7,wid,heigt]  #left, bottom, width,height
Rct2=[left2,0.7,wid,heigt]  #left, bottom, width,height
Rct3=[left1,0.4,wid,heigt]  #left, bottom, width,height
Rct4=[left2,0.4,wid,heigt]  #left, bottom, width,height
Rct5=[left1,0.1,wid,heigt]  #left, bottom, width,height
Rct6=[left2,0.1,wid,heigt]  #left, bottom, width,height
xtext=0.2
#subplot(3,2,1)
ax1=plt.axes(Rct1)
for kk in linspace(0,ncmp-1,ncmp):
    ax1.plot(rho,q[kk]*qsign,linsyb[kk],linewidth=2,label=nsyb[kk])
    #ylabel('q('+str(qsign)[0]+')',fontsize=fs2,family='serif')
    ylabel('$q$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks([2,4,6,8],fontsize=fs1,family='serif')
    legend(loc=0,fontsize=fs1).draggable(True)
    ylim([1,8])
    text(xtext,7.4,'(a)',fontsize=fs3)
#subplot(3,2,2)
ax2=plt.axes(Rct2)
for kk in linspace(0,ncmp-1,ncmp):
    ax2.plot(rho,cur[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    ylabel('$<J>(MA m^{-2})$',fontsize=fs2-4,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylim(0,1.8)
    text(xtext,1.35,'(b)',fontsize=fs3)
    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,5)
ax5=plt.axes(Rct5)
for kk in linspace(0,ncmp-1,ncmp):
    ax5.plot(rho,ne[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
#    ax5.plot(rho,10*nhe[kk],linsyb[2*kk],linewidth=2,label='10*Helium')
    xlabel('$rho$',fontsize=fs2,family='serif')
    ylabel('$n_e(10^{19}m^{-3})$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylim([0,15])
    text(xtext,9,'(e)',fontsize=fs3)
    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,4)
ax4=plt.axes(Rct4)
for kk in linspace(0,ncmp-1,ncmp):
    ax4.plot(rho,Ti[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$T_i(keV)$',fontsize=fs2,family='serif')
    ylim([0,40])
    text(xtext,27,'(d)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,3)
ax3=plt.axes(Rct3)
for kk in linspace(0,ncmp-1,ncmp):
    ax3.plot(rho,Te[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$T_e(keV)$',fontsize=fs2,family='serif')
    ylim([0,40])
    text(xtext,27,'(c)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,6)
ax6=plt.axes(Rct6)
for kk in linspace(0,ncmp-1,ncmp):
#    ax6.plot(rho,w[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    ax6.plot(rho,nhe[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
#    ylabel('$\omega(krad s^-1)$',fontsize=fs2,family='serif')
    ylabel('$n_{he}(10^{19}m^{-3})$',fontsize=fs2,family='serif')
    xlabel('$rho$',fontsize=fs2,family='serif')
#    ylim([-45,0])
    text(xtext,-6,'(f)',fontsize=fs3)
    legend(loc='lower right',fontsize=fs1).draggable(True)
