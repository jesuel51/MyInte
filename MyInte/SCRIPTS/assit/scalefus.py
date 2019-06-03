# this script is used to scale the fusion power calculated from ONETWO to TGYRO, since the fusion power maybe unreasonable since the D&T fraction maybe not correct
# first we define a function to get the fraction of the fuel ions
def getdenfrac(fordenfrac):
    # we assumes that the ions are D&T, frist impurity, Second impurity. The concentration of the 1st impurity(normally helium or W) is specified by user. 
    # the format of ForDenFrac should be [F_imp1, Zeff, Z1, Z2]. Where F_imp is the concentration of the 1st impurity, Z1 and Z2 are the charge number of the 1st and 2nd impurity ions;
    b=fordenfrac[0]
    Zeff=fordenfrac[1]
    Z1=fordenfrac[2]
    Z2=fordenfrac[3]
    # the a, b,c represent the fraction of DT, 1st impurity and 2nd Impurity ,respectively
    #a=(Z2-Zeff+2*b)/2./(Z2-1)-b
    a=(Z2-Zeff+Z1*b)/2./(Z2-1)-b
    #c=(Zeff-1-2.*b)/(Z2**2-Z2)
    c=(Zeff-1-Z1*b)/(Z2**2-Z2)
    DenFrac=array([a,a,b,c])
    return DenFrac

# calculate the fueling ions concentration of case DT, He, Ar 
Fimp_He=root['SETTINGS']['PHYSICS']['ForDenFrac'][0]
Zeff=root['SETTINGS']['PHYSICS']['ForDenFrac'][1]
Z2=root['SETTINGS']['PHYSICS']['ForDenFrac'][2]
DenFrac1=getdenfrac(array([Fimp_He,Zeff,2,Z2]))
# calculate the fueling ions conctration of case DT, W, Ar
ene=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['ENEIN']
n_w=root['SETTINGS']['DEPENDENCIES']['W']
Fimp_W=(sum(n_w)/len(n_w))/(sum(ene)/len(ene))
DenFrac2=getdenfrac(array([Fimp_W,Zeff,74,Z2]))

# 
scalefrac=DenFrac1[0]/DenFrac2[0]
scalefrac=scalefrac**2
# scale the fusion power
inputpro=root['INPUTS']['TGYROInput']['input.profiles']
pow_e_fus=inputpro['pow_e_fus']
pow_i_fus=inputpro['pow_i_fus']
pow_e_fus_diff=pow_e_fus*(1-scalefrac)
pow_i_fus_diff=pow_i_fus*(1-scalefrac)
# update the pow_fus and pow in the input.profiles
inputpro['pow_e_fus']=scalefrac*inputpro['pow_e_fus']
inputpro['pow_i_fus']=scalefrac*inputpro['pow_i_fus']
inputpro['pow_e']=inputpro['pow_e']-pow_e_fus_diff
inputpro['pow_i']=inputpro['pow_i']-pow_i_fus_diff

