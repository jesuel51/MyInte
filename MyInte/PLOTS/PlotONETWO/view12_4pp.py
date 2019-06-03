# this script is used to plot the onetwo profile for paper while required less subplot
k=root['SETTINGS']['PLOTS']['iview']
iEr=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']
iNe=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']
fulldir=root['SETTINGS']['PLOTS']['dirpre']+root['SETTINGS']['PLOTS']['workdir']
fs1=12
fs2=16
fs3=20
plt.close()
plt.figure(311,figsize=[7.5,8])
# get the pressure and q profile from EFIT output gfile
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
# get the current density for all components
curden=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curden']['data'];
curohm=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curohm']['data'];
curni=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curni']['data'];
curboot=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curboot']['data'];
currf=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['currf']['data'];
curbeam=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curbeam']['data'];
paux=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['paux']['data'];
qdt=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['qdt']['data'];
etor=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['etor']['data'];
dim_n3d=size(curbeam,0);
dim_nj=size(curbeam,1);
rho=linspace(0,1,dim_nj);
#   distribution of each current component
#h1=subplot(2,2,1)
#rct1=[0.15,0.5,0.28,0.25]
rct1=[0.15,0.54,0.32,0.36]
#rct1=[0.15,0.5,0.28,0.25]
ax1=plt.axes(rct1)
#get(h1.frame_on)
# get the geometry information from EFIT output
GridR,GridZ=meshgrid(gdata['AuxQuantities']['R'],gdata['AuxQuantities']['Z'])
PsiGrid=gdata['PSIRZ']
ax1.contourf(GridR,GridZ,PsiGrid,36,levels=linspace(gdata['SIMAG'],gdata['SIBRY'],16))
#contourf(GridR,GridZ,PsiGrid,36,levels=linspace(gdata['SIMAG'],gdata['SIBRY'],16))
axis('equal')
ylim([-4.5,4.5])
xlim(4,9)
text(8,2.5,'(a)',fontsize=fs3)
plot(gdata['RBBBS'],gdata['ZBBBS'],'-r',linewidth=1.6)
plot(gdata['RLIM'],gdata['ZLIM'],linewidth=3.6)
xlabel('R',fontsize=fs2,family='serif')
ylabel('Z',fontsize=fs2,family='serif')
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
subplot(2,2,3)
currff=curden-curohm-curboot-curbeam
plot(rho,curden[dim_n3d-1]/100,'-m',label='tot',linewidth=2)
plot(rho,curohm[dim_n3d-1]/100,'-r',label='ohmic',linewidth=2)
plot(rho,curboot[dim_n3d-1]/100,'-y',label='BS',linewidth=2)
#plot(rho,currf[dim_n3d-1]/100,'-k',label='rf',linewidth=2)
plot(rho,currff[dim_n3d-1]/100,'-k',label='rf',linewidth=2)
plot(rho,curbeam[dim_n3d-1]/100,'-g',label='beam',linewidth=2)
legend(loc=0,fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
#xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('$Jt(MA.m^{-2})$',fontsize=fs2,family='serif')
text(0.2,1.6,'(c)',fontsize=fs3)
ylim([0,2])
#subplot(2,2,3)
#totohm=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totohm']['data'];
#totboot=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totboot']['data'];
#totb=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totb']['data'];
#totrf=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totrf']['data'];
#dim_time=len(totb);
#text(-0.8,1.00,'(c)',fontsize=fs3)
#curr=array([totboot[dim_time-1],totohm[dim_time-1],totb[dim_time-1],totrf[dim_time-1]]);
# get the Ip from the rfile of EFIT
#Ip=root['INPUTS']['EFITInput']['rtest']['IN1']['PLASMA']
#frac=[int(round(item)) for item in (curr/Ip*100.)]
#label=['BS '+str(frac[0]),'ohm '+str(frac[1]),'beam '+str(frac[2]),'rf '+str(frac[3])]
#label=['BS '+str(frac[1]),'beam '+str(frac[2]),'rf '+str(frac[3])]
#pie([totboot[dim_time-1],totohm[dim_time-1],totb[dim_time-1],totrf[dim_time-1]],explode=[0,0,0,0],labels=label)#,fontsize=fs1)
# safety factor q profile
#subplot(3,2,4)
subplot(2,2,2)
plot(rhot,qpsi,linewidth=2)
ylim([2,9])
xticks(fontsize=fs1,family='serif')
yticks(linspace(2,9,8),fontsize=fs1,family='serif')
xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('q',fontsize=fs2,family='serif')
text(0.2,7,'(b)',fontsize=fs3)
#toroidal electrical field
#subplot(3,2,5)
#plot(linspace(0,1,dim_nj),etor[dim_n3d-1])
#xticks(fontsize=fs1,family='serif')
#yticks(fontsize=fs1,family='serif')
#ylim([-1.e-6,1.e-6])
#xlabel('$rho$',fontsize=fs2,family='serif')
#ylabel('$E_{tor}(V.cm^{-1})$',fontsize=fs2,family='serif')
#text(0.2,0.5e-6,'(e)',fontsize=fs3)
# pressure profile
#subplot(3,2,6)
subplot(2,2,4)
plot(rhot,Pres,linewidth=2)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
xlabel('$rho$',fontsize=fs2,family='serif')
plot([0.64,0.64],[1.e5,6.e5],'-k',linewidth=3)
text(0.52,6.5e5,'$\\rho_{q-min}$',fontsize=fs1+8,family='serif')
ylim([0,8.e5])
text(0.8,6.e5,'(d)',fontsize=fs3)
ylabel('P(pa)',fontsize=fs2,family='serif')
#   central ohmic current evolution
#subplot(2,2,4)
#plot(rho,curohm[dim_n3d-1]/100,'-bo')
#xticks(fontsize=fs1,family='serif')
#yticks(fontsize=fs1,family='serif')
#xlabel('$rho$',fontsize=fs2,family='serif')
#ylabel('J-ohmic MA/m^2',fontsize=fs2,family='serif')
#figure('current profile')
iextra=0
if iextra==1:
    plt.figure('current profile',figsize=[9,7])
    subplot(1,2,1)
    currff=curden-curohm-curboot-curbeam
    lw=4
    fsadd=6
    plot(rho,curden[dim_n3d-1]/100,'-m',label='tot',linewidth=lw)
    plot(rho,curohm[dim_n3d-1]/100,'-r',label='ohmic',linewidth=lw)
    plot(rho,curboot[dim_n3d-1]/100,'-y',label='BS',linewidth=lw)
    #plot(rho,currf[dim_n3d-1]/100,'-k',label='rf',linewidth=2)
    plot(rho,currff[dim_n3d-1]/100,'-k',label='rf',linewidth=lw)
    plot(rho,curbeam[dim_n3d-1]/100,'-g',label='beam',linewidth=lw)
    legend(loc=0,fontsize=fs1+fsadd).draggable(True)
    xticks(fontsize=fs1+fsadd,family='serif')
    yticks(fontsize=fs1+fsadd,family='serif')
    #xlabel('$rho$',fontsize=fs2,family='serif')
    ylabel('$Jt(MA.m^{-2})$',fontsize=fs2+fsadd,family='serif')
    xlabel('$rho$',fontsize=fs2+fsadd,family='serif')
    #text(0.2,1.6,'(b)',fontsize=fs3+fsadd)
    ylim([0,2])
    subplot(1,2,2)
    plot(rhot,qpsi,linewidth=lw)
    ylim([2,9])
    xticks(fontsize=fs1+fsadd,family='serif')
    yticks(linspace(2,9,8),fontsize=fs1+fsadd,family='serif')
    #xlabel('$rho$',fontsize=fs2,family='serif')
    #ylabel('q',fontsize=fs2,family='serif')
    title('$q$',fontsize=fs2+fsadd,family='serif')
    xlabel('$rho$',fontsize=fs2+fsadd,family='serif')
