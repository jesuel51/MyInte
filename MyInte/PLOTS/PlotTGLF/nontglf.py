#  this script is used to plot the flux of each species and each modes
#  the radius is specified by the root['SETTINGS']['PHYSICS']['ipltspectrum']
#  let's define a function to read the out.tglf.flux_spectrum typefile
def readspectrum(filename):
    f=open(filename,'Ur')
    l=[]
    count=0
    for line in f:
        try:
            case=float(line[0:6])
            l.append(line)
        except:
            count=count+1
    #        print(count)
    col=len(l[0].split())
    row=len(l)
    ll=zeros([row,col])
    count=0
    for item in l:
        ll[count]=[float(item2) for item2 in item.split()]
        count=count+1
    return ll
    f.close()
def readflux(filename):
    f=open(filename,'Ur')
    for line in f:
        flux=[float(item) for item in line.split()]
    return flux
    f.close()
    
ns=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_N_ION']+1 # number of species
nfield=1
if root['INPUTS']['TGLFInput']['input.tglf']['USE_BPER']==True:
    nfield=nfield+1
if root['INPUTS']['TGLFInput']['input.tglf']['USE_BPAR']==True:
    nfield=nfield+1
ipltspectrum= root['SETTINGS']['PLOTS']['ipltspectrum']
niplt=len(ipltspectrum)
fn=root['OUTPUTS']['TGLFScan'][ipltspectrum[0]]['nonlin']['out.tglf.flux_spectrum'].filename
lltemp=readspectrum(fn)
nky=size(lltemp.T[0])/nfield/ns
#nky=len(root['SETTINGS']['SETUP']['kyarr'])
specdata=zeros([niplt,nky*nfield*ns,6])
fluxdata=zeros([niplt,ns*4])
#count=0
for count in range(0,niplt):
    try:
        ll=readspectrum(root['OUTPUTS']['TGLFScan'][ipltspectrum[count]]['nonlin']['out.tglf.flux_spectrum'].filename)
        specdata[count]=ll
        flux=readflux(root['OUTPUTS']['TGLFScan'][ipltspectrum[count]]['nonlin']['out.tglf.gbflux'].filename)
        fluxdata[count]=flux
    except:
        specdata[count]=zeros([nky*nfield*ns,6])
        fluxdata[count]=zeros([ns*4])
#    count=count+1
# plot
#lab=['-kd','-ko','-k*','-ks','-md','-mo','-m*','-ms','-bd','-bo','-b*','-bs','-rd','-ro','-r*','-rs']
lab=['-kd','-md','-bd','-rd','-ko','-mo','-bo','-ro','-k*','-m*','-b*','-r*','-ks','-ms','-bs','-rs']
#ion=['Elec','DT','He','Ar']
ion=['Elec','Ion','He','Ar']
fs1=24
fs2=20
fs3=20
lw=2
#figure('flux for each ky,left(phi contribution),right(B_para contribution)')
# first, let's get the all the flux first
niplt=len(ipltspectrum)
pflux=zeros([niplt,ns,nky*nfield])
Eflux=zeros([niplt,ns,nky*nfield])
TorStrflux=zeros([niplt,ns,nky*nfield])
ParStrflux=zeros([niplt,ns,nky*nfield])
Exchflux=zeros([niplt,ns,nky*nfield])
ra=zeros(niplt)
for k in range(0,niplt):
    ll=specdata[k]
    ky=ll.T[0].reshape(ns,nky*nfield)
    pflux[k]=ll.T[1].reshape(ns,nky*nfield)
    Eflux[k]=ll.T[2].reshape(ns,nky*nfield)
    TorStrflux[k]=ll.T[3].reshape(ns,nky*nfield)
    ParStrflux[k]=ll.T[4].reshape(ns,nky*nfield)
    Exchflux[k]=ll.T[5].reshape(ns,nky*nfield)
    ra[k]=str(root['OUTPUTS']['TGYROOutput'][ipltspectrum[k]]['RMIN_LOC'])
