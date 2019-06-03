# this script is used to record the initial Ne profile in sparse grid for the core region
rho_pvt=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
rho_tgyro=linspace(0,rho_pvt,p_tgyro+1)
drho=rho_pvt/float(p_tgyro)
nj=root['SETTINGS']['PHYSICS']['nj']
rho_12=linspace(0,1,nj)
root['SETTINGS']['PHYSICS']['NEIN']=spline(rho_12,root['INPUTS']['ONETWOInput']['inone']['namelis1']['ENEIN'],rho_tgyro)
root['SETTINGS']['PHYSICS']['drho_tgyro']=drho
