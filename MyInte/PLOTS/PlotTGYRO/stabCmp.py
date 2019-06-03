# This script is used to compare the linear stability result of TGLF(calculated using TGYRO with linear stability calculation modes) and GYRO linear modes
# Before running this script , note that the linear stability calclation using both TGYRO and GYRO should have been performed;
# compare the analysis of radius specified in root['SETTINGS']['PLOTS']['ipltspectrum']
# this scripts is used to plot the micro-stability issues for all radiuas and kyrho
plt.close()
#=============================
# load the result of TGYRO
#=============================
ptgyro=root['SETTINGS']['PLOTS']['p_tgyro']
nky=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_STAB_NKY']
Output=root['OUTPUTS']['TGYROOutput']['spectrum']
spectrum=OMFIT['MyInte']['OUTPUTS']['TGYROOutput']['spectrum']
wr_elec=spectrum['out.tgyro.wr_elec']['data']
wr_ion=spectrum['out.tgyro.wr_ion']['data']
wi_elec=spectrum['out.tgyro.wi_elec']['data']
wi_ion=spectrum['out.tgyro.wi_ion']['data']
# initialization
wr_elec_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
wr_ion_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
wi_elec_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
wi_ion_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
# get the data
ra=wr_elec['col1'][0:ptgyro+1]
for k in linspace(2,nky+1,nky):
    wr_elec_arr[int(k)-2]=wr_elec['col'+str(int(k))]
    wr_ion_arr[int(k)-2]=wr_ion['col'+str(int(k))]
    wi_elec_arr[int(k)-2]=wi_elec['col'+str(int(k))]    
    wi_ion_arr[int(k)-2]=wi_ion['col'+str(int(k))]
kyrho=[wr_elec_arr[int(k)][0] for k in linspace(0,nky-1,nky)]
lab=['-bo','-b*','-bd','-ko','-k*','-kd','-ro','-r*','-rd','-go','-g*','-gd','-yo','-y*','-yd']
iradius=root['SETTINGS']['PLOTS']['ipltspectrum'];
iradius=array([iradius])
#===================================
# load the result of GYRO
# ===================================
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
wr=root['OUTPUTSRec']['GYROOutput'][k]['wr']
wi=root['OUTPUTSRec']['GYROOutput'][k]['wi']
wr_err=root['OUTPUTSRec']['GYROOutput'][k]['wr_err']
wi_err=root['OUTPUTSRec']['GYROOutput'][k]['wi_err']
# calculate ky
ky=L_Y/TOROIDAL_MIN*(TOROIDAL_MIN+linspace(0,TOROIDAL_GRID-1,TOROIDAL_GRID)*TOROIDAL_SEP)
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho_max=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
rho_all=linspace(0,rho_max,p_tgyro+1)
rho=rho_all[k]
#================================================================
# start to plot and compare
#==============================================================
#figure('name',['ra='+str(ra[iradius])])
figure(281)
subplot(2,2,1)
for p in iradius:
    plot(kyrho,[wr_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)])
#legend(loc=0).draggable(True)
#xlabel('kyrho')
ylabel('a/cs*omega')
title('wr_elec '+'ra'+str(ra[iradius]))
subplot(2,2,2)
for p in iradius:
    plot(kyrho,[wr_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label='TGLF')
    plot(ky,wr,'-bo',linewidth=2,label='GYRO')
legend(loc=0).draggable(True)
#xlabel('kyrho')
ylabel('a/cs*omega')
title('wr_ion '+'ra'+str(ra[iradius]))
subplot(2,2,3)
for p in iradius:
    plot(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)])
#    semilogy(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p-1]))
legend(loc=0).draggable(True)
xlabel('ky*rho')
ylabel('a/cs*gamma')
title('wi_elec '+'ra'+str(ra[iradius]))
subplot(2,2,4)
for p in iradius:
    plot(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label='TGLF')
    plot(ky,wi,'-b*',linewidth=2,label='GYRO')
#    semilogy(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p-1]))
legend(loc=0).draggable(True)
xlabel('ky*rho')
ylabel('a/cs*gamma')
title('wi_ion '+'ra'+str(ra[iradius]))
