# this script is used to display all the kinds of pressure profile; and compare them to that of EFIT g-file;
# all the data are get from statefile;
#plt.close()
#iview=root['SETTINGS']['PLOTS']['iview']
#        double press(dim_rho) ;
#                press:long_name = "*  total pressure on transport rho grid, nt/m^2" ;
#                press:units = "newton/meter^2" ;
#        double pressb(dim_rho) ;
#                pressb:long_name = "* beam  pressure on transport rho grid nt/m^2" ;
#                pressb:units = "newton/meter^2" ;

#        double ene(dim_rho) ;
#                ene:long_name = "*  electron density, #/meter^3" ;
#                ene:units = "1/meter^3" ;
#        double enion(dim_ion, dim_rho) ;
#                enion:long_name = "* thermal ion densities, species: d t he o" ;
#                enion:units = "1/meter^3" ;

#        double Te(dim_rho) ;
#                Te:long_name = "*  electron temperature, keV" ;
#                Te:units = "keV" ;
#        double Ti(dim_rho) ;
#                Ti:long_name = "*  ion temperature, keV" ;
#                Ti:units = "keV" ;

#        double wbeam(dim_rho) ;
#                wbeam:long_name = "* fast ion stored energy density KEV/m**3" ;
#                wbeam:units = "keV/meter^3" ;
#        double walp(dim_rho) ;
#                walp:long_name = "* fast alpha stored energy density KEV/m**3" ;
#                walp:units = "keV/meter^3" ;
#        double enalp(dim_rho) ;
#                enalp:long_name = "* fast alpha density 1/m**3" ;
#                enalp:units = "1/meter^3" ;
#        double enbeam(dim_fi, dim_rho) ;dim_fi=1 here
#                enbeam:long_name = "*  fast ion density, #/meter^3, species: d" ;
#                enbeam:units = "#/(meter^3)" ;
####################################################################################
#iview=root['SETTINGS']['PLOTS']['iview']
#stateroot=root['OUTPUTSRec']['ONETWOOutput'][iview]['statefile']
stateroot=root['OUTPUTS']['ONETWO']['statefile.nc']
press=stateroot['press']['data']
pressb=stateroot['pressb']['data']
ene=stateroot['ene']['data']
enion=stateroot['enion']['data']
Te=stateroot['Te']['data']
Ti=stateroot['Ti']['data']
wbeam=stateroot['wbeam']['data']
enbeam=stateroot['enbeam']['data']
walp=stateroot['walp']['data']
enalp=stateroot['enalp']['data']

dim_rho=len(press)
rho=linspace(0,1,dim_rho)
fct=1.602e-16; #keV/m^3->Fct* pa;
figure(1)
# density profile
subplot(2,2,1)
plot(rho,ene,'-ro',label='ne')
plot(rho,enion[0],'-b*',label='D')
plot(rho,enion[1],'-bd',label='T')
plot(rho,enion[2],'-k*',label='He')
plot(rho,enion[3],'-kd',label='o')
xlabel('rho')
ylabel('density-m^{-3}')
legend(loc=0).draggable(True)
subplot(2,2,2)
plot(rho,ene,'-ro',label='ne')
plot(rho,10*enbeam[0],'-b*',label='10*beam')
plot(rho,100*enalp,'-bo',label='100*enalp')
xlabel('rho')
ylabel('density-m{-3}')
legend(loc=0).draggable(True)
subplot(2,2,3)
plot(rho,enion[0]*Ti+enion[1]*Ti,'-b*',label='Main Ion')
plot(rho,enion[2]*Ti+enion[3]*Ti,'-bo',label='Imp')
plot(rho,ene*Te,'-bd',label='Electron')
plot(rho,2./3*wbeam,'-k*',label='Beam')
plot(rho,2./3*walp,'-ko',label='Alpha')
EnergyStore=(enion[0]+enion[1]+enion[2]+enion[3])*Ti+ene*Te+2./3*wbeam+2./3*walp
plot(rho,EnergyStore,'-ro',label='Sum')
xlabel('rho')
ylabel('Pressure keV/m*{-3}')
legend(loc=0).draggable(True)
subplot(2,2,4)
#PressSum=((enion[0]+enion[1]+enion[2]+enion[3])*Ti+ene*Te+wbeam*2./3+walp)*fct
# the factor 2/3 may comes from that only the perpendicular pressure are calculated
PressSum=((enion[0]+enion[1]+enion[2]+enion[3])*Ti+ene*Te+wbeam*2./3+2./3*walp)*fct
PressBeam=wbeam*2./3*fct
plot(rho,PressSum,'-ro',label='Total_Sum')
plot(rho,press,'-r*',label='Total_state')
plot(rho,PressBeam,'-bo',label='Beam')
plot(rho,pressb,'-b*',label='beam_state')
xlabel('rho')
ylabel('Pressure-pa')
legend(loc=0).draggable(True)
# compare whether we sum the right componenet
#figure(2)
#plot(rho,(PressSum-press)/press,'-ro',label='presssum')
#plot(rho,(PressBeam-pressb)/pressb,'-r*',label='pressbeam')
#xlabel('rho')
#ylabel('press')
#legend(loc=0).draggable(True)
# calculate the pressure fraction of beam and alpha over the total pressure 
figure(3)
subplot(1,2,1)
plot(rho,PressBeam/PressSum,'-r')
xlabel('rho')
ylabel('Beam pressure fraction')
subplot(1,2,2)
plot(rho,2./3*walp/EnergyStore,'-r')
xlabel('rho')
ylabel('alpha pressure fraction')

