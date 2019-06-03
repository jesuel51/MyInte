# this script is used to geTrate temperature profile , the profile geTrated is quite similar to density
# note that theta_T[1]>theta[0] is required and both must be in the range [0,pi]
T_ped=root['SETTINGS']['PHYSICS']['T_ped']
theta=root['SETTINGS']['PHYSICS']['theta_T']
T_avg_dsr=root['SETTINGS']['PHYSICS']['T_avg_dsr'];	# desired averaged density
rho_ped=root['SETTINGS']['PHYSICS']['rho_ped']
#theta=[item * pi for item in theta]
nj=root['SETTINGS']['PHYSICS']['nj']
te_tmplt=root['SETTINGS']['DEPENDENCIES']['te_tmplt']
nj_tmplt=len(te_tmplt)
#rho51=linspace(0,1,51)
#rho201=linspace(0,1,201)
rho=linspace(0,1,nj)
rho_tmplt=linspace(0,1,nj_tmplt)
#te_tmplt51=interp(rho51,rho201,te_tmplt)
#rho_ped=0.96
#theta=[item * pi for item in theta]
theta=theta*pi;
#te_51=linspace(1,1,51);
te=linspace(1,1,nj_tmplt);
#ne[-3:]=linspace(n_ped,1,3);	# here we assume pedestal width to be 4%, which is resonlable
#nn_51=floor(rho_ped*50)
#nn_201=floor(rho_ped*200)
nn=floor(rho_ped*(nj_tmplt-1))
#ne[-1]=1.;	# here we assume pedestal width to be 4%, which is resonlable
#ne[-2]=n_ped*1./6.+ne[-1]*5./6.;
#ne[-3]=n_ped*5./6.+ne[-1]*1./6.;
#te_51[nn_51:51]=ne_tmplt51[nn_51:51]/1.e13
#te_201[nn_201:201]=ne_tmplt201[nn_201:201]/1.e13
#te_201[nn_201:201]=ne_tmplt201[nn_201:201]/1.e13
fct=T_ped/te_tmplt[nn];
te[nn:nj_tmplt]=fct*te_tmplt[nn:nj_tmplt]
A=T_avg_dsr/rho_ped-T_ped;
#A=A/((sin(theta[1])-sin(theta[0]))/(theta[1]-theta[0])-cos(theta[1]));
#A=A/(tanh(theta[1]-log(cosh(theta[1])-cosh(theta[0]))/(theta[1]-theta[0])));
A=A/(tanh(theta[1])-(log(cosh(theta[1]))-log(cosh(theta[0])))/(theta[1]-theta[0]));
w=(theta[1]-theta[0])/rho_ped;
#rho_51=linspace(0,1,51);
#rho_201=linspace(0,1,201);
#ne[0:49]=n_ped+A*cos(w*rho[0:49]+theta[0])-A*cos(theta[1])
#te_51[0:nn_51]=n_ped-A*tanh(w*rho_51[0:nn_51]+theta[0])+A*tanh(theta[1])
#te_201[0:nn_201]=n_ped-A*tanh(w*rho_201[0:nn_201]+theta[0])+A*tanh(theta[1])
te[0:nn]=T_ped-A*tanh(w*rho_tmplt[0:nn]+theta[0])+A*tanh(theta[1])
rho_tmplt=linspace(0,1,nj_tmplt)
T=spline(rho_tmplt,te,rho)
# store in the tree
version=root['SETTINGS']['PHYSICS']['version']
if version==4:
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN']=T
    root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN']=T
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TIIN']=T
    root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TEIN']=T
elif version==57:
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['TIIN']=T
    root['INPUTS']['ONETWOInput']['inone']['namelis1']['TEIN']=T
else:
    print('Error, the 12 version should be a correct value!')
