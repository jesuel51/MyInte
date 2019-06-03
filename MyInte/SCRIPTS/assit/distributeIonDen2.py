# this scripts is used to update the ion density 
# in ONETWO, when Helium profile is updated, adjust the DT profile to keep quasi-neutrality
# also, there is another option to use Ar to replace the W contribution on the Zeff
# there are 2 options here, one is to the one discribed above
# the other one is that the ions species shares the electron density profile shape
# the options are determined by the root['SETTINGS']['PHYSICS']['idistributeion'], default 0
idistributeion=root['SETTINGS']['PHYSICS']['idistributeion']
namelis1=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']
ne=namelis1['ENEIN']
if idistributeion == 1:
    Zw=63
    Zar=18
    if root['SETTINGS']['PHYSICS']['reconsImp']!='':
        nw=root['SETTINGS']['DEPENDENCIES']['W']
    else:
        nw=zeros([len(namelis1['ENEIN'])])
    nhe=root['SETTINGS']['DEPENDENCIES']['He']
    namelis1['eni'].T[0]=nhe
    if root['SETTINGS']['PHYSICS']['iArRepW']==1:   # use the Ar to replace the W's contribution to Zeff
        fw=nw/ne
        Zeff_w=fw*Zw**2
        f_ar_add=Zeff_w/Zar**2
        # recode the Ar profile so that Ar profile can be recoved in the input.profiles
        namelis1['eni'].T[1]=root['SETTINGS']['TEMP']['n_ar']*1.e13
        namelis1['eni'].T[1]=namelis1['eni'].T[1]+f_ar_add*ne
    ndt=ne-Zar*namelis1['eni'].T[1]-2*namelis1['eni'].T[0]
    namelis1['enp'].T[0]=ndt/2.
    namelis1['enp'].T[1]=ndt/2.
else:
    # prepare the ion fractions 
    root['SCRIPTS']['assit']['denfrac.py'].run()
    DenFrac=root['SETTINGS']['PHYSICS']['DenFrac']
    namelis1['enp'].T[0]=ne*DenFrac[0]
    namelis1['enp'].T[1]=ne*DenFrac[1]
    namelis1['eni'].T[0]=ne*DenFrac[2]
    namelis1['eni'].T[1]=ne*DenFrac[3]
