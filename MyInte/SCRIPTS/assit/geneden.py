# this script is used to generate the density profile for all species
# note that theta_ne[1]>theta[0] is required and both must be in the range [0,pi]
n_ped=root['SETTINGS']['PHYSICS']['n_ped']
theta=root['SETTINGS']['PHYSICS']['theta_ne']
ne_avg_dsr=root['SETTINGS']['PHYSICS']['ne_avg_dsr'];	# desired averaged density
nj=root['SETTINGS']['PHYSICS']['nj']
ne_tmplt=root['SETTINGS']['DEPENDENCIES']['ne_tmplt']
nj_tmplt=len(ne_tmplt)
#te_tmplt=root['SETTINGS']['DEPENDENCIES']['te_tmplt']
#rho51=linspace(0,1,51)
#rho201=linspace(0,1,201)
#ne_tmplt51=interp(rho51,rho201,ne_tmplt)
#rho_ped=0.96
rho_ped=root['SETTINGS']['PHYSICS']['rho_ped']
#theta=[item * pi for item in theta]
theta=theta*pi;
#ne_51=linspace(1,1,51);
ne=linspace(1,1,nj_tmplt);
#ne[-3:]=linspace(n_ped,1,3);	# here we assume pedestal width to be 4%, which is resonlable
#nn_51=floor(rho_ped*50)
#nn_201=floor(rho_ped*200)
nn=floor(rho_ped*(nj_tmplt-1))
#ne[-1]=1.;	# here we assume pedestal width to be 4%, which is resonlable
#ne[-2]=n_ped*1./6.+ne[-1]*5./6.;
#ne[-3]=n_ped*5./6.+ne[-1]*1./6.;
#ne_51[nn_51:51]=ne_tmplt51[nn_51:51]/1.e13
#ne_201[nn_201:201]=ne_tmplt201[nn_201:201]/1.e13
fct=n_ped/ne_tmplt[nn]*1.e13
ne[nn:nj_tmplt]=fct*ne_tmplt[nn:nj_tmplt]/1.e13
A=ne_avg_dsr/rho_ped-n_ped;
#A=A/((sin(theta[1])-sin(theta[0]))/(theta[1]-theta[0])-cos(theta[1]));
#A=A/(tanh(theta[1]-log(cosh(theta[1])-cosh(theta[0]))/(theta[1]-theta[0])));
A=A/(tanh(theta[1])-(log(cosh(theta[1]))-log(cosh(theta[0])))/(theta[1]-theta[0]));
w=(theta[1]-theta[0])/rho_ped;
#rho_51=linspace(0,1,51);
#rho_201=linspace(0,1,201);
rho_tmplt=linspace(0,1,nj_tmplt);
#ne[0:49]=n_ped+A*cos(w*rho[0:49]+theta[0])-A*cos(theta[1])
#ne_51[0:nn_51]=n_ped-A*tanh(w*rho_51[0:nn_51]+theta[0])+A*tanh(theta[1])
#ne_201[0:nn_201]=n_ped-A*tanh(w*rho_201[0:nn_201]+theta[0])+A*tanh(theta[1])
ne[0:nn]=n_ped-A*tanh(w*rho_tmplt[0:nn]+theta[0])+A*tanh(theta[1])
rho=linspace(0,1,nj)
#ne=interp(rho_tmplt,ne_tmplt,rho)
ne=spline(rho_tmplt,ne,rho)
ne=ne*1e13;
# distribute for all species
#frac=array([0.35,0.35,0.1,0.015])
frac=root['SETTINGS']['PHYSICS']['DenFrac']
np1=ne*frac[0]
np2=ne*frac[1]
ni1=ne*frac[2]
ni2=ne*frac[3]
version=root['SETTINGS']['PHYSICS']['version']
# store in the tree
root['SETTINGS']['PHYSICS']['np1']=np1
root['SETTINGS']['PHYSICS']['np2']=np2
root['SETTINGS']['PHYSICS']['ni1']=ni1
root['SETTINGS']['PHYSICS']['ni2']=ni2
root['SETTINGS']['PHYSICS']['ne']=ne
if version==4:
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['enp(1,1)']=np1
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['enp(1,2)']=np2
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['eni(1,1)']=ni1
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['eni(1,2)']=ni2
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['ENEIN']=ne
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['enp(1,1)']=np1
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['enp(1,2)']=np2
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['eni(1,1)']=ni1
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['eni(1,2)']=ni2
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['ENEIN']=ne
elif version==57:
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['enp(1,1)']=np1
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['enp(1,2)']=np2
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['eni(1,1)']=ni1
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['eni(1,2)']=ni2
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['ENEIN']=ne
else:
    print('Error, the 12 version should be a correct value!')
