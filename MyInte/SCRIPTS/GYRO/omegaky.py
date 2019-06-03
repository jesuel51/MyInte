# this script is used to plot the omega(gamma) vs the ky of the current calculation
# which I mean, the output is stored in GYROoutput instead of GYROoutputrecord
# firstly, set some default value
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

# get the data
wr=ones(TOROIDAL_GRID)
wr_err=ones(TOROIDAL_GRID)
wi=ones(TOROIDAL_GRID)
wi_err=ones(TOROIDAL_GRID)
for k in linspace(0,TOROIDAL_GRID-1,TOROIDAL_GRID):
    wr[k]=root['OUTPUTS']['GYROOutput']['out.gyro.freq']['data'][-TOROIDAL_GRID:][k][0]
    wi[k]=root['OUTPUTS']['GYROOutput']['out.gyro.freq']['data'][-TOROIDAL_GRID:][k][1]
    wr_err[k]=root['OUTPUTS']['GYROOutput']['out.gyro.freq']['data'][-TOROIDAL_GRID:][k][2]
    wi_err[k]=root['OUTPUTS']['GYROOutput']['out.gyro.freq']['data'][-TOROIDAL_GRID:][k][3]
# record the result
root['SETTINGS']['TEMP']['wr']=wr
root['SETTINGS']['TEMP']['wi']=wi
root['SETTINGS']['TEMP']['wr_err']=wr_err
root['SETTINGS']['TEMP']['wi_err']=wi_err
ky=L_Y/TOROIDAL_MIN*(TOROIDAL_MIN+linspace(0,TOROIDAL_GRID-1,TOROIDAL_GRID)*TOROIDAL_SEP)
rho=root['INPUTS']['GYROInput']['input.gyro']['RADIUS']
figure(5)
fsize=24
subplot(1,2,1)
plot(ky,wr,'-bo',linewidth=2,label='rho='+str(rho)+' $\omega$')
if iplotErr==1:
    plot(ky,wr_err,'-ro',linewidth=2,label='rho='+str(rho)+' $Error$')
    legend(loc=0).draggable(True)
xlabel('$k_y$',fontsize=fsize)
ylabel('$\omega$',fontsize=fsize)
#title('rho='+str(rho))
subplot(1,2,2)
plot(ky,wi,'-b*',linewidth=2,label='rho'+str(rho)+' $\gamma$')
if iplotErr==1:
    plot(ky,wi_err,'-r*',linewidth=2,label='rho='+str(rho)+' $Error$')
    legend(loc=0).draggable(True)
xlabel('$k_y$',fontsize=fsize)
ylabel('$\gamma$',fontsize=fsize)
#title('rho='+str(rho))
