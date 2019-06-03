# this script is used to plot the eigenfrequency and growth rate for all the kyrho, the radius is specified by the root['SETTINGS']['PHYSICS']['ipltspectrum']
# note the stability analyis should be performed by TGLF before running this plot scrip
# first we should define a function to read the date of out.tglf.run, which contains the frequency and growth rate
#plt.close()
def readfile(filename):
    count=0
    w=zeros([2,2])
    f=open(filename,'Ur')
    for line in f:
        if line.find('(wr,wi)')!=-1:
            temp=line.split()
            w[count][0]=temp[1]
            w[count][1]=temp[2]
            count=count+1
    return w
# then read all the data
kyarr=root['SETTINGS']['SETUP']['kyarr']
num_ky=len(kyarr)
ptgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
w_1=zeros([ptgyro,num_ky])     # dominate mode frequency
w_2=zeros([ptgyro,num_ky])     # subdominate mode frequency
gamma_1=zeros([ptgyro,num_ky]) # dominate mode growth rate
gamma_2=zeros([ptgyro,num_ky]) # subdominate mode growth rate
ExBShear=zeros(ptgyro)         # ExB shearing rate, defined as a/cs*r/q*d(omega)/dr
Kappa=zeros(ptgyro)            # Elongation
# all the information about frequency and growth rate can be get
for k in range(1,ptgyro+1):
    count=0
    for item in kyarr:
        filename=root['OUTPUTS']['TGLFScan'][k]['lin'][str(item)[0:4]]['out.tglf.run'].filename
        w=readfile(filename)
        w_1[k-1][count]=w[0][0]
        w_2[k-1][count]=w[1][0]
        gamma_1[k-1][count]=w[0][1]
        gamma_2[k-1][count]=w[1][1]
        count=count+1
# all the ExB shearing information is get
for k in range(0,ptgyro):
    ExBShear[k]=abs(root['OUTPUTS']['TGLFScan'][k+1]['lin']['input.tglf']['VEXB_SHEAR'])
    Kappa[k]=abs(root['OUTPUTS']['TGLFScan'][k+1]['lin']['input.tglf']['KAPPA_LOC'])
ExBShear=ExBShear*0.3*sqrt(Kappa)
# based on the profiles we get, then all the linear information can be plotted
ipltspectrum=root['SETTINGS']['PLOTS']['ipltspectrum']
figure('micro-turbulence linear stability property',figsize=[12,9])
lab=['-kd','-ko','-k*','-md','-mo','-m*','-bd','-bo','-b*','-rd','-ro','-r*','-gd','go','-g*']
lw=2
fs1=20
fs2=16
fs3=24
pow_kyarr=1
ilogplt = 0# decide whether to use logrithm coordinate
ipltExB = 1
ipltgamnet = 1 # determine whether to plot the gammanet
subplot(221)
for k in ipltspectrum:
    ra=root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']
#    plot(kyarr,w_1[k],lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
    semilogx(kyarr,w_1[k-1]/kyarr**pow_kyarr,lab[k-1],linewidth=lw,label='rho='+str(int(100*ra)/100.))
legend(loc=1,fontsize=fs2).draggable(True)
#title('dominate mode frequency/ky^'+str(pow_kyarr),fontsize=fs1)
title('r/a='+str(int(ra*100)/100.),fontsize=fs1)
#xlim([0.1,30])
xlim([0.1,max(kyarr)])
xticks(fontsize=fs2)
yticks(fontsize=fs2)
subplot(223)
bdryky=5
indbdry=find(kyarr>bdryky)[0]+1
print('Seperatrix ky for lowk and highk is ',bdryky)
for k in ipltspectrum:
    ra=root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']
#    plot(kyarr,gamma_1[k-1],lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
#    loglog(kyarr,gamma_1[k-1]/kyarr,lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
    if ilogplt == 0:
#        semilogx(kyarr,gamma_1[k-1]/kyarr**pow_kyarr,lab[k-1],linewidth=lw,label='rho='+str(int(ra*100)/100.))
#        semilogx(kyarr,gamma_1[k-1]/kyarr**pow_kyarr,lab[7],linewidth=lw,label='gamma rho='+str(int(ra*100)/100.))
        semilogx(kyarr,gamma_1[k-1]/kyarr**pow_kyarr,lab[7],linewidth=lw,label='$\gamma/k_y$')
        if ipltExB==1:
            semilogx(kyarr,ExBShear[k-1]/kyarr**pow_kyarr,lab[8],linewidth=lw,label='$\gamma_{e-eff}$/$k_y$')
        if ipltgamnet == 1:
            semilogx(kyarr,(gamma_1[k-1]-ExBShear[k-1])/kyarr**pow_kyarr,lab[9],linewidth=lw+1,label='$\gamma_{net}$')
