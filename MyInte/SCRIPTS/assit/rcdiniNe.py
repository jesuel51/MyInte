# this script is used to record the initial ne profile in sparse grid use for pedestal region
rho_ped=root['SETTINGS']['PHYSICS']['rho_ped']
rho_pvt=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
#ibccond=root['SETTINGS']['PHYSICS']['ibccond']
rho_sparse=linspace(rho_pvt,rho_ped,floor((rho_ped-rho_pvt)/0.04)+1)
if len(rho_sparse)==1:
    rho_sparse=list(rho_sparse)
    rho_sparse.append(rho_ped)
    rho_sparse=array(rho_sparse)
#nj=root['SETTINGS']['PHYSICS']['nj']
nj=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['NJENE']
rho_12=linspace(0,1,nj)
root['SETTINGS']['PHYSICS']['ENEIN']=spline(rho_12,root['INPUTS']['ONETWOInput']['inone']['namelis1']['ENEIN'],rho_sparse)
root['SETTINGS']['PHYSICS']['rho_sparse']=rho_sparse
#root['SETTINGS']['PHYSICS']['drho_tgyro']=drho
