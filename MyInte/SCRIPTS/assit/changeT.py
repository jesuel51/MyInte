#this script is used to change the temperature profile
# since somethings we may change the density profile, for maintaining the fusion power, we shall adjust the temperature profile
# the fusion power is proportional to n^2, but BS current scales as n, so increase density profile is expected to change the total BS current while maintaining the fusion power;
# here we shall decrease the BS current, since the BS current now is reaching 60% with fusion power 40MW. besides, we need NB power to maintain the temperature profile outside the q_min;
num=46
factor=linspace(0.8,1,46);
T=root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN(1,1)']
for k in linspace(0,num-1,num):
    T[k]=T[k]*factor[k]
root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TIIN(1,1)']=T
root['INPUTS']['ONETWOInput']['inone_pre']['namelis1']['TEIN(1,1)']=T
root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TIIN(1,1)']=T
root['INPUTS']['ONETWOInput']['inone_ss']['namelis1']['TEIN(1,1)']=T
root['SETTINGS']['PHYSICS']['pvt_e']=array([ 1. ,  0.24,  3.6])
root['SETTINGS']['PHYSICS']['pvt_i']=array([ 1. ,  0.24,  3.6])
root['SCRIPTS']['assit']['flatcore.py'].run()
root['SETTINGS']['PHYSICS']['pvt_e']=array([ 1. ,  0.20,  3.6])
root['SETTINGS']['PHYSICS']['pvt_i']=array([ 1. ,  0.20,  3.6])
