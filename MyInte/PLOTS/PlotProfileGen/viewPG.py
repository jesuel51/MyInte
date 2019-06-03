#-*-Python-*-
# Created by xiangjian at 2015/05/04 21:32
k=root['SETTINGS']['PLOTS']['iview']
rho=root['OUTPUTSRec']['ProfileGenOutput'][k]['rho']
rmin=root['OUTPUTSRec']['ProfileGenOutput'][k]['rmin']
q=root['OUTPUTSRec']['ProfileGenOutput'][k]['q']
Pow_e=root['OUTPUTSRec']['ProfileGenOutput'][k]['pow_e']
Pow_i=root['OUTPUTSRec']['ProfileGenOutput'][k]['pow_i']
Te=root['OUTPUTSRec']['ProfileGenOutput'][k]['Te']
Ti=root['OUTPUTSRec']['ProfileGenOutput'][k]['Ti_1']
ne=root['OUTPUTSRec']['ProfileGenOutput'][k]['ne']
w0=root['OUTPUTSRec']['ProfileGenOutput'][k]['omega0']
curden=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curden']['data'][-1]
flow_mom=root['OUTPUTSRec']['ProfileGenOutput'][k]['flow_mom']
flow_beam=root['OUTPUTSRec']['ProfileGenOutput'][k]['flow_beam']
flow_wall=root['OUTPUTSRec']['ProfileGenOutput'][k]['flow_wall']
Cs=2.2e5*sqrt(Te)
a=rmin[-1]
adCs=a/Cs
num=len(rho)
s=(log(q[2:num-1])-log(q[1:num-2]))/(log(rmin[2:num-1])-log(rmin[1:num-2]))
Gamma_E=-(rmin[1:num]+rmin[0:num-1])/(q[1:num]+q[0:num-1])*(w0[0:num-1]-w0[1:num])/(rmin[0:num-1]-rmin[1:num])
Gamma_p=-5.6*(w0[0:num-1]-w0[1:num])/(rmin[0:num-1]-rmin[1:num])
adCs_s=(adCs[1:num]+adCs[0:num-1])/2.
rmin_s=(rmin[2:num-1]+rmin[1:num-2])/2.
rmin_Gamma=(rmin[1:num]+rmin[0:num-1])/2
if q[0]<0:
    sign=-1
else:
    sign=1
figure(111)
left_axis=subplot(2,5,1)
right_axis=left_axis.twinx()
left_axis.plot(rho,sign*q,'-bo',linewidth=2)
right_axis.plot(rmin_s/1.6,s,'-ro',linewidth=2)
right_axis.plot(rmin_s/1.6,zeros(num-3),'-r')
right_axis.set_ylabel('s')
right_axis.yaxis.label.set_color('r')
#xlabel('$rho$')
if q[0]<0:
    ylabel('$q(-)$')
else:
    ylabel('$q$')
subplot(2,5,2)
plot(rho,Te,'-bo',linewidth=2)
#xlabel('$rho$')
ylabel('$Te- keV$')
subplot(2,5,3)
plot(rho,Ti,'-bo',linewidth=2)
#xlabel('$rho$')
ylabel('$Ti- keV$')
subplot(2,5,4)
plot(rho,ne,'-bo',linewidth=2)
#xlabel('$rho$')
ylabel('$ne- 10^{19} m^-3$')
left_axis=subplot(2,5,5)
p1,=left_axis.plot(rho,w0/1.e3,'-bo',linewidth=2)
right_axis=left_axis.twinx()
p2,=right_axis.plot(rmin_Gamma/rmin[-1],10*adCs_s*Gamma_E,'-ro',label='10*Gamma_E')
#p2,=right_axis.semilogy(rmin_Gamma/rmin[-1],10*adCs_s*Gamma_E,'-ro',label='10*Gamma_E')
p3,=right_axis.plot(rmin_Gamma/rmin[-1],adCs_s*Gamma_p,'-r*',label='Gamma_p')
#p3,=right_axis.semilogy(rmin_Gamma/rmin[-1],adCs_s*Gamma_p,'-r*',label='Gamma_p')
right_axis.set_ylim(5.e-3,5.e-1)
xlabel('$rho$')
left_axis.set_ylabel('$rotation -krad s^{-1}$')
right_axis.set_ylabel('Gamma')
legend(loc=0).draggable(True)
subplot(2,5,6)
plot(rho,curden/100,'-bo',linewidth=2)
xlabel('$rho$')
ylabel('$<Jt>- MA m^{-2}$')
subplot(2,5,7)
plot(rho,Pow_e,'-bo',linewidth=2)
xlabel('$rho$')
ylabel('$Powe- MW$')
subplot(2,5,8)
plot(rho,Pow_i,'-bo',linewidth=2)
xlabel('$rho$')
ylabel('$Powi- MW$')
subplot(2,5,9)
semilogy(rho,flow_wall,'-r*',linewidth=2,label='wall')
semilogy(rho,flow_beam,'-k*',linewidth=2,label='beam')
semilogy(rho,flow_beam+flow_wall,'-bo',linewidth=2,label='total')
legend(loc=0).draggable(True)
xlabel('$rho$')
ylabel('$Particle source-kW/eV$')
subplot(2,5,10)
plot(rho,flow_mom,'-bo',linewidth=2)
xlabel('$rho$')
ylabel('$momentum source- Nm$')
#figure(1)
#plot(rho,Cs,'-r*')
#xlabel('rho')
#ylabel('Cs')