#        gammatemp=gamma_1[k-1]
        gammatemp=gamma_1[k-1]-ExBShear[k-1]
        D_lowk=max(gammatemp[0:indbdry]/kyarr[0:indbdry]**pow_kyarr)
        D_lowk=max([D_lowk,0])
        D_highk=max(gammatemp[indbdry:]/kyarr[indbdry:]**pow_kyarr)
        D_highk=max([D_highk,0])
        try:
            S=D_lowk/(D_lowk+D_highk)
        except:
            S=1.
#        print('rho='+str(int(ra*100)/100.))
#        print('S = ',S)
        print('rho:%-6.2e,  S:%-6.2e'%(ra,S))
    else:
        loglog(kyarr,gamma_1[k-1]/kyarr**pow_kyarr,lab[7],linewidth=lw,label='gamma rho='+str(int(ra*100)/100.))
        if ipltExB==1:
            loglog(kyarr,ExBShear[k-1]/kyarr**pow_kyarr,lab[8],linewidth=lw-1,label='Gamma_E_eff')
        if ipltgamnet == 1:
            loglog(kyarr,(gamma_1[k-1]-ExBShear[k-1])/kyarr**pow_kyarr,lab[9],linewidth=lw+1,label='Gamma_net')
# determine whether to write the omega and gamma_out to a file
iwrite=0
if iwrite==1:
    fid = open('/scratch/xiangjian/test/tglf/forquasiweight/65072/lin.txt','w')
    for k in ipltspectrum:
        count=0
        for item in kyarr:
            print(k,count)
            line=str(item)+'  '+str(gamma_1[k-1][count])+'  '+str(ExBShear[k-1])+' '+str(w_1[k-1][count])
            fid.write(line)
            fid.write('\n')
            count=count+1
legend(loc=1,fontsize=fs2).draggable(True)
#title('dominate mode growth rate/ky^'+str(pow_kyarr),fontsize=fs1)
title('r/a='+str(int(100*ra)/100.),fontsize=fs1)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
#xlim([0.1,30])
xlim([0.1,1.2*max(kyarr)])
#ylim([1.e-3,1.e0])
xlabel('$k_y$*$\\rho_s$',fontsize=fs1)
subplot(222)
for k in ipltspectrum:
#    plot(kyarr,w_2[k-1],lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
    ra=root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']
    semilogx(kyarr,w_2[k-1]/kyarr**pow_kyarr,lab[k-1],linewidth=lw,label='rho='+str(int(100*ra)/100.))
legend(loc=1,fontsize=fs2).draggable(True)
title('subdominate mode frequency/ky^'+str(pow_kyarr),fontsize=fs1)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
xlim([0.1,1.2*max(kyarr)])
subplot(224)
for k in ipltspectrum:
    ra=root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']
#    plot(kyarr,gamma_2[k-1],lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
#    loglog(kyarr,gamma_2[k-1]/kyarr,lab[k-1],linewidth=lw,label='rho='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
    if ilogplt == 0:
        semilogx(kyarr,gamma_2[k-1]/kyarr**pow_kyarr,lab[k-1],linewidth=lw,label='rho='+str(int(100*ra)/100.))
    else:
        loglog(kyarr,gamma_2[k-1]/kyarr**pow_kyarr,lab[k-1],linewidth=lw,label='rho='+str(int(100*ra)/100.))
#    semilogx(kyarr,ExBShear[k-1]*ones(len(kyarr))/kyarr,lab[k-1],linewidth=lw,label='Gamma_E rho='+str(int(ra*100)/100.))
legend(loc=1,fontsize=fs2).draggable(True)
title('Subdominate mode frequency/ky^'+str(pow_kyarr),fontsize=fs1)
xticks(fontsize=fs2)
yticks(fontsize=fs2)
#xlim([0.1,30])
xlim([0.1,1.2*max(kyarr)])
#lim([1.e-3,1.e0])
xlabel('ky*rho_s',fontsize=fs1)
