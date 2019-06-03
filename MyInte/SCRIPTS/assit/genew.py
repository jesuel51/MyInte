# this script is used to generate a typical rotation profile
# x denote the radial coordinate, here we shall use w=w(1-x^2)^v; v dontes the peaking factor
w0=root['SETTINGS']['PHYSICS']['w0']
pf_w=root['SETTINGS']['PHYSICS']['pf_w']
nj=root['SETTINGS']['PHYSICS']['nj']
rho=linspace(0,1,nj);
w=w0*(1-rho**2)**pf_w
#root['OUTPUTS']['ProfileGenOutput']['input.profiles']['omega0']=w*1.e3
root['SETTINGS']['PHYSICS']['omega0']=w*1.e3
