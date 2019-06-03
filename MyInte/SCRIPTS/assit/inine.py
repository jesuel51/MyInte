# this script is used to initialize the ne profile based on the density set on the pivot point
physics=root['SETTINGS']['physics']
#r_sparse=physics['rho_sparse'] # the first elecment of the rho_sparse should the radius of povit point
ne_pvt_set=physics['ne_pvt_set']  # tehe pivot density desired
ptgyro=physics['p_tgyro']
r_pvt=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
r_ped=root['SETTINGS']['PHYSICS']['rho_ped']
r_t=linspace(0,r_pvt,ptgyro+1)
#r_sparse=linspace(r_pvt,r_ped,floor((r_ped-r_pvt)/0.03)+1)
r_sparse=[r_pvt,r_ped]
ne_ref=root['SETTINGS']['DEPENDENCIES']['ne_tmplt']
nj=physics['nj']
rho_12=linspace(0,1,physics['nj'])
ne_t=spline(rho_12,ne_ref,r_t)
ne_sparse=spline(rho_12,ne_ref,r_sparse)
diffne_pvt=ne_pvt_set-ne_sparse[0]
ne_t=ne_t+diffne_pvt
ne_sparse[0]=ne_t[-1]
ne_ini=zeros(nj)
r_t_add=r_sparse[-1]
ne_t_add=ne_sparse[-1]
#r_t=concatenate((r_t[0:-1],r_t_add))
r_t=concatenate((r_t[0:-1],r_sparse))
#ne_t=concatenate((ne_t[0:-1],ne_t_add))
ne_t=concatenate((ne_t[0:-1],ne_sparse))
num_ped=int((nj-1)*r_ped)
ne_ini[0:num_ped]=spline(r_t,ne_t,rho_12[0:num_ped])
ne_ini[num_ped:]=ne_ref[num_ped:]
root['SETTINGS']['TEMP']['neini']=ne_ini
#figure('setup the densiyt of pivot point')
#subplot(1,2,1)
#plot(r_t,ne_t,'-ro')
#subplot(1,2,2)
#plot(rho_12,ne_ref,'-ro',label='ref')
#plot(rho_12,ne_ini,'-bo',label='ini')
##plot(r_t,ne_t,'-ko')
#legend(loc=0)
