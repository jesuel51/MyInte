# this script is used to link the between the module MyInte and ForW
# first the tgyro input needs to be transferred
tgyroin_forw=root['ForW']['INPUTS']['TGYRO']
tgyroin_myinte=root['INPUTS']['TGYROInput']
inputfile=['input.tgyro','input.profiles','input.profiles.geo']
for item in inputfile:
    tgyroin_forw[item]=tgyroin_myinte[item].duplicate()
print(tgyroin_forw['input.tgyro'].keys())
if tgyroin_forw['input.tgyro'].has_key('TGYRO_RMIN'):
    print('hello')
    del tgyroin_forw['input.tgyro']['TGYRO_RMIN']
# this maybe important for the correct reconstruction of W profile
tgyroin_forw['input.tgyro']['LOC_HE_FEEDBACK_FLAG']=0

#root['ForW']['SETTINGS']['PHYSICS']['FracImp']=root['SETTINGS']['PHYSICS']['FracImp']
# determine tglf or neo or both needs to be used for reconstructing the profile
root['ForW']['SETTINGS']['PLOTS']['iplotpro']=0
root['ForW']['SETTINGS']['SETUP']['consflag']=root['SETTINGS']['PHYSICS']['reconsImp']
if 'neo' in root['ForW']['SETTINGS']['SETUP']['consflag']:
    root['ForW']['SETTINGS']['SETUP']['irunneo']=1
else:
    root['ForW']['SETTINGS']['SETUP']['irunneo']=0
OMFIT['MyInte']['ForW']['SCRIPTS']['proctrl.py'].run()
# interporation 
rho_t=root['ForW']['SETTINGS']['DEPENDENCIES']['rho_t']
n_imp=root['ForW']['SETTINGS']['DEPENDENCIES']['n_imp']
rho=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['RENEIN']
ene=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']
# get the density of the the pivot point
rho_pvt=tgyroin_forw['input.tgyro']['TGYRO_RMAX']
num_r=int((len(rho)-1)*rho_pvt)
ne_pvt=ene[num_r]
#n_imp=n_imp*ne_pvt*root['ForW']['SETTINGS']['PHYSICS']['FracImp']
# the tungsten profile outside the pivot point is set to be the same shape of the electron density profile
ene_nor=ene/ne_pvt;    # normalized electron density profile by the pivot point
nj=len(ene)
np_tgyro=len(tgyroin_myinte['input.tgyro']['DIR'].keys())
n_add=[floor(float(nj-1)/np_tgyro*0.2)+num_r,floor(float(nj-1)/np_tgyro*0.3)+num_r]
rho_t_add=rho[n_add]
n_imp_add=ene_nor[n_add]
rho_t_full=concatenate((rho_t,rho_t_add))
n_imp_full=concatenate((n_imp,n_imp_add))
n_imp_ref=zeros(nj)
n_imp_ref[0:num_r]=spline(rho_t_full,n_imp_full,rho[0:num_r])
n_imp_ref[num_r:]=ene_nor[num_r:]
# get the whole tungsten profile
n_imp_ref=n_imp_ref*ne_pvt*root['SETTINGS']['PHYSICS']['FracImp']
# transfer it to the dependencies
root['SETTINGS']['DEPENDENCIES']['W']=n_imp_ref
