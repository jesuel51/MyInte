# this script is used to read the following data , which is used to compare to the 0D data, includes:
# Te(0),Ti(0),ne_avg,pf_ne,f_bs,P_H,P_ECH,P_NB,fusion gain Q, fusion power,beta_n, li,ECCD efficiency, NBCD efficiency and total efficiency, H98 factor;
# first T(0)
k=root['SETTINGS']['PLOTS']['iview']
#ibetan=root['SETTINGS']['PLOTS']['ibeta_n']
ibeta_n=0
inone=root['INPUTSRec']['ONETWO'][k]['inone']['NAMELIS1']
#Te=root['OUTPUTSRec']['ProfileGenOutput'][int(k)]['Te']
#Ti=root['OUTPUTSRec']['ProfileGenOutput'][int(k)]['Ti_1']
#ne=root['OUTPUTSRec']['ProfileGenOutput'][int(k)]['ne']
Te=inone['TEIN']
Ti=inone['TIIN']
ne=inone['ENEIN']/1.e13
n_DT=inone['ENP'].T[0]/1.e13*2
n_He=inone['ENI'].T[0]/1.e13
n_Ar=inone['ENI'].T[1]/1.e13
Te0=Te[0]
Ti0=Ti[0]
ne_avg=sum(ne)/len(ne)
pf_ne=ne[0]/ne_avg
n_DT_avg=sum(n_DT)/len(n_DT)
n_He_avg=sum(n_He)/len(n_He)
n_Ar_avg=sum(n_Ar)/len(n_Ar)
# BS fraction
totboot=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totboot']['data'][-1]
f_bs=totboot/root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totcur']['data'][-1]
## all kinds of power:
#qbeame=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qbeame']['data'][-1];	# beam on electrons
pwrbme=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pwrbme']['data'][-1];
#qrfeiv=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qrfeiv']['data'][-1];	# rf on electrons
prfe=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['prfe']['data'][-1];
#qfusev=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qfusev']['data'][-1];	# fusion on electrons
#pfuse=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pfuse']['data'][-1];
pfuse=OMFIT['MyInte']['INPUTSRec']['TGYRO'][int(k)]['input.profiles']['pow_e_fus'];
#qrad=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['qrad']['data'][-1];		# radiation on  electrons
prad=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['prad']['data'][-1];
#qohm=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qohm']['data'][-1];		# ohm heating on electrons
pohm=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pohm']['data'][-1];	
#qdelten=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qdelten']['data'][-1];		# electron-ion power exchange
pdelten=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pdelten']['data'][-1];		
#qsume=qbeame+qrfeiv+qfusev+qohm-qrad+qdelten;
psume=pwrbme+prfe+pfuse+pohm-prad+pdelten;
#	ion part
#qbeami=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qbeami']['data'][-1];	# beam on ions
pwrbmi=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pwrbmi']['data'][-1];
#qrfiiv=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qrfiiv']['data'][-1];	# rf on ions
prfi=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['prfi']['data'][-1];
#qfusiv=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['qfusiv']['data'][-1];	# fusion on ions
#pfusi=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['pfusi']['data'][-1];
pfusi=OMFIT['MyInte']['INPUTSRec']['TGYRO'][int(k)]['input.profiles']['pow_i_fus'];
#qsumi=qbeami+qrfiiv+qfusiv-qdelten;
psumi=pwrbmi+prfi+pfusi-pdelten
# fusion gain
#P_H=pwrbme[-1]+prfe[-1]+pfuse[-1]+pwrbmi[-1]+prfi[-1]+pfusi[-1];
QFlag=root['SETTINGS']['PHYSICS']['QFlag']
if QFlag==1:
    P_H=pwrbme[-1]+prfe[-1]+pwrbmi[-1]+prfi[-1]
    P_ECH=prfe[-1]+prfi[-1]
    P_NB=pwrbme[-1]+pwrbmi[-1]
else:
    P_ECH=sum(root['INPUTSRec']['ONETWO'][int(k)]['inone']['NAMELIS2']['rfpow'])
    P_NB=sum(OMFIT['MyInte']['INPUTSRec']['ONETWO'][int(k)]['auxiliary']['nubeam.dat']['nbdrive_naml']['PINJA'])
    P_H=P_ECH+P_NB
