# this script is used to plot different species' contribution to transport
#plt.close()
mksz=8      # markersize
fs1=16      # fontsize
fs2=24      # fontsize
fml='serif' # font famlily
lwd=2       # linewidth
k=root['SETTINGS']['PLOTS']['iview']
IonSp=root['SETTINGS']['PLOTS']['IonSp']
Charge=root['SETTINGS']['PHYSICS']['ChargeForMerge']
isemiplt=root['SETTINGS']['PLOTS']['isemiplt']
#rho=root['SETTINGS']['PLOTS']['rho']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho_pvt=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
rho=linspace(0,rho_pvt,p_tgyro+1)
flux_e=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.flux_e']['data']
flux_e=map(list,zip(*flux_e))
flux_i=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.flux_i']['data']
flux_i=map(list,zip(*flux_i))
flux_i2=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.flux_i2']['data']
flux_i2=map(list,zip(*flux_i2))
flux_i3=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.flux_i3']['data']
flux_i3=map(list,zip(*flux_i3))
pflux_e_neo=flux_e[1][1:p_tgyro+2]
pflux_e_neo=array([float(p) for p in pflux_e_neo])
pflux_e_tur=flux_e[2][1:p_tgyro+2]
pflux_e_tur=array([float(p) for p in pflux_e_tur])
eflux_e_neo=flux_e[3][1:p_tgyro+2]
eflux_e_neo=array([float(p) for p in eflux_e_neo])
eflux_e_tur=flux_e[4][1:p_tgyro+2]
eflux_e_tur=array([float(p) for p in eflux_e_tur])
pflux_i_neo=flux_i[1][1:p_tgyro+2]
pflux_i_neo=array([float(p) for p in pflux_i_neo])
pflux_i_tur=flux_i[2][1:p_tgyro+2]
pflux_i_tur=array([float(p) for p in pflux_i_tur])
eflux_i_neo=flux_i[3][1:p_tgyro+2]
eflux_i_neo=array([float(p) for p in eflux_i_neo])
eflux_i_tur=flux_i[4][1:p_tgyro+2]
eflux_i_tur=array([float(p) for p in eflux_i_tur])
pflux_i2_neo=flux_i2[1][1:p_tgyro+2]
pflux_i2_neo=array([float(p) for p in pflux_i2_neo])
pflux_i2_tur=flux_i2[2][1:p_tgyro+2]
pflux_i2_tur=array([float(p) for p in pflux_i2_tur])
eflux_i2_neo=flux_i2[3][1:p_tgyro+2]
eflux_i2_neo=array([float(p) for p in eflux_i2_neo])
eflux_i2_tur=flux_i2[4][1:p_tgyro+2]
eflux_i2_tur=array([float(p) for p in eflux_i2_tur])
pflux_i3_neo=flux_i3[1][1:p_tgyro+2]
pflux_i3_neo=array([float(p) for p in pflux_i3_neo])
pflux_i3_tur=flux_i3[2][1:p_tgyro+2]
pflux_i3_tur=array([float(p) for p in pflux_i3_tur])
eflux_i3_neo=flux_i3[3][1:p_tgyro+2]
eflux_i3_neo=array([float(p) for p in eflux_i3_neo])
eflux_i3_tur=flux_i3[4][1:p_tgyro+2]
eflux_i3_tur=array([float(p) for p in eflux_i3_tur])
pflux_e=pflux_e_neo+pflux_e_tur
eflux_e=eflux_e_neo+eflux_e_tur
pflux_i=pflux_i_neo+pflux_i_tur
eflux_i=eflux_i_neo+eflux_i_tur
pflux_i2=pflux_i2_neo+pflux_i2_tur
eflux_i2=eflux_i2_neo+eflux_i2_tur
pflux_i3=pflux_i3_neo+pflux_i3_tur
eflux_i3=eflux_i3_neo+eflux_i3_tur
eflux_ii=eflux_i+eflux_i2+eflux_i3
pflux_ii=pflux_i*Charge[0]+pflux_i2*Charge[1]+pflux_i3*Charge[2]
#figure('title','istropic effect on transport')
figure(251)
subplot(1,2,1)
if isemiplt==1:
    semilogy(rho,pflux_i,'-bo',linewidth=2,markersize=mksz,label=IonSp[0])
    semilogy(rho,pflux_i2,'-b*',linewidth=2,markersize=mksz,label=IonSp[1])
    semilogy(rho,pflux_i3,'-bs',linewidth=2,markersize=mksz,label=IonSp[2])
    semilogy(rho,pflux_ii,'-ro',linewidth=2,markersize=mksz,label='Sum-i')
    semilogy(rho,pflux_e,'-r*',linewidth=2,markersize=mksz,label='Electrons')
else:
    plot(rho,pflux_i,'-bo',linewidth=2,markersize=mksz,label=IonSp[0])
    plot(rho,pflux_i2,'-b*',linewidth=2,markersize=mksz,label=IonSp[1])
    plot(rho,pflux_i3,'-bs',linewidth=2,markersize=mksz,label=IonSp[2])
    plot(rho,pflux_ii,'-ro',linewidth=2,markersize=mksz,label='Sum-i')
    plot(rho,pflux_e,'-r*',linewidth=2,markersize=mksz,label='Electrons')
xlim(0,1)
legend(loc=0,fontsize=fs1).draggable(True)
ylabel('$PFlux_i/GB$',fontsize=fs2,family=fml)
xlabel('rho',fontsize=fs2,family=fml)
xticks(fontsize=fs2,family=fml)
yticks(fontsize=fs2,family=fml)
subplot(1,2,2)
if isemiplt==1:
    semilogy(rho,eflux_i,'-bo',linewidth=2,label=IonSp[0])
    semilogy(rho,eflux_i2,'-b*',linewidth=2,label=IonSp[1])
    semilogy(rho,eflux_i3,'-bs',linewidth=2,label=IonSp[2])
    semilogy(rho,eflux_ii,'-ro',linewidth=2,label='Sum-i')
    semilogy(rho,eflux_e,'-r*',linewidth=2,label='Electron')
else:
    plot(rho,eflux_i,'-bo',linewidth=2,label=IonSp[0])
    plot(rho,eflux_i2,'-b*',linewidth=2,label=IonSp[1])
    plot(rho,eflux_i3,'-bs',linewidth=2,label=IonSp[2])
    plot(rho,eflux_ii,'-ro',linewidth=2,label='Sum-i')
    plot(rho,eflux_e,'-r*',linewidth=2,label='Electron')
xlim(0,1)
legend(loc=0,fontsize=fs1).draggable(True)
ylabel('Energy Flux',fontsize=fs2,family=fml)
xlabel('rho',fontsize=fs2,family=fml)
xticks(fontsize=fs2,family=fml)
yticks(fontsize=fs2,family=fml)