###########################################################
# next, we shall get the pressure profile from EFIT g-file
icmp=0
if icmp==1:
    gdata=root['OUTPUTSRec']['EFITOutput']['Out'][iview]['gfile']
    difab=gdata['SIMAG']-gdata['SIBRY']
    numgrid=len(gdata['QPSI'])
    qpsi=gdata['QPSI']
    rhop=linspace(0,1,numgrid)
    Pres=linspace(0,0,numgrid)
    rhot=linspace(0,0,numgrid)
    rhopres=(rhop[0:numgrid-1]+rhop[1:numgrid])/2;
    pppsi=spline(rhop,gdata['PPRIME'],rhopres)
    q=spline(rhop,gdata['QPSI'],rhopres)
    dpsi=difab/(numgrid-1);
    for k in linspace(numgrid-2,0,numgrid-1): #numgrid-1:-1:1
        Pres[k]=Pres[k+1]+pppsi[k]*dpsi;
    for k in linspace(0,numgrid-2,numgrid-1):
	rhot[k+1]=rhot[k]+q[k]/float(numgrid-1)
    rhot=sqrt(rhot/max(rhot))
    figure(4)
    subplot(1,2,1)
    plot(rhot,Pres,'-k*')
    xlabel('rho')
    ylabel('Pressure')
    subplot(1,2,2)
    plot(rhot,qpsi,'-k*')
    xlabel('rho')
    ylabel('q')
figure(5)
subplot(1,2,1)
plot(rhot,Pres,'-ro',label='EFIT g-file')
plot(rho,press,'-r*',label='ONETWO output')
xlabel('rho')
ylabel('Pressure-pa')
legend(loc=0).draggable(True)
subplot(1,2,2)
plot(rho,(enion[0]*Ti+enion[1]*Ti)*fct,'-b*',label='Main Ion')
plot(rho,(enion[2]*Ti+enion[3]*Ti)*fct,'-bo',label='Imp')
plot(rho,(ene*Te)*fct,'-bd',label='Electron')
plot(rho,(2./3*wbeam)*fct,'-k*',label='Beam')
plot(rho,(2./3*walp)*fct,'-ko',label='Alpha')
plot(rho,press,'-ro',label='Total')
xlabel('rho')
ylabel('Pressure-pa')
legend(loc=0).draggable(True)
# we are going to plot the beta_nb and beta_alpha
Bt=gdata['BCENTR']
TorMagPres=Bt**2*4*1.e5;
figure(6)
Pres_Beam=2./3*wbeam*fct
Pres_Alpha=2./3*walp*fct
plot(rho,Pres_Beam/TorMagPres,'-bo',label='Beam')
plot(rho,Pres_Alpha/TorMagPres,'-ro',label='Alpha')
xlabel('rho')
ylabel('Toroidal Beta')
legend(loc=0).draggable(True)
iwrite=1
if iwrite==1:
    fid=open('/scratch/xiangjian/phaseII.txt','w')
    for k in range(0,201):
        line=str(rho[k])+'    '+str(enion[2][k])+'    '+str(enalp[k])+'    '+str(Pres_Alpha[k])+'    '+str(Pres_Alpha[k]/TorMagPres)
        fid.write(line)
        fid.write('\n')
    fid.close()