#Q=(pwrbme[-1]+prfe[-1]+pfuse[-1]+pwrbmi[-1]+prfi[-1]+pfusi[-1])/
Q=5*(pfusi[-1]+pfuse[-1])/P_H*1.e6
li=root['OUTPUTSRec']['EFITOutput']['Out'][int(k)]['afile']['ali']
betaN=root['OUTPUTSRec']['EFITOutput']['Out'][int(k)]['afile']['betan']
# ECCD efficiency
currf=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['currf']['data'][-1]
currf[0:int(root['SETTINGS']['PHYSICS']['delta_loc']*len(currf))]=0.*currf[0:int(root['SETTINGS']['PHYSICS']['delta_loc']*len(currf))]
maxindcurrf=list(currf).index(max(currf))
totrf=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totrf']['data'][-1]
rmajloc=root['OUTPUTSRec']['ProfileGenOutput'][k]['rmaj'][maxindcurrf]
neloc=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1][maxindcurrf]
Teloc=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1][maxindcurrf]
zeta_rf=33*(neloc*1e-14)*totrf*rmajloc/((prfe[-1]+prfi[-1])*Teloc) # normalized CD efficiency from T.C.Luce, PRL,1997
gamma_rf=root['OUTPUTS']['EFITOutput']['gfile']['RCENTR']*totrf*1.e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/(prfe[-1]+prfi[-1])
# NBCD efficiency
curbeam=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['curbeam']['data'][-1]
maxindcurbeam=list(curbeam).index(max(curbeam))
totbeam=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['totb']['data'][-1]
rmajloc=root['OUTPUTSRec']['ProfileGenOutput'][k]['rmaj'][maxindcurbeam]
neloc=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1][maxindcurbeam]
Teloc=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1][maxindcurbeam]
#zeta_beam=33*(neloc*1e-14)*totbeam*rmajloc/((pwrbme[-1]+pwrbmi[-1])*Teloc)
zeta_beam=33*(neloc*1e-14)*totbeam*rmajloc/(P_NB*Teloc)
#gamma_beam=root['OUTPUTS']['EFITOutput']['gfile']['RCENTR']*totbeam*1.e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/(pwrbme[-1]+pwrbmi[-1])
gamma_beam=root['OUTPUTS']['EFITOutput']['gfile']['RCENTR']*totbeam*1.e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/P_NB
#total CD efficiency
gamma_tot=root['OUTPUTS']['EFITOutput']['gfile']['RCENTR']*(totbeam+totrf)*1.e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/(P_NB+prfe[-1]+prfi[-1])
#zeta_tot=33*1e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])*(totbeam+totrf)*rmajloc/((pwrbme[-1]+pwrbmi[-1]+prfe[-1]+prfi[-1])*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1]))
#zeta_tot=33*1e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])*(totbeam+totrf)*rmajloc/((prfe[-1]+prfi[-1]+P_NB)*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1]))
zeta_tot=33*gamma_tot*(2+0.5)/root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['te']['data'][-1][0]/2.
#gamma_tot=root['OUTPUTS']['EFITOutput']['gfile']['RCENTR']*(totbeam+totrf)*1.e-14*sum(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/len(root['OUTPUTSRec']['ONETWOOutput'][int(k)]['trpltout.nc']['ene']['data'][-1])/(pwrbme[-1]+pwrbmi[-1]+prfe[-1]+prfi[-1])
# h-factor
if OMFIT['MyInte']['SETTINGS']['PHYSICS']['reconsImp']!='':
    filename=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['summary_dt'].filename
else:
    filename=root['OUTPUTSRec']['ONETWOOutput'][int(k)]['summary'].filename
stringH='H_ITER98y2'
stringPtransp='Ptransport'
stringW='Stored Energy'
f=open(filename,'Ur')
for line in f:
    ind=line.find(stringH)
    if line.find(stringH)>0:
        H98=float(line[ind+len(stringH)+4:ind+len(stringH)+8])
    elif line.find(stringPtransp)>0:
        Ptransp=float(line[-10:])
    elif line.find(stringW)>0:
        W=float(line[-22:-10])             # total thermal stored energy
        W_ion=float(line[-34:-22])         # ion stored thermal energy
