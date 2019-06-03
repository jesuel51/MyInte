import numpy as np
fs1=24
fs2=20
iplot=array([0,0,0,1])
plt.close()
# define a function to read the out.tgyro.w* series data
def readw(fn):
    fid=open(fn,'r')
    lines=fid.readlines()
    count=0
    data=[]
    for line in lines:
        linetemp=line.split()
        if count==1:
            kyrho=[float(item) for item in linetemp[1:]]
        if count>1:
            data.append([float(item) for item in linetemp])
        count=count+1
    data=array(data).T
    ra=data[0]
    data=data[1:]
    return kyrho,ra,data
# this scripts is used to plot the micro-stability issues for all radiuas and kyrho
ptgyro=root['SETTINGS']['PLOTS']['p_tgyro']
if root['INPUTS']['TGYROInput']['input.tgyro'].has_key('TGYRO_STAB_NKY'):
    nky=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_STAB_NKY']
else:
    nky=2
Output=root['OUTPUTS']['TGYROOutput']['spectrum']
spectrum=OMFIT['MyInte']['OUTPUTS']['TGYROOutput']['spectrum']
datamethod=1 # 0 for omfit data format, 1 for reading as just a txt file
if datamethod==0:
    wr_elec=spectrum['out.tgyro.wr_elec']['data']
    wr_ion=spectrum['out.tgyro.wr_ion']['data']
    wi_elec=spectrum['out.tgyro.wi_elec']['data']
    wi_ion=spectrum['out.tgyro.wi_ion']['data']
    # initialization
    wr_elec_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
    wr_ion_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
    wi_elec_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
    wi_ion_arr=[[0 for col in range(ptgyro+1)] for row in range(nky+1)]
    # get the data
    ra=wr_elec['col1'][0:ptgyro+1]
    for k in linspace(2,nky+1,nky):
        wr_elec_arr[int(k)-2]=wr_elec['col'+str(int(k))]
        wr_ion_arr[int(k)-2]=wr_ion['col'+str(int(k))]
        wi_elec_arr[int(k)-2]=wi_elec['col'+str(int(k))]    
        wi_ion_arr[int(k)-2]=wi_ion['col'+str(int(k))]
        kyrho=[wr_elec_arr[int(k)][0] for k in linspace(0,nky-1,nky)]
else:
    kyrho,ra,wr_elec_arr=readw(spectrum['out.tgyro.wr_elec'].filename)
    kyrho,ra,wr_ion_arr=readw(spectrum['out.tgyro.wr_ion'].filename)
    kyrho,ra,wi_elec_arr=readw(spectrum['out.tgyro.wi_elec'].filename)
    kyrho,ra,wi_ion_arr=readw(spectrum['out.tgyro.wi_ion'].filename)
