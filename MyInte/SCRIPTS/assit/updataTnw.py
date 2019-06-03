# this script is used to update the outputs profile calculated by TGYRO
ismoothpivot=root['SETTINGS']['PHYSICS']['ismoothpivot']
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
profile=root['OUTPUTS']['TGYROOutput']['out.tgyro.profile']['data'];
geometry1=root['OUTPUTS']['TGYROOutput']['out.tgyro.geometry.1']['data'];
gyrobohm=root['OUTPUTS']['TGYROOutput']['out.tgyro.gyrobohm']['data'];
flux=root['OUTPUTS']['TGYROOutput']['out.tgyro.flux_target']['data'];
profile=array(map(list,zip(*profile)))
geometry1=array(map(list,zip(*geometry1)))
gyrobohm=array(map(list,zip(*gyrobohm)))
ne_t=profile[2];
Ti_t=profile[3];
Te_t=profile[4];
root['SETTINGS']['PHYSICS']['TIIN_TGYRO']=Ti_t
root['SETTINGS']['PHYSICS']['TEIN_TGYRO']=Te_t
root['SCRIPTS']['assit']['useiniT2.py'].run()
Ti_t=root['SETTINGS']['PHYSICS']['TIIN_TGYRO']
Te_t=root['SETTINGS']['PHYSICS']['TEIN_TGYRO']
w0_t=profile[8];
gcs=gyrobohm[5][0:p_tgyro+1];   #get the cs data
gcs=[float(x) for x in gcs]
rmaj=geometry1[9];
rmaj=[x*1.6 for x in geometry1[9]]
w0_t=w0_t*gcs/rmaj;
# the old profile
Te_old=root['INPUTS']['TGYROInput']['input.profiles']['Te']
Ti_old=root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']
ne_old=root['INPUTS']['TGYROInput']['input.profiles']['ne']
w0_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
rho_pivot=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
np_tgyro=len(ne_t)
nj=root['SETTINGS']['PHYSICS']['nj']
r_12=linspace(0,1,nj)
r_t=linspace(0,rho_pivot,np_tgyro);     # denotes r_tgyro here
num_rho=len(r_12)
num_r=floor(rho_pivot*(nj-1))
if ismoothpivot==1:
    n_add=[floor(float(nj-1)/np_tgyro*0.25)+num_r,floor(float(nj-1)/np_tgyro*0.5)+num_r]
    r_t_add=r_12[n_add]
    Te_t_add=Te_old[n_add]
    Ti_t_add=Ti_old[n_add]
    ne_t_add=ne_old[n_add]
    w0_t_add=w0_old[n_add]
    r_t=concatenate((r_t,r_t_add))
    Te_t=concatenate((Te_t,Te_t_add))
    Ti_t=concatenate((Ti_t,Ti_t_add))
    ne_t=concatenate((ne_t,ne_t_add))
    w0_t=concatenate((w0_t,w0_t_add))
Te_new=ones(num_rho)
Ti_new=ones(num_rho)
ne_new=ones(num_rho)
w0_new=ones(num_rho)
# update n&T&w profile
Te_new[0:(num_r-1)]=spline(r_t,Te_t,r_12[0:(num_r-1)])
Ti_new[0:(num_r-1)]=spline(r_t,Ti_t,r_12[0:(num_r-1)])
ne_new[0:(num_r-1)]=spline(r_t[0:-2],ne_t[0:-2],r_12[0:(num_r-1)])/1.e13
w0_new[0:(num_r-1)]=spline(r_t,w0_t,r_12[0:(num_r-1)])
Te_new[num_r-1:num_rho]=Te_old[num_r-1:num_rho]
Ti_new[num_r-1:num_rho]=Ti_old[num_r-1:num_rho]
ne_new[num_r-1:num_rho]=ne_old[num_r-1:num_rho]
w0_new[num_r-1:num_rho]=w0_old[num_r-1:num_rho]
root['SETTINGS']['TEMP']['Te']=Te_new
root['SETTINGS']['TEMP']['Ti']=Ti_new
root['SETTINGS']['TEMP']['ne']=ne_new
root['SETTINGS']['TEMP']['w0']=w0_new
