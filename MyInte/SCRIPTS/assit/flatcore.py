import scipy.interpolate as itp
pvt_e=root['SETTINGS']['PHYSICS']['pvt_e'][1]
pvt_i=root['SETTINGS']['PHYSICS']['pvt_i'][1]
slope_e=root['SETTINGS']['PHYSICS']['pvt_e'][2]
slope_i=root['SETTINGS']['PHYSICS']['pvt_i'][2]
#rho=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['rtiin(1,1)']
#Te_pre=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN(1,1)']
#Ti_pre=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN(1,1)']
#rho=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['rtiin']
nj=root['SETTINGS']['PHYSICS']['nj']
rho=linspace(0,1,nj)
Te_pre=root['INPUTS']['ONETWOInput']['inone']['namelis1']['TEIN']
Ti_pre=root['INPUTS']['ONETWOInput']['inone']['namelis1']['TIIN']
Te_pvt=interp(pvt_e,rho,Te_pre)
Ti_pvt=interp(pvt_i,rho,Ti_pre)
drho=rho[1]-rho[0]
num_e=int(pvt_e/drho)
num_i=int(pvt_i/drho)
num1=3
num2=6
if root['SETTINGS']['PHYSICS']['pvt_e'][0]==1:
    for k in linspace(0,num_e,num_e+1):
        Te_pre[k]=(pvt_e-k*drho)*abs(slope_e)+Te_pvt
	Te4pvt=array(list(Te_pre[num_e-num2:num_e-num1])+list(Te_pre[num_e+num1:num_e+num2]))
	rhoe4pvt=array(list(rho[num_e-num2:num_e-num1])+list(rho[num_e+num1:num_e+num2]))
	rhoepvt=rho[num_e-num1+1:num_e+num1-1];
	Te_pre[num_e-num1+1:num_e+num1-1]=itp.spline(rhoe4pvt,Te4pvt,rhoepvt);
	root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN(1,1)']=Te_pre
	root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TEIN(1,1)']=Te_pre
if root['SETTINGS']['PHYSICS']['pvt_i'][0]==1:
    for k in linspace(0,num_i,num_i+1):
        Ti_pre[k]=(pvt_i-k*drho)*abs(slope_i)+Ti_pvt
	Ti4pvt=array(list(Ti_pre[num_i-num2:num_i-num1])+list(Ti_pre[num_i+num1:num_i+num2]))
	rhoi4pvt=array(list(rho[num_i-num2:num_i-num1])+list(rho[num_i+num1:num_i+num2]))
	rhoipvt=rho[num_i-num1+1:num_i+num1-1];
	Ti_pre[num_i-num1+1:num_i+num1-1]=itp.spline(rhoi4pvt,Ti4pvt,rhoipvt);
	root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN(1,1)']=Ti_pre
	root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TIIN(1,1)']=Ti_pre


