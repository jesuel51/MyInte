# this scripts is used to distribute the density of ion species according to the density of electrons
# this script is used in 2 place; 
#(1) distribute the ion density in inone, the density profile W should be provided;
#(2) distribute the ion density in input.profiles; the density profile of Helium should be provided;
# normally, some ions density profiles shape maybe different from electrons, in this way, we need to distribute the ions density for every grid point
# This script is controlled by ImpName=root['SETTINGS']['TEMP']['ImpName']; 
# if ImpName='He', then this script needs runs for input.profiles, if ImpName='W', then this script runs for inone
# the parameter required here is from root['SETTINGS']['PHYSICS']['ForDenFrac'], including Zeff and the Z2
# first let's define a function which can be used to get the fraction of each ions according to a given zeff and fixing one ion species concentration
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
# the density profile of the 1st impurity need to be specified, and is specified in the root['SETTINGS']['DEPENDENCIES']=depend
# depend['He'] is the density of Helium, depend['W'] is the density of tungsten
ImpName=root['SETTINGS']['TEMP']['ImpName']
depend=root['SETTINGS']['DEPENDENCIES']
Z2=root['SETTINGS']['PHYSICS']['ForDenFrac'][2]
Zeff=root['SETTINGS']['PHYSICS']['ForDenFrac'][1]
if ImpName=='W':
    Z1=74
    namelis1=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']
    ene=namelis1['ENEIN']
    n_imp1=depend[ImpName]
    F_imp1=n_imp1/ene
    namelis1['NAMEI'][0]='w'
    num_ene=len(ene)
    if not namelis1.has_key('enp(1,1)'):
        namelis1['enp(1,1)']=zeros(num_ene)
    if not namelis1.has_key('enp(1,2)'):
        namelis1['enp(1,2)']=zeros(num_ene)
    if not namelis1.has_key('eni(1,1)'):
        namelis1['eni(1,1)']=zeros(num_ene)
    if not namelis1.has_key('eni(1,2)'):
        namelis1['eni(1,2)']=zeros(num_ene)
    for k in range(0,num_ene):
        ForDenFrac=array([F_imp1[k],Zeff,Z1,Z2])
        DenFrac=getdenfrac(ForDenFrac)
        namelis1['enp(1,1)'][k]=ene[k]*DenFrac[0]
        namelis1['enp(1,2)'][k]=ene[k]*DenFrac[1]
        namelis1['eni(1,1)'][k]=ene[k]*DenFrac[2]
        namelis1['eni(1,2)'][k]=ene[k]*DenFrac[3]
elif ImpName=='He':
# we note here that normally the merge script will appear in the flowmanager script after this one
    Z1=2
    TGYROInput=root['INPUTS']['TGYROInput']
    TGYROInput['input.tgyro']['LOC_Z3']=2
    TGYROInput['input.tgyro']['LOC_MA3']=4
    ene=TGYROInput['input.profiles']['ne']
    n_imp1=depend[ImpName]
    F_imp1=n_imp1/ene
    num_ene=len(ene)
    for k in range(0,num_ene):
        ForDenFrac=array([F_imp1[k],Zeff,Z1,Z2])
        DenFrac=getdenfrac(ForDenFrac)
        TGYROInput['input.profiles']['ni_1']=ene*DenFrac[0]
        TGYROInput['input.profiles']['ni_2']=ene*DenFrac[1]
        TGYROInput['input.profiles']['ni_3']=ene*DenFrac[2]
        TGYROInput['input.profiles']['ni_4']=ene*DenFrac[3]
else:
    print('Only He and W is permitted!')
