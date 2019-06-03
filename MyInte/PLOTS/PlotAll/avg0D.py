# Backgound: since sometimes the profile may vary in a small range, thus we shall average them to give a more accurate solution
iview=root['SETTINGS']['PLOTS']['iview']
ncmp=root['SETTINGS']['PLOTS']['ncmp']
root['SCRIPTS']['assit']['readGlobdat.py'].run()
numout=len(root['SETTINGS']['TEMP']['out'])
outarr=np.zeros([ncmp,numout])
outarrerr=np.zeros([ncmp,numout])
for kk in linspace(iview,iview+ncmp-1,ncmp):
    root['SETTINGS']['PLOTS']['iview']=kk
    root['SCRIPTS']['assit']['readGlobdat.py'].run()
    outarr[kk-iview]=root['SETTINGS']['TEMP']['out']
outavg=np.mean(outarr,0)
for kk in linspace(0,ncmp-1,ncmp):
    outarrerr[kk]=(outarr[kk]-outavg)/outavg
outerr=linspace(0,0,numout)
for kk in linspace(0,numout-1,numout):
    outerr[kk]=norm(outarrerr[0:ncmp,kk])/ncmp
    outerr[kk]=norm(outarrerr[0:ncmp,kk])/sqrt(float(ncmp))
outavg[0]='100000'
outname=array(['iview','Te0','Ti0','ne_avg','n_DT_avg','n_He_avg','n_Ar_avg','ne(0)','n_DT(0)','n_He(0)','n_Ar(0)','pf_ne','f_bs','P_H','P_ECH','P_NB','Q','Pfus','betaN','li','zeta-rf','gamma_rf','zeta-beam','gamma-beam','zeta_tot-notsure','gamma_tot','H98','tau_e','stored energy','Prad','Psep'])
for k in range(0,len(outavg)):
    print('%16s=%.2e %.2e'%(outname[k],outavg[k],outerr[k]))
root['SETTINGS']['PLOTS']['iview']=iview