# for test, this test shows the total flux is the sum of the flux over the ky
#print(sum(pflux[0][0]))
#print(sum(Eflux[0][0]))
#print(sum(TorStrflux[0][0]))
#print(sum(ParStrflux[0][0]))
# basically, it has been tested that the output flux is the sum over ky
# next ,we should give a summary on the flux, named particle&ion energy&electron energy flux * low-k&high-k&total
ky=ky[0][0:nky]
low_k_bdry = 1.  # the boundary of index for low-k
ind_low_k_bdry=max(find(ky<low_k_bdry))+1
for k in range(0,niplt):
#    print('r/a=',str(root['OUTPUTS']['TGYROOutput'][ipltspectrum[k]]['RMIN_LOC']))
    print('RLTS=',str(root['OUTPUTS']['TGYROOutput'][ipltspectrum[k]]['RLTS_2']))
    p_lowk = sum(pflux[k][0][0:ind_low_k_bdry])    # low-k particle contribution
    p_highk = sum(pflux[k][0][ind_low_k_bdry:])    # high-k particle contribution
    p_total = sum(pflux[k][0])                     # high-k particle contribution
    Elec_lowk = sum(Eflux[k][0][0:ind_low_k_bdry]) # low-k electron energy contribution
    Elec_highk = sum(Eflux[k][0][ind_low_k_bdry:]) # high-k electron energy contribution
    Elec_total = sum(Eflux[k][0])                  # total electron energy contribution
    Ion_lowk = sum([sum(Eflux[k][m][0:ind_low_k_bdry]) for m in range(1,ns)])  # low-k ion energy contribution
    Ion_highk = sum([sum(Eflux[k][m][ind_low_k_bdry:]) for m in range(1,ns)])  # high-k ion energy contribution
    Ion_total = sum([sum(Eflux[k][m]) for m in range(1,ns)])  # total ion energy contribution
    TorM_lowk = sum([sum(TorStrflux[k][m][0:ind_low_k_bdry]) for m in range(1,ns)])  # low-k Toroidal momentum contribution
    TorM_highk = sum([sum(TorStrflux[k][m][ind_low_k_bdry:]) for m in range(1,ns)])  # high-k Toroidal momentum contribution
    TorM_total = sum([sum(TorStrflux[k][m]) for m in range(1,ns)])  # high-k Toroidal momentum contribution
    print('           low-k        high-k      total      high-k/total(%)')
    print("particle %-12.2e %-12.2e %-12.2e %-12.2d"%(p_lowk,p_highk,p_total,100*p_highk/p_total))
    print('electron %-12.2e %-12.2e %-12.2e %-12.2d'%(Elec_lowk,Elec_highk,Elec_total,100*Elec_highk/Elec_total))
    print('ion      %-12.2e %-12.2e %-12.2e %-12.2d'%(Ion_lowk,Ion_highk,Ion_total,100*Ion_highk/Ion_total))
    print('TorM     %-12.2e %-12.2e %-12.2e %-12.2d'%(TorM_lowk,TorM_highk,TorM_total,100*TorM_highk/TorM_total))
iwritefile=0
if iwritefile==1:
    fid=open('/scratch/xiangjian/test/tglf/EAST65072_6000/ALTiScan_V4.txt','w')
    for k in range(0,12):
        line=str(str(root['OUTPUTS']['TGYROOutput'][ipltspectrum[k]]['RLTS_2']))+'    '+\
             str(sum(pflux[k][0][0:ind_low_k_bdry]))+'    '+\
             str(sum(pflux[k][0][ind_low_k_bdry:]))+'    '+\
             str(sum(Eflux[k][0][0:ind_low_k_bdry]))+'    '+\
             str(sum(Eflux[k][0][ind_low_k_bdry:]))+'    '+\
             str(sum([sum(Eflux[k][m][0:ind_low_k_bdry]) for m in range(1,ns)]))+'    '+\
             str(sum([sum(Eflux[k][m][ind_low_k_bdry:]) for m in range(1,ns)]))+'    '+\
             str(sum([sum(TorStrflux[k][m][0:ind_low_k_bdry]) for m in range(1,ns)]))+'    '+\
             str(sum([sum(TorStrflux[k][m][ind_low_k_bdry:]) for m in range(1,ns)]))
        fid.write(line)
        fid.write('\n')
    fid.close()
