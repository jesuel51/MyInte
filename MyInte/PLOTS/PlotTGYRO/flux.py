#-*-Python-*-
# Created by xiangjian at 2015/05/04 21:32
#plt.close();
# define a function to read the out.tgyro.*

def readouttgyro(filename):
# return all the numerisim data in a format of [numrho*niter, ncol]
    f=open(filename,'Ur')
    fread=f.readlines()
    lis=[]
    for line in fread:
        lintemp=line.split()
        try:
            temp=float(lintemp[0])
            lis.append(line)
        except:
            continue
# turn the list to array so that it can be easily handled
    row=len(lis)
    col=len(lis[0].split())
    arr=zeros([row,col])
    for k in arange(row):
        arr[k]=[float(item) for item in lis[k].split()]
    arr=arr.T
    return arr
    f.close()
#
physics=root['SETTINGS']['PHYSICS']
iview=root['SETTINGS']['PLOTS']['iview']
outtgyro=root['OUTPUTSRec']['TGYROOutput'][iview]
if outtgyro.has_key('out.tgyro.evo_n2') and physics['ievoHe']==1:
    arr_evo_nhe=readouttgyro(outtgyro['out.tgyro.evo_n2'].filename)
arr_evo_ne=readouttgyro(outtgyro['out.tgyro.evo_ne'].filename)
arr_evo_Te=readouttgyro(outtgyro['out.tgyro.evo_te'].filename)
arr_evo_Ti=readouttgyro(outtgyro['out.tgyro.evo_ti'].filename)
arr_evo_Er=readouttgyro(outtgyro['out.tgyro.evo_er'].filename)
# plot
fs1=16;
fs2=24;
fs3=22;
inputtgyro = root['INPUTS']['TGYROInput']['input.tgyro']
ptgyro = len(inputtgyro['DIR'])
arr_geometry1=readouttgyro(outtgyro['out.tgyro.geometry.1'].filename)
rho=arr_geometry1[1][-ptgyro-1:]
figure('Gorybohm Normalized Flux',figsize=[10,8])
subplot(2,2,1)
semilogy(rho,arr_evo_Te[1][-ptgyro-1:],'-*k',linewidth=2,label='transp')
semilogy(rho,arr_evo_Te[2][-ptgyro-1:],'-or',linewidth=2,label='target')
legend(loc='lower right',fontsize=fs1).draggable(True)
#xlabel('$rho$',fontsize=fs2,family='serif')
ylabel('GyroBohm',fontsize=fs2,family='serif')
text(0.1,1.e1,'(a) Qe',fontsize=fs3,family='serif')
ylim([1.e-3,1.e2])
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
subplot(2,2,2)
semilogy(rho,arr_evo_Ti[1][-ptgyro-1:],'-*k',linewidth=2)
semilogy(rho,arr_evo_Ti[2][-ptgyro-1:],'-or',linewidth=2)
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
ylim([1.e-3,1.e2])
#xlabel('$rho$',fontsize=fs2,family='serif')
text(0.1,1.e1,'(b) Qi',fontsize=fs3,family='serif')
#ylabel('$EFlux_e/GB$',fontsize=fs2,family='serif')
subplot(2,2,3)
semilogy(rho,arr_evo_ne[1][-ptgyro-1:],'-*k',linewidth=2)
semilogy(rho,arr_evo_ne[2][-ptgyro-1:],'-or',linewidth=2,label='Electron')
try: 
    semilogy(rho,arr_evo_nhe[1][-ptgyro-1:],'-*g',linewidth=2)
    semilogy(rho,arr_evo_nhe[2][-ptgyro-1:],'-om',linewidth=2,label='Helium')
    legend(loc=0,fontsize=fs2).draggable(True)
except:
    print('No helium evolution!')
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
ylabel('GyroBohm',fontsize=fs2,family='serif')
ylim([1.e-4,1.e0])
xlabel('$rho$',fontsize=fs2,family='serif')
text(0.1,1.e-1,'(c) $\Gamma_e$',fontsize=fs3,family='serif')
#ylabel('$PFlux_e/GB$',fontsize=fs2,family='serif')
subplot(2,2,4)
semilogy(rho,arr_evo_Er[1][-ptgyro-1:],'-*k',linewidth=2)
semilogy(rho,arr_evo_Er[2][-ptgyro-1:],'-or',linewidth=2)
legend(loc='lower right',fontsize=fs1).draggable(True)
xticks(fontsize=fs1,family='serif')
yticks(fontsize=fs1,family='serif')
ylim([1.e-3,1.e2])
xlabel('$rho$',fontsize=fs2,family='serif')
text(0.1,1.e1,'(d) $\Pi$',fontsize=fs3,family='serif')
#ylabel('$MFlux/GB$',fontsize=fs2,family='serif')
