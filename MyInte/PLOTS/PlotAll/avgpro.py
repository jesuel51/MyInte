import numpy as np
ipltcmp=root['SETTINGS']['PLOTS']['ipltcmp']
k=root['SETTINGS']['PLOTS']['iview']
ncmp=root['SETTINGS']['PLOTS']['ncmp']
nj=len(root['OUTPUTSRec']['ProfileGenOutput'][k]['rho'])
q=np.zeros([ncmp,nj])
Te=np.zeros([ncmp,nj])
Ti=np.zeros([ncmp,nj])
ne=np.zeros([ncmp,nj])
w=np.zeros([ncmp,nj])
cur=np.zeros([ncmp,nj])
for kk in linspace(k,k+ncmp-1,ncmp):
    rho=root['OUTPUTSRec']['ProfileGenOutput'][kk]['rho']
#    q[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['q']
    q[kk-k]=root['INPUTSRec']['TGYRO'][kk]['input.profiles']['q']
    Te[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['Te']
    Ti[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['Ti_1']
    ne[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['ne']
    w[kk-k]=root['OUTPUTSRec']['ProfileGenOutput'][kk]['omega0']
    cur[kk-k]=root['OUTPUTSRec']['ONETWOOutput'][int(kk)]['trpltout.nc']['curden']['data'][-1]/100.
q_avg=np.mean(q,0)
Te_avg=np.mean(Te,0)
Ti_avg=np.mean(Ti,0)
ne_avg=np.mean(ne,0)
w_avg=np.mean(w,0)
cur_avg=np.mean(cur,0)

#plt.close()
w=w/1.e3
fs1=16
fs2=24
fs3=24
linsyb=array(['-b','-r*','-b*','-k*','-ro','-bo','-ko','-r+','-b+','-k+'])
nsyb=array([str(k),str(k+1),str(k+2),str(k+3),str(k+4),str(k+5),str(k+6),str(k+7),str(k+8)])
###############################################
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
num_sym=0
#subplot(3,2,1)
ax1=plt.axes(Rct1)
for kk in array([num_sym]):
    ax1.plot(rho,q_avg,linsyb[kk],linewidth=2)
    #ylabel('q('+str(qsign)[0]+')',fontsize=fs2,family='serif')
    ylabel('$q$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks([1,2,4,6,8],fontsize=fs1,family='serif')
#    legend(loc=0,fontsize=fs1).draggable(True)
    ylim([0,8])
    text(xtext,7.4,'(a)',fontsize=fs3)
#subplot(3,2,2)
ax2=plt.axes(Rct2)
for kk in array([num_sym]):
    ax2.plot(rho,cur_avg,linsyb[kk],linewidth=2)
    ylabel('$<J>(MA m^{-2})$',fontsize=fs2-4,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylim(0,1.8)
    text(xtext,1.35,'(b)',fontsize=fs3)
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,5)
ax5=plt.axes(Rct5)
for kk in array([num_sym]):
    ax5.plot(rho,ne_avg,linsyb[kk],linewidth=2)
    xlabel('$rho$',fontsize=fs2,family='serif')
    ylabel('$n_e(10^{19}m^{-3})$',fontsize=fs2,family='serif')
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylim([0,15])
    text(xtext,9,'(e)',fontsize=fs3)
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,4)
ax4=plt.axes(Rct4)
for kk in array([num_sym]):
    ax4.plot(rho,Ti_avg,linsyb[kk],linewidth=2)
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$T_i(keV)$',fontsize=fs2,family='serif')
    ylim([0,40])
    text(xtext,27,'(d)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,3)
ax3=plt.axes(Rct3)
for kk in array([num_sym]):
    ax3.plot(rho,Te_avg,linsyb[kk],linewidth=2)
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$T_e(keV)$',fontsize=fs2,family='serif')
    ylim([0,40])
    text(xtext,27,'(c)',fontsize=fs3)
#    xlabel('$rho$',fontsize=fs2,family='serif')
#    legend(loc=0,fontsize=fs1).draggable(True)
#subplot(3,2,6)
ax6=plt.axes(Rct6)
for kk in array([num_sym]):
    ax6.plot(rho,w_avg/1.e3,linsyb[kk],linewidth=2)
    xticks(fontsize=fs1,family='serif')
    yticks(fontsize=fs1,family='serif')
    ylabel('$\omega(krad s^-1)$',fontsize=fs2,family='serif')
    xlabel('$rho$',fontsize=fs2,family='serif')
    ylim([-45,0])
    text(xtext,-6,'(f)',fontsize=fs3)
#    legend(loc='lower right',fontsize=fs1).draggable(True)

