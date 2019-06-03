#-*-Python-*-
# Created by xiangjian at 2015/05/16 10:12
# this file will be used to test the equilibrium file in each code interface
plt.close()
q_12_trp_all=root['OUTPUTS']['ONETWOOutput']['trpltout.nc']['q']['data']
dim_n3d=size(q_12_trp_all,0)
nj=size(q_12_trp_all,1)
q_12_trp=q_12_trp_all[dim_n3d-1];
figure(1)
subplot(1,3,1)
rho1=linspace(0,1,nj);
plot(rho1,q_12_trp,'-r')
xlim(0,1)
ylim(0,8)
##xlabel('$\sqrt(\{phi}/{phi}0)$')
xlabel('$normalized sqrt(phi)$')
ylabel('$q_trp$')
subplot(1,3,2)
q_12_g0=root['OUTPUTS']['ONETWOOutput']['gfile']['QPSI']
nw=len(q_12_g0)
rho2=linspace(0,1,nw);
plot(rho2,q_12_g0,'-ok')
xlim(0,1)
ylim(0,8)
xlabel('$normalized psi$')
ylabel('$q_g0$')
subplot(1,3,3)
q_input_tgyro=root['INPUTS']['TGYROInput']['input.profiles']['q']
rho3=root['INPUTS']['TGYROInput']['input.profiles']['rho']
plot(rho3,-q_input_tgyro,'-*g')
xlim(0,1)
ylim(0,8)
xlabel('$normalized psi$')
ylabel('$q_input_tgyro$')
## well, since GUO says that the profile in g0 file is numerically unsatisfactory
## the commands below is used to test it
#figure(2)