iplotall=0
if iplotall==1:
    figure('flux for each ky,left(phi contribution),right(B_para contribution)')
    subplot(4,nfield,1)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,pflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1 
    title('particle flux-GB',fontsize=fs1)
    subplot(4,nfield,nfield*1+1)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,Eflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Energy flux-GB',fontsize=fs1)    
    subplot(4,nfield,nfield*2+1)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,TorStrflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Toroidal Stress flux-GB',fontsize=fs1)
    subplot(4,nfield,nfield*3+1)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,ParStrflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks(fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Parallel Stress flux-GB',fontsize=fs1)
#subplot(4,nfield,nfield*4+1)
#count=0
#for k in range(0,niplt):
#    for m in range(0,ns):
#        semilogx(ky,Exchflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
#        xlim([1.e-1,3.e1])
#        xticks(fontsize=fs2)
#        yticks(fontsize=fs2)
#        legend(loc='lower right').draggable(True)
#        count=count+1
#title('exchange flux-GB',fontsize=fs1)
#====================================================================
    subplot(4,nfield,2)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,pflux[k][m][nky:],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('particle flux-GB',fontsize=fs1)
    subplot(4,nfield,nfield*1+2)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,Eflux[k][m][nky:],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Energy flux-GB',fontsize=fs1)
    subplot(4,nfield,nfield*2+2)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,TorStrflux[k][m][nky:],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks([],fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Toroidal Stress flux-GB',fontsize=fs1)
    subplot(4,nfield,nfield*3+2)
    count=0
    for k in range(0,niplt):
        for m in range(0,ns):
            semilogx(ky,ParStrflux[k][m][nky:],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            xlim([1.e-1,3.e1])
            xticks(fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right').draggable(True)
            count=count+1
    title('Parallel Stress flux-GB',fontsize=fs1)
#subplot(4,nfield,nfield*4+2)
#count=0
#for k in range(0,niplt):
#    for m in range(0,ns):
#        semilogx(ky,Exchflux[k][m][nky:],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
#        xlim([1.e-1,3.e1])
#        xticks(fontsize=fs2)
#        yticks(fontsize=fs2)
#        legend(loc='lower right').draggable(True)
#        count=count+1
#title('exchange flux-GB',fontsize=fs1)
#print('summary')
#for k in ipltspectrum:
#    print('r/a='+str(root['OUTPUTS']['TGYROOutput'][k]['RMIN_LOC']))
#    filename=root['OUTPUTS']['TGLFScan'][ipltspectrum[0]]['nonlin']['out.tglf.run'].filename
#    f=open(filename,'Ur')
#    for line in f:
#        print(line)
# we want to sperate the energy and particle flux of the electrostatic contribution out
ipltGQ=1
if ipltGQ==1:
    figure(figsize=[12,10])
    subplot(1,2,1)
    for k in range(0,niplt):
#        for m in range(0,ns):
        for m in range(0,1):
#            semilogx(ky,pflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            semilogx(ky,pflux[k][m][0:nky],lab[m],linewidth=lw,label=ion[m])
            xlim([1.e-1,3.e1])
            xticks(fontsize=fs2)
            yticks(fontsize=fs2)
#            legend(loc='lower right').draggable(True)
            count=count+1
    semilogx(ky,zeros(nky),'--k',linewidth=int(lw/2))
    xlabel('$k_y*\\rho_s$',fontsize=fs1)
    title('particle flux-GB',fontsize=fs1)
    subplot(1,2,2)
    count=0
    for k in range(0,niplt):
#        for m in range(0,ns):
        for m in range(0,2):
    #        semilogx(ky,Eflux[k][m][0:nky],lab[count],linewidth=lw,label=['r/a='+str(int(100*ra[k])/100.)+'-'+ion[m]])
            semilogx(ky,Eflux[k][m][0:nky],lab[m],linewidth=lw,label=ion[m])#
            xlim([1.e-1,3.e1])
            xticks(fontsize=fs2)
            yticks(fontsize=fs2)
            legend(loc='lower right',fontsize=fs2).draggable(True)
            count=count+1
    xlabel('$k_y*\\rho_s$',fontsize=fs1)
    title('Energy flux-GB',fontsize=fs1)
#    title('r/a='+str(int(100*ra[k])/100.),fontsize=fs1,family='serif')
# determine whether to plot the quasi-linear weight
# only the electrostatic quasi-linear weight is plotted
ipltweight=0
ms=6
if ipltweight==1:
    fn=root['OUTPUTS']['TGLFScan'][ipltspectrum[0]]['nonlin']['out.tglf.potential_spectrum'].filename
    amptemp=readspectrum(fn)
    phi_amp=amptemp.T[1]  # the normalized potential, fai_norm=e*fai/Te
    figure(figsize=[12,8])
    subplot(2,2,1)
    for k in range(0,niplt):
#        for m in range(0,ns):  #only electron particle flux is plotted
        m=1
        semilogx(ky,pflux[k][m][0:nky],'-bo',linewidth=lw,markersize=ms)
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    ylabel('$\Gamma$',fontsize=fs1,family='serif')
    subplot(2,2,2)
    for k in range(0,niplt):    #only the electron and first ion is plotted
        semilogx(ky,Eflux[k][0][0:nky],'-bo',label='Electron',linewidth=lw,markersize=ms)  # Electron energy flux
        semilogx(ky,Eflux[k][1][0:nky],'-ro',label='Ion',linewidth=lw,markersize=ms)       # Ion energy flux
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    ylabel('$Q$',fontsize=fs1,family='serif')
    legend(loc=0,fontsize=fs2).draggable(True)
    subplot(2,2,3)
    for k in range(0,niplt):
#        for m in range(0,ns):  #only electron particle flux is plotted
        m=1
        semilogx(ky,pflux[k][m][0:nky]/phi_amp,'-bo',linewidth=lw,markersize=ms)
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('$k_y*\\rho_s$',fontsize=fs1,family='serif')
    ylabel('$\Gamma_{ql}$',fontsize=fs1,family='serif')
    subplot(2,2,4)
    for k in range(0,niplt):    #only the electron and first ion is plotted
        semilogx(ky,Eflux[k][0][0:nky]/phi_amp,'-bo',label='Electron',linewidth=lw,markersize=ms)  
        semilogx(ky,Eflux[k][1][0:nky]/phi_amp,'-ro',label='Ion',linewidth=lw,markersize=ms)       
    xticks(fontsize=fs2)
    yticks(fontsize=fs2)
    xlabel('$k_y*\\rho_s$',fontsize=fs1,family='serif')
    ylabel('$Q_{ql}$',fontsize=fs1,family='serif')
    legend(loc=0,fontsize=fs2).draggable(True)