#    ra=wr_elec_arr[0]
lab=['-bo','-b*','-bd','-ko','-k*','-kd','-ro','-r*','-rd','-go','-g*','-gd','-yo','-y*','-yd']
if iplot[0]==1:
    figure('linear stability analysis')
    subplot(2,2,1)
    for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
        plot(kyrho,[wr_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    #xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wr_elec')
    subplot(2,2,2)
    for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
        plot(kyrho,[wr_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    #xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wr_ion')
    subplot(2,2,3)
    for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
        plot(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    #    semilogy(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wi_elec')
    subplot(2,2,4)
    for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
        plot(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    #    semilogy(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wi_ion')
# ======================================================================================================
# plot the spectrum of  radius specified
# ======================================================================================================
iradius=root['SETTINGS']['PLOTS']['ipltspectrum'];
iradius=array([iradius])
if iplot[1]==1:
    figure('spectrum for the given radius')
    subplot(2,2,1)
    for p in iradius:
        plot(kyrho,[wr_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    #xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wr_elec')
    subplot(2,2,2)
    for p in iradius:
        plot(kyrho,[wr_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    #xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wr_ion')
    subplot(2,2,3)
    for p in iradius:
        plot(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    #    semilogy(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wi_elec')
    subplot(2,2,4)
    for p in iradius:
        plot(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    #    semilogy(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],lab[int(p)],label=str(ra[p]))
    legend(loc=0).draggable(True)
    xlabel('kyrho')
    ylabel('a/cs*gamma')
    title('wi_ion')
# ======================================================================================================
# plot the maxmium growth rate for evergy radius
# ======================================================================================================
wi_ion_max=linspace(0,0,ptgyro+1)
wi_elec_max=linspace(0,0,ptgyro+1)
#for p in linspace(1,ptgyro-1,ptgyro-1):
for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
    wi_elec_max[p]=max([wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
    wi_ion_max[p]=max([wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
if iplot[2]==1:
    figure('maximum growth rate for each radius')
    #plot([float(item) for item in ra],wi_elec_max,'-bo',label='wi_elec')
    #plot([float(item) for item in ra],wi_ion_max,'-ro',label='wi_ion')
    semilogy([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],wi_elec_max[1:ptgyro+1],'-bo',label='wi_elec')
    semilogy([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],wi_ion_max[1:ptgyro+1],'-ro',label='wi_ion')
    legend(loc=0).draggable(True)
    xlabel('r/a')
    ylabel('a/cs*gamma')
# =========================================================
# plot the growth rate and real frequency for a specific ky for evergy radius
# ========================================================
wi_ion_ky=linspace(0,0,ptgyro+1)
wr_ion_ky=linspace(0,0,ptgyro+1)
wi_elec_ky=linspace(0,0,ptgyro+1)
wr_elec_ky=linspace(0,0,ptgyro+1)
ExBShear=zeros(ptgyro)
for k in range(1,ptgyro+1):
    ExBShear[k-1]=root['OUTPUTS']['TGYROOutput'][k]['VEXB_SHEAR']
    ExBShear[k-1]=0.3*sqrt(root['OUTPUTS']['TGYROOutput'][k]['KAPPA_LOC'])*ExBShear[k-1]
ky_care=root['SETTINGS']['PLOTS']['ky_care']
for p in linspace(1-datamethod,ptgyro-datamethod,ptgyro):
#    wi_elec_ky[p]=spline(kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],ky_care)
#    wr_elec_ky[p]=spline(kyrho,[wr_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)],ky_care)
#    wi_ion_ky[p]=spline(kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],ky_care)
#    wr_ion_ky[p]=spline(kyrho,[wr_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)],ky_care)
    wi_elec_ky[p]=interp(ky_care,kyrho,[wi_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
    wr_elec_ky[p]=interp(ky_care,kyrho,[wr_elec_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
    wi_ion_ky[p]=interp(ky_care,kyrho,[wi_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
    wr_ion_ky[p]=interp(ky_care,kyrho,[wr_ion_arr[int(k)][p] for k in linspace(0,nky-1,nky)])
if iplot[3]==1:
    figure('ky='+str(ky_care)+' for each radius',figsize=[16,8])
    subplot(1,2,1)
    #plot([float(item) for item in ra],wi_elec_max,'-bo',label='wi_elec')
    #plot([float(item) for item in ra],wi_ion_max,'-ro',label='wi_ion')
    ra_elec=[float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]]
    ra_ion=[float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]]
    wi_elec_ky_temp=wi_elec_ky[1:ptgyro+1]
    wi_ion_ky_temp=wi_ion_ky[1:ptgyro+1]
    def delarr(X,num):
        X=list(X)
    #    del X[array(n) for n in num]
        for m in range(0,len(num)):
            del X[num[m]-m]
        X=array(X)
        return X
    count=0
    n_elec_null=[]
    for item in wi_elec_ky_temp:
        if item<1.e-5:
            n_elec_null=n_elec_null+[count]
        count=count+1
    count=0
    n_ion_null=[]
    for item in wi_ion_ky_temp:
        if item<1.e-5:
            n_ion_null=n_ion_null+[count]
        count=count+1
    wi_elec_ky_temp=delarr(wi_elec_ky_temp,n_elec_null)
    ra_elec=delarr(ra_elec,n_elec_null)
    wi_ion_ky_temp=delarr(wi_ion_ky_temp,n_ion_null)
    ra_ion=delarr(ra_ion,n_ion_null)
    semilogy(ra_elec,wi_elec_ky_temp,'-bo',label='TEM',linewidth=2)
    semilogy(ra_ion,wi_ion_ky_temp,'-ro',label='ITG',linewidth=2)
#    semilogy(ra,ExBShear,'-k',label='0.3*sqrt(kappa)*gamma_E')
    semilogy(ra,ExBShear,'-k',label='$\gamma_E$',linewidth=2)
    print('ra_elec=',ra_elec)
    print('wi_elec_ky=',wi_elec_ky_temp)
    print('ra_ion=',ra_ion)
    print('wi_ion_ky=',wi_ion_ky_temp)
    print('ra_Er=',ra)
    print('gamma_E',ExBShear)
#    root['OUTPUTS']['TGLFScan'][k]['lin']=OMFITtree()
    legend(loc=0,fontsize=fs2).draggable(True)
    ylim([1.e-4,1.e0])
    xlabel('r/a',fontsize=fs1,family='serif')
    ylabel('$\gamma$',fontsize=fs1+6,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
    subplot(1,2,2)
    #plot([float(item) for item in ra],wi_elec_max,'-bo',label='wi_elec')
    #plot([float(item) for item in ra],wi_ion_max,'-ro',label='wi_ion')
    #semilogy([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],wr_elec_ky[1:ptgyro+1],'-bo',label='wr_elec')
    #semilogy([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],-1*wr_ion_ky[1:ptgyro+1],'-ro',label='wr_ion')
    plot([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],wr_elec_ky[1:ptgyro+1],'-bo',label='TEM',linewidth=2)
    plot([float(item) for item in ra[1-datamethod:ptgyro+1-datamethod]],wr_ion_ky[1:ptgyro+1],'-ro',label='ITG',linewidth=2)
    ylim([-0.2,0.2])
    legend(loc=0,fontsize=fs2).draggable(True)
    #ylim([1.e-5,1.e0])
    xlabel('r/a',fontsize=fs1,family='serif')
    ylabel('$\omega$',fontsize=fs1+6,family='serif')
    xticks(fontsize=fs2,family='serif')
    yticks(fontsize=fs2,family='serif')
# we want to sperate the particle and energy of electrostatic contribution out

