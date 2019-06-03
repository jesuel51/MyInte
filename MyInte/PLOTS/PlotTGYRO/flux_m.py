plt.close();
k=root['SETTINGS']['PLOTS']['iview']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
mflux_e=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.mflux_e']['data'];
mflux_e=map(list,zip(*mflux_e));
mflux_i=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.mflux_i']['data'];
mflux_i=map(list,zip(*mflux_i));
mflux_i2=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.mflux_i2']['data'];
mflux_i2=map(list,zip(*mflux_i2));
mflux_i3=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.mflux_i3']['data'];
mflux_i3=map(list,zip(*mflux_i3));
geometry=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.geometry.1']['data']
geometry=map(list,zip(*geometry))
rho=geometry[1]
figure(261)
subplot(2,2,1)
plot(rho,mflux_e[1][1:p_tgyro+2],'-bd',linewidth=2,markersize=6,label='mflux-neo')
plot(rho,mflux_e[2][1:p_tgyro+2],'-ro',linewidth=2,markersize=6,label='mflux-tur')
#plot(rho,mflux_e[3][1:p_tgyro+2],'-bo',markersize=6,label='expwd-tur')
legend(loc=0).draggable(True)
ylabel('Electron Flux-GB')
subplot(2,2,2)
plot(rho,mflux_i[1][1:p_tgyro+2],'-bd',linewidth=2,markersize=6,label='mflux-neo')
plot(rho,mflux_i[2][1:p_tgyro+2],'-ro',linewidth=2,markersize=6,label='mflux-tur')
#plot(rho,mflux_i[4][1:p_tgyro+2],'-bo',markersize=6,label='expwd-tur')
legend(loc=0).draggable(True)
ylabel('DT Flux-GB')
subplot(2,2,3)
plot(rho,mflux_i2[1][1:p_tgyro+2],'-bd',linewidth=2,markersize=6,label='mflux-neo')
plot(rho,mflux_i2[2][1:p_tgyro+2],'-ro',linewidth=2,markersize=6,label='mflux-tur')
#plot(rho,mflux_i2[3][1:p_tgyro+2],'-bo',markersize=6,label='expwd-tur')
legend(loc=0).draggable(True)
ylabel('He Flux-GB')
xlabel('$rho$')
subplot(2,2,4)
plot(rho,mflux_i3[1][1:p_tgyro+2],'-bd',linewidth=2,markersize=6,label='mflux-neo')
plot(rho,mflux_i3[2][1:p_tgyro+2],'-ro',linewidth=2,markersize=6,label='mflux-tur')
#plot(rho,mflux_i3[3][1:p_tgyro+2],'-bo',markersize=6,label='expwd-tur')
legend(loc=0).draggable(True)
ylabel('Ar Flux-GB')
xlabel('$rho$')
