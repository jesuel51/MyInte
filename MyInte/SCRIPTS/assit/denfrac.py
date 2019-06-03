# this script is used to calculate the density fraction for each species
# the input parameters are in the settingnamalist fordenfrac, which is compose of b, zeff, z, which means Helium fraction, z_effective and the charge number of impurity
fordenfrac=root['SETTINGS']['PHYSICS']['ForDenFrac']
b=fordenfrac[0]
Zeff=fordenfrac[1]
Z=fordenfrac[2]
# the a, b,c represent the fraction of DT, Helium and Impurity ,respectively
a=(Z-Zeff+2*b)/2./(Z-1)-b
c=(Zeff-1-2.*b)/(Z**2-Z)
DenFrac=array([a,a,b,c])
root['SETTINGS']['PHYSICS']['DenFrac']=DenFrac
