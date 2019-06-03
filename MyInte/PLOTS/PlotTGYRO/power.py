#-*-Python-*-
# Created by xiangjian at 2015/05/04 21:32
k=root['SETTINGS']['PLOTS']['iview']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
plt.close()
#power_e=root['OUTPUTSRec']['TGYROOutput']['power'][k]['data'];
power_e=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.power_e']['data'];
power_e=map(list,zip(*power_e));
power_i=root['OUTPUTSRec']['TGYROOutput'][k]['out.tgyro.power_i']['data'];
power_i=map(list,zip(*power_i));
geometry=root['OUTPUTSRec']['TGYROOutput'][int(k)]['out.tgyro.geometry.1']['data']
geometry=map(list,zip(*geometry))
rho=geometry[1]
fus_e=power_e[1]
aux_e=power_e[2]
brem_e=power_e[3]
sync_e=power_e[4]
line_e=power_e[5]
exch_e=-1.*power_e[6]
expwd_e=-1*power_e[7]
fus_i=power_i[1]
aux_i=power_i[2]
exch_i=power_i[3]
expwd_i=power_i[4]
figure(221)
subplot(2,1,1)
plot(rho,fus_e,'-r*',label='fus-e')
plot(rho,aux_e,'-k*',label='aux-e')
plot(rho,brem_e,'-b*',label='brem-e')
plot(rho,sync_e,'-ro',label='sync-e')
plot(rho,line_e,'-ko',label='line-e')
plot(rho,exch_e,'-bo',label='exch-e')
plot(rho,expwd_e,'-rd',label='expwd-e')
legend(loc=0).draggable(True)
xlabel('$rho$')
ylabel('$Pow_e-MW$')
subplot(2,1,1)
plot(rho,fus_i,'-r*',label='fus-i')
plot(rho,aux_i,'-k*',label='aux-i')
plot(rho,exch_i,'-r*',label='exch-i')
plot(rho,expwd_i,'-r*',label='expwd-i')
legend(loc=0).draggable(True)
xlabel('$rho$')
ylabel('$Pow_i-MW$')

