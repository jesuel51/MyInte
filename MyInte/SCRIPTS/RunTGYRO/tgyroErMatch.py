# this script is used to run TGYRO with Er shear evolution
# The technique is discribed in 'obtaining from talking with stabler'
# If this script is execulated, then the switch for Er evolution is open;

# first, we shall evolve w&T when alpha_E=0
iErMatchMax=root['SETTINGS']['PHYSICS']['IErMatchMax']
ncount=0
normTerr=1.
tol=1.e-2
while ncount<iErMatch .and .normTerr>tol:
    root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh']=OMFITgaCode('/home/users/xiangjian/OMFIT-source/modules/MyInte/MyInte/INPUTS/TGYROInput/subjob/monitePBStgyro.sh_p12_no_alphaE')
    root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()
    root['OUTPUTS']['TGYROOutput']['']
    # get the calculated omega
    p_tgyro=root['SETTINGS']['PLOTS']['p_tgyro']
    profile=root['OUTPUTS']['TGYROOutput']['out.tgyro.profile']['data']
    Ti_old=profile[3]
    profile=map(list,zip(*profile))
    geometry=root['OUTPUTS']['TGYROOutput']['out.tgyro.geometry.1']['data']
    geometry=map(list,zip(*geometry))
    gyrobohm=root['OUTPUTS']['TGYROOutput']['out.tgyro.gyrobohm']['data']
    gyrobohm=map(list,zip(*gyrobohm))
    geometry1=root['OUTPUTS']['TGYROOutput']['out.tgyro.geometry.1']['data']
    geometry1=map(list,zip(*geometry1))
    Mach=array(profile[8])
    rho=geometry[1]
    # rotation date
    gcs=gyrobohm[5][0:p_tgyro+1];    #get the cs data
    gcs=[float(x) for x in gcs]
    rmaj=array([x*1.6 for x in geometry1[9]]);
    w0_t=Mach*gcs/rmaj;
    # interp the w0 calculated by TGYRO 
    rho_pivot=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RMAX']
    rho_t=linspace(0,rho_pivot,p_tgyro+1)
    nj=root['SETTINGS']['PHYSICS']['nj']
    r_12=linspace(0,1,nj)
    rho_12=linspace(0,1,nj)
    np=floor(rho_pivot*(nj-1))
    omega_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
    omega_new=ones(nj)
    omega_new[0:np-1]=spline(rho_t,w0_t,r_12[0:np-1])
    omega_new[np-1:nj]=omega_old[np-1:nj]
    root['INPUTS']['TGYROInput']['input.profiles']['omega0']=omega_new
    root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh']=OMFITgaCode('/home/users/xiangjian/OMFIT-source/modules/MyInte/MyInte/INPUTS/TGYROInput/subjob/monitePBStgyro.sh_p12')
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
    root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()
    profile=root['OUTPUTS']['TGYROOutput']['out.tgyro.profile']['data']
    Ti_new=profile[3]
    normTerr=norm(abs(Ti_new-Ti_old)/Ti_new)
    ncount=ncount+1
root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
