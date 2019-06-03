# this script is used to plot the density profiles of the all the species, including n_dt, n_he, n_ar, n_w, ne
import numpy as np
k=root['SETTINGS']['PLOTS']['iview']
ncmp=root['SETTINGS']['PLOTS']['ncmp']
#nj=root['SETTINGS']['PHYSICS']['nj']
nj=root['INPUTS']['TGYROInput']['input.profiles']['N_EXP']
rho=linspace(0,1,nj)
fs1=16
fs2=24
fs3=24
ne=np.zeros([ncmp,nj])
ndt=np.zeros([ncmp,nj])
nhe=np.zeros([ncmp,nj])
nar=np.zeros([ncmp,nj])
nw=np.zeros([ncmp,nj])
Zeff=np.zeros([ncmp,nj])
#cur=np.zeros([ncmp,nj])
for kk in linspace(k,k+ncmp-1,ncmp):
    inonedt=root['INPUTSRec']['ONETWO'][kk]['inone_dt']['NAMELIS1']
    ne[kk-k]=inonedt['ENEIN']
    ndt[kk-k]=inonedt['ENP'].T[0]
    nhe[kk-k]=inonedt['ENP'].T[1]
    nar[kk-k]=inonedt['ENI'].T[1]
    nw[kk-k]=inonedt['ENI'].T[0]
    Zeff[kk-k]=root['INPUTSRec']['TGYRO'][4]['input.profiles']['z_eff']
#    cur[kk-k]=root['OUTPUTSRec']['ONETWOOutput'][int(kk)]['trpltout.nc']['curden']['data'][-1]/100.
#plt.close()
linsyb=array(['-ro','-b*','-r*','-bo','-k*','-ko'])
nsyb=array([str(k),str(k+1),str(k+2),str(k+3),str(k+4),str(k+5)])
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
#xtext=0.2
#subplot(3,2,1)
ax1=plt.axes(Rct1)
for kk in linspace(0,ncmp-1,ncmp):
    ax1.plot(rho,ne[kk]/1.e13,linsyb[kk],linewidth=2,label=nsyb[kk])
    #ylabel('q('+str(qsign)[0]+')',fontsize=fs2,family='serif')
    ylabel('$n_e$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
#    yticks([2,4,6,8],fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    legend(loc=0,fontsize=fs1).draggable(True)
#    ylim([2,8])
#    text(xtext,7.4,'(a)',fontsize=fs3)
#subplot(3,2,2)
ax2=plt.axes(Rct2)
for kk in linspace(0,ncmp-1,ncmp):
    ax2.plot(rho,ndt[kk]/1.e13,linsyb[kk],linewidth=2,label=nsyb[kk])
    ylabel('$n_{dt}$',fontsize=fs2-4,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
#    ylim(0,1.5)
#    text(xtext,1.35,'(b)',fontsize=fs3)
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,5)
ax5=plt.axes(Rct5)
for kk in linspace(0,ncmp-1,ncmp):
    ax5.plot(rho,nw[kk]/1.e13,linsyb[kk],linewidth=2,label=nsyb[kk])
    xlabel('$rho$',fontsize=fs2,family='serif')
    ylabel('$n_{w}$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
#    ylim([0,10])
#    text(xtext,9,'(e)',fontsize=fs3)
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,4)
ax4=plt.axes(Rct4)
for kk in linspace(0,ncmp-1,ncmp):
    ax4.plot(rho,nar[kk]/1.e13,linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$n_{ar}$',fontsize=fs2,family='serif')
#    ylim([0,30])
#    text(xtext,27,'(d)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,3)
ax3=plt.axes(Rct3)
for kk in linspace(0,ncmp-1,ncmp):
    ax3.plot(rho,nhe[kk]/1.e13,linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$n_{he}$',fontsize=fs2,family='serif')
#    ylim([0,30])
#    text(xtext,27,'(c)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,6)
ax6=plt.axes(Rct6)
for kk in linspace(0,ncmp-1,ncmp):
#   ax6.plot(rho,w[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    ax6.plot(rho,Zeff[kk],linsyb[kk],linewidth=2,label=nsyb[kk])
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
#    ylabel('$\omega(krad s^-1)$',fontsize=fs2,family='serif')
    ylabel('$z_{eff}$',fontsize=fs2,family='serif')
    xlabel('$rho$',fontsize=fs2,family='serif')
#    ylim([-60,0])
#    text(xtext,-6,'(f)',fontsize=fs3)
    legend(loc='lower right',fontsize=fs1).draggable(True)