f.close()
#tau_e=W/Ptransp/1.e6
inputpro=root['INPUTSRec']['TGYRO'][int(k)]['input.profiles']
Prad=inputpro['pow_e_line'][-1]*(-1.)
#Psep=inputpro['pow_e'][-10]+inputpro['pow_i'][-10]
Psep=(P_H+Q*P_H/5.-Prad*1.e6)/1.e6
Ptransp_true=Psep
# ##########################
## here we plan to transfrom the total ion species
#def getdenfrac(fordenfrac):
#    # we assumes that the ions are D&T, frist impurity, Second impurity. The concentration of the 1st impurity(normally helium or W) is specified by user. 
#    # the format of ForDenFrac should be [F_imp1, Zeff, Z1, Z2]. Where F_imp is the concentration of the 1st impurity, Z1 and Z2 are the charge number of the 1st and 2nd impurity ions;
#    b=fordenfrac[0]
#   Zeff=fordenfrac[1]
#    Z1=fordenfrac[2]
#    Z2=fordenfrac[3]
#    # the a, b,c represent the fraction of DT, 1st impurity and 2nd Impurity ,respectively
#    #a=(Z2-Zeff+2*b)/2./(Z2-1)-b
#    a=(Z2-Zeff+Z1*b)/2./(Z2-1)-b
#    #c=(Zeff-1-2.*b)/(Z2**2-Z2)
#    c=(Zeff-1-Z1*b)/(Z2**2-Z2)
#    DenFrac=array([a,a,b,c])
#    return DenFrac
## the density profile of the 1st impurity need to be specified, and is specified in the root['SETTINGS']['DEPENDENCIES']=depend
## depend['He'] is the density of Helium, depend['W'] is the density of tungsten
#ImpName=root['SETTINGS']['TEMP']['ImpName']
#depend=root['SETTINGS']['DEPENDENCIES']
#Z2=root['SETTINGS']['PHYSICS']['ForDenFrac'][2]
#Zeff=root['SETTINGS']['PHYSICS']['ForDenFrac'][1]
#Frac_W=root['SETTINGS']['PHYSICS']['FracImp']
#Frac_He=root['SETTINGS']['PHYSICS']['ForDenFrac'][0]
#DenFrac_W=getdenfrac(array([Frac_W,Zeff,74,Z2]))
#DenFrac_He=getdenfrac(array([Frac_He,Zeff,2,Z2]))
#W_scale=W_ion/W*(1.-sum(DenFrac_He)/sum(DenFrac_W))
#W_scale=1.-W_scale
# ############################
#W_true=W*W_scale
#W_true=W
#tau_e=W_true/Ptransp_true/1.e6
#H98_true=H98*(Ptransp/Ptransp_true)**0.31  # in view of transp
#H98_true=H98_true*(W_true/W)               # in view of stored energy
H98_true=H98
W_true=W
tau_e=W/Ptransp/1.e6
outname=array(['iview','Te0','Ti0','ne_avg','n_DT_avg','n_He_avg','n_Ar_avg','ne(0)','n_DT(0)','n_He(0)','n_Ar(0)','pf_ne','f_bs','P_H','P_ECH','P_NB','Q','Pfus','betaN','li','zeta-rf','gamma_rf','zeta-beam','gamma-beam','zeta_tot-notsure','gamma_tot','H98','tau_e','stored energy','Prad(MW)','Psep(MW)'])
out=array([k,Te0,Ti0,ne_avg,n_DT_avg,n_He_avg,n_Ar_avg,ne[0],n_DT[0],n_He[0],n_Ar[0],pf_ne,f_bs,P_H,P_ECH,P_NB,Q,Q*P_H,betaN,li,zeta_rf,gamma_rf,zeta_beam,gamma_beam,zeta_tot,gamma_tot,H98_true,tau_e,W_true,Prad,Psep])
root['SETTINGS']['TEMP']['out']=out
#print("[Te0,Ti0,f_bs,P_H,P_ECH,P_NB,Q,P_fus,Beta_N]=")
for k in range(0,len(out)):
    print('%16s=%.2e'%(outname[k],out[k]))
#    print("%s"%outname[k])
#print([format(x,'.2e') for x in out])
