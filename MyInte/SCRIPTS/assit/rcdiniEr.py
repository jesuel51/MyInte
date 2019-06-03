# this script is used to record the initial T profile in sparse grid
rho_pvt=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho_tgyro=linspace(0,rho_pvt,p_tgyro+1)
drho=rho_pvt/float(p_tgyro)
nj=root['SETTINGS']['PHYSICS']['nj']
rho_12=linspace(0,1,nj)
inormEr=root['SETTINGS']['PHYSICS']['inormEr']
if inormEr==0:
    root['SETTINGS']['PHYSICS']['omega_sparse']=spline(rho_12,root['SETTINGS']['PHYSICS']['omega0'],rho_tgyro)
else:
    root['SETTINGS']['PHYSICS']['omega_sparse']=spline(rho_12,root['SETTINGS']['PHYSICS']['omega0_norm'],rho_tgyro)
root['SETTINGS']['PHYSICS']['drho_tgyro']=drho
