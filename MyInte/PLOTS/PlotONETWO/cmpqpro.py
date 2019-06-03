# this script is used to compare the q profile of the ONETWO output and the input.profiles which is used for turbulence transport evaluation.
# get the q profile of ONETWO output (efit gfile)
k=root['SETTINGS']['PLOTS']['iview']
gdata=root['OUTPUTSRec']['EFITOutput']['Out'][int(k)]['gfile']
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
for m in linspace(numgrid-2,0,numgrid-1): #numgrid-1:-1:1
    Pres[m]=Pres[m+1]+pppsi[m]*dpsi;
for m in linspace(0,numgrid-2,numgrid-1):
    rhot[m+1]=rhot[m]+q[m]/float(numgrid-1)
rhot=sqrt(rhot/max(rhot))
# get q profile of input.profiles
inputpro=root['INPUTSRec']['TGYRO'][int(k)]['input.profiles']
rho=inputpro['rho']
qinputpro=[abs(item) for item in inputpro['q']]
# get the q profile of the AUG hybrid shot
inputpro_hybrid=root['INPUTS']['TGYROInput']['input.profiles_hybrid']
q_hybrid=[abs(item) for item in inputpro_hybrid['q']]
# plot
figure('current profile',figsize=[8,8])
fs1=24
fs2=20
lw=4
plot(rhot,qpsi,'--b',linewidth=lw,label='efit')
plot(rho,q_hybrid,'--m',linewidth=lw,label='aug_hybrid')
plot(rho,qinputpro,'--k',linewidth=lw,label='tgyro')
plot(array([0,1]),array([1,1]),'--r',linewidth=lw/2.)
plot(array([0,1]),array([1.5,1.5]),'--r',linewidth=lw/2.)
text(0.6,0.6,'q=1',fontsize=fs2-4,family='serif')
text(0.6,1.6,'q=1.5',fontsize=fs2-4,family='serif')
legend(loc=0,fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
xlabel('$\\rho$',fontsize=fs2,family='serif')
ylabel('q',fontsize=fs2,family='serif')
ylim([0,9])
