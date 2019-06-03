# this file is used to watch the q evolved in each iteration
#ncyclemax=root['SETTINGS']['PHYSICS']['ncyclemax'];
#qtmp=root['OUTPUTSRec']['ONETWOOutput'][0]['q']['data'];
#dim_n3d=size(qtmp,0);
#dim_nj=size(qtmp,1);
#qrec=ones((ncyclemax,dim_nj));	# record the q evolution
#qrecini=ones((ncyclemax,dim_nj));	# record the q evolution
#rho=linspace(0,1,dim_nj);
#plt.close()
#figure;
#shape=['-*','-o','--']
#color=['k','b','g']
#ms=len(shape)
#mc=len(color);
#figure
#subplot(1,2,1)
#for k in linspace(0,ncyclemax-1,ncyclemax):
#    q_all=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['q']['data'];
#    qrecini[k]=q_all[0];
#    plot(rho,qrecini[k],shape[int(k/mc)]+color[int(k%mc)],label=str(k))
#    title('initial q')
#    legend(loc=0).draggable(True)
#subplot(1,2,2)
#for k in linspace(0,ncyclemax-1,ncyclemax):
#    q_all=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['q']['data'];
#    qrec[k]=q_all[dim_n3d-1];
#    plot(rho,qrec[k],shape[int(k/mc)]+color[int(k%mc)],label=str(k))
#    title('final q')
#    legend(loc=0).draggable(True)
# the q profile evolution is from the trpltout.nc in ONETWO, as we know, the q profile in trpltout.nc is not correct since its psi is wrong
# thus we shall record the q profile evolution from the EFIT
ncyclemax=root['SETTINGS']['PHYSICS']['ncyclemax'];
#ncyclemax=1;
qtmp=root['INPUTS']['ONETWOInput']['gfile']['QPSI']
#dim_n3d=size(qtmp,0);
dim_nj=size(qtmp,0);
qrec=ones((ncyclemax+1,dim_nj));	# record the q evolution
rho=linspace(0,1,dim_nj);
plt.close()
figure;
shape=['-*','-o','--']
color=['k','b','g']
ms=len(shape)
mc=len(color);
figure
subplot(1,2,1)
qrec[0]=root['OUTPUTSRec']['EFITOutput']['In'][0]['QPSI']
plot(rho,qrec[0],shape[int(0/mc)]+color[int(0%mc)],label=str(0))
for k in linspace(1,ncyclemax,ncyclemax):
    qrec[k]=root['OUTPUTSRec']['EFITOutput']['Out'][int(k-1)]['QPSI']
    plot(rho,qrec[k],shape[int(k/mc)]+color[int(k%mc)],label=str(k))
    title('q Evolution')
    legend(loc=0).draggable(True)
