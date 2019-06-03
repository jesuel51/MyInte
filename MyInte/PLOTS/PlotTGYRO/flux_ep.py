# this script is used to plot the 
#plt.close();
isemiplt=root['SETTINGS']['PLOTS']['isemiplt']
IonSp=root['SETTINGS']['PLOTS']['IonSp']
ipltpflux=root['SETTINGS']['PLOTS']['ipltpflux']
k=root['SETTINGS']['PLOTS']['iview']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
flux_e=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.flux_e']['data'];
flux_e=map(list,zip(*flux_e));
flux_i=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.flux_i']['data'];
flux_i=map(list,zip(*flux_i));
flux_i2=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.flux_i2']['data'];
flux_i2=map(list,zip(*flux_i2));
flux_i3=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.flux_i3']['data'];
flux_i3=map(list,zip(*flux_i3));
geometry=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.geometry.1']['data']
geometry=map(list,zip(*geometry))
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho=geometry[1]
mksz=8      # markersize
fs1=16      # fontsize
fs2=24      # fontsize
fml='serif' # font famlily
lwd=2       # linewidth
figure(241)
subplot(2,2,1)
if isemiplt==1:
    semilogy(rho,flux_e[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
    semilogy(rho,flux_e[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    semilogy(rho,flux_e[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    semilogy(rho,flux_e[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
else:
    plot(rho,flux_e[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
    plot(rho,flux_e[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    plot(rho,flux_e[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    plot(rho,flux_e[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
legend(loc=0,fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel('Electron Flux-GB',fontsize=fs2,family=fml)
subplot(2,2,2)
if isemiplt==1:
    if ipltpflux==1:
        semilogy(rho,flux_i[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        semilogy(rho,flux_i[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    semilogy(rho,flux_i[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    semilogy(rho,flux_i[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
else:
    if ipltpflux==1:
        plot(rho,flux_i[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        plot(rho,flux_i[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    plot(rho,flux_i[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    plot(rho,flux_i[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
legend(loc=0,fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel(IonSp[0]+' Flux-GB',fontsize=fs2,family=fml)
subplot(2,2,3)
if isemiplt==1:
    if ipltpflux==1:
        semilogy(rho,flux_i2[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        semilogy(rho,flux_i2[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    semilogy(rho,flux_i2[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    semilogy(rho,flux_i2[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
else:
    if ipltpflux==1:
        plot(rho,flux_i2[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        plot(rho,flux_i2[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    plot(rho,flux_i2[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    plot(rho,flux_i2[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
legend(loc=0,fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
ylabel(IonSp[1]+' Flux-GB',fontsize=fs2,family=fml)
xlabel('rho',fontsize=fs2,family=fml)
subplot(2,2,4)
if isemiplt==1:
    if ipltpflux==1:
        semilogy(rho,flux_i3[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        semilogy(rho,flux_i3[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    semilogy(rho,flux_i3[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    semilogy(rho,flux_i3[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
else:
    if ipltpflux==1:
        plot(rho,flux_i3[1][1:p_tgyro+2],'-b*',linewidth=lwd,markersize=mksz,label='pflux-neo')
        plot(rho,flux_i3[2][1:p_tgyro+2],'-bo',linewidth=lwd,markersize=mksz,label='pflux-tur')
    plot(rho,flux_i3[3][1:p_tgyro+2],'-r*',linewidth=lwd,markersize=mksz,label='eflux-neo')
    plot(rho,flux_i3[4][1:p_tgyro+2],'-ro',linewidth=lwd,markersize=mksz,label='eflux-tur')
legend(loc=0,fontsize=fs1).draggable(True)
ylabel(IonSp[2]+' Flux-GB',fontsize=fs2,family=fml)
xticks(fontsize=fs1,family=fml)
yticks(fontsize=fs1,family=fml)
xlabel('rho',fontsize=fs2,family=fml)
