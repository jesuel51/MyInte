# this script is used to generate the ECCD core density and also the ECH power density
# The basic principle can be refered to a document
delta_loc=root['SETTINGS']['PHYSICS']['delta_loc']
gamma_loc=root['SETTINGS']['PHYSICS']['gamma_loc']
rho=root['INPUTS']['ONETWOInput']['inone']['NAMELIS2']['extcurrf_rho']
num=len(rho)
Flag=linspace(0,0,num);
Flag[0:int(delta_loc*num)+1]=1.
J_loc=gamma_loc*cos(pi/2.*rho/delta_loc)**2*Flag;
root['INPUTS']['ONETWOInput']['inone']['NAMELIS2']['extcurrf_curr']=J_loc
# the profile of the power is same to the current, a factor of the current density against the power can be set, it's 200 by default, twice to the efficiency at rho~0.5, but the CD efficiency should be higher in the core region
ECeffFct=root['SETTINGS']['PHYSICS']['ECeffFct']
q_loc=J_loc/ECeffFct
root['INPUTS']['ONETWOInput']['inone']['NAMELIS2']['extqerf_qe']=q_loc
# there is another option
#ecnoreff=root['SETTINGS']['PHYSICS']['ecnoreff']   # normalized efficiency, power|current flag, total power|current
