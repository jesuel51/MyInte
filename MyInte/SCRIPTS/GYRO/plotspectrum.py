# this script is used to plot the spectrum of omega(ky) & gamma(ky) for a given rho
# Read some input parameter
iplotErr=root['SETTINGS']['PLOTS']['iplotErr']
if root['INPUTS']['GYROInput']['input.gyro'].has_key('L_Y'):
    L_Y=root['INPUTS']['GYROInput']['input.gyro']['L_Y'] # the reference ky
else:
    L_Y=0.3
if root['INPUTS']['GYROInput']['input.gyro'].has_key('TOROIDAL_GRID'):
    TOROIDAL_GRID=root['INPUTS']['GYROInput']['input.gyro']['TOROIDAL_GRID'] # the reference ky
else:
    TOROIDAL_GRID=1
if root['INPUTS']['GYROInput']['input.gyro'].has_key('TOROIDAL_MIN'):
    TOROIDAL_MIN=root['INPUTS']['GYROInput']['input.gyro']['TOROIDAL_MIN'] # the reference ky
else:
    TOROIDAL_MIN=30
if root['INPUTS']['GYROInput']['input.gyro'].has_key('TOROIDAL_SEP'):
    TOROIDAL_SEP=root['INPUTS']['GYROInput']['input.gyro']['TOROIDAL_SEP'] # the reference ky
else:
    TOROIDAL_SEP=10

k=root['SETTINGS']['PLOTS']['ipltspectrum']
#wr=ones(TOROIDAL_GRID)
#wr_err=ones(TOROIDAL_GRID)
#wi=ones(TOROIDAL_GRID)
#wi_err=ones(TOROIDAL_GRID)
#for k in linspace(0,TOROIDAL_GRID-1,TOROIDAL_GRID):
wr=root['OUTPUTSRec']['GYROOutput'][k]['wr']
wi=root['OUTPUTSRec']['GYROOutput'][k]['wi']
wr_err=root['OUTPUTSRec']['GYROOutput'][k]['wr_err']
wi_err=root['OUTPUTSRec']['GYROOutput'][k]['wi_err']
# calculate ky
ky=L_Y/TOROIDAL_MIN*(TOROIDAL_MIN+linspace(0,TOROIDAL_GRID-1,TOROIDAL_GRID)*TOROIDAL_SEP)
#rho=root['INPUTS']['GYROInput']['input.gyro']['RADIUS']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho_max=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
rho_all=linspace(0,rho_max,p_tgyro+1)
rho=rho_all[k]
figure(5)
fsize=24
subplot(1,2,1)
#plot(ky,wr,'-bo',linewidth=2,label='rho='+str(rho)+' $\omega$')
plot(ky,wr,'-bo',linewidth=2,label='$\omega$')
if iplotErr==1:
    plot(ky,wr_err,'-ro',linewidth=2,label='$Error$')
    legend(loc=0).draggable(True)
xlabel('$k_y$',fontsize=fsize,family='serif')
ylabel('$\omega$',fontsize=fsize,family='serif')
xticks(fontsize=16,family='serif')
yticks(fontsize=16,family='serif')
title('rho='+str(rho))
subplot(1,2,2)
plot(ky,wi,'-b*',linewidth=2,label='$\gamma$')
if iplotErr==1:
    plot(ky,wi_err,'-r*',linewidth=2,label='$Error$')
    legend(loc=0).draggable(True)
xticks(fontsize=16,family='serif')
yticks(fontsize=16,family='serif')
xlabel('$k_y$',fontsize=fsize,family='serif')
ylabel('$\gamma$',fontsize=fsize,family='serif')
title('rho='+str(rho))
