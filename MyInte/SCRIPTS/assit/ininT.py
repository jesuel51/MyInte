# this script is used to initial the n&T profile in the inone based on the profile in DEPENDENCIES
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['TIIN']=root['SETTINGS']['DEPENDENCIES']['te_tmplt']
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['TEIN']=root['SETTINGS']['DEPENDENCIES']['te_tmplt']
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']=root['SETTINGS']['DEPENDENCIES']['ne_tmplt']
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['enp(1,1)']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']*0.35
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['enp(1,2)']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']*0.35
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['eni(1,1)']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']*0.1
root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['eni(1,2)']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']*0.015
root['INPUTS']['ONETWOInput']['inone'].deploy('/home/users/xiangjian/OMFIT-source/modules/MyInte/MyInte/INPUTS/ONETWOInput/inone_201')
root['INPUTS']['ONETWOInput']['inone']=OMFITnamelist('/home/users/xiangjian/OMFIT-source/modules/MyInte/MyInte/INPUTS/ONETWOInput/inone_201')

