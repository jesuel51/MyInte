#itemRT=root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']['nbdrive_naml']['RTCENA(1)']
itemRT=root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']['nbdrive_naml']['RTCENA']
#itemPhi=root['INPUTS']['ONETWOInput']['inone_pre']['namelis2']['phaiec(1)']
itemPhi=root['INPUTS']['ONETWOInput']['inone_pre']['namelis2']['phaiec']
#itemTheta=root['INPUTS']['ONETWOInput']['inone_pre']['namelis2']['thetec(1)']
itemTheta=root['INPUTS']['ONETWOInput']['inone_pre']['namelis2']['thetec']
nbeam=root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']['nbdrive_naml']['NBEAM']
nech=root['SETTINGS']['PHYSICS']['nech']
if nbeam==1:
    NBdir=str(int(itemRT))
else:
    NBdir=''
    for k in linspace(0,nbeam-1,nbeam):
        NBdir=NBdir+'_'+str(int(itemRT[k]))
if nech==1:
    Phidir=str(int(itemPhi))
    Thetadir=str(int(itemTheta))
else:
    Phidir=''
    Thetadir=''
    for k in linspace(0,nech-1,nech):
        Phidir=Phidir+'_'+str(int(itemPhi[k]))
        Thetadir=Thetadir+'_'+str(int(itemTheta[k]))
workdir='RT'+NBdir+'Phi'+Phidir+'Theta'+Thetadir+'/'
root['SETTINGS']['PLOTS']['workdir']=workdir
