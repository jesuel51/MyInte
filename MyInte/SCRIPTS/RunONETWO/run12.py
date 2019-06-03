# this script is used to ensure that the output current profile is fully non-inductive, 
# here we shall realized it by dynamically adjust our heating & CD power
# we note that the last NB and last rf is used to ensure the fully non-inductive operation
fNBEC=root['SETTINGS']['PHYSICS']['fNBEC'] # detemine the ohmic current fraction distribution to NB and EC to eliminate
root['SCRIPTS']['RunONETWO']['baserun12_v57.py'].run()
ohmtol=root['SETTINGS']['PHYSICS']['ohmtol']
try :
    nRF=len(root['INPUTS']['ONETWOInput']['inone']['NAMELIS2']['rfpow'])
except:
    nRF=1
ncount=0
numit4noohmic=root['SETTINGS']['PHYSICS']['numit4noohmic']
rlxfac=0.6
trpltout=root['OUTPUTS']['ONETWOOutput']['trpltout.nc']
#nbdat=root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']
#inone=root['INPUTS']['ONETWOInput']['inone']
#nbeam=nbdat['nbdrive_naml']['NBEAM']
while (trpltout['totohm']['data'][-1]>ohmtol[1] or trpltout['totohm']['data'][-1]<ohmtol[0]):
    trpltout=root['OUTPUTS']['ONETWOOutput']['trpltout.nc']
    nbdat=root['INPUTS']['ONETWOInput']['auxiliary']['nubeam.dat']
    inone=root['INPUTS']['ONETWOInput']['inone']
    nbeam=nbdat['nbdrive_naml']['NBEAM']
    ncount=ncount+1
    curbeam=trpltout['totb']['data'][-1]
    currf=trpltout['totrf']['data'][-1]
    Powbeam=nbdat['nbdrive_naml']['PINJA']
    PowRF=inone['NAMELIS2']['rfpow']
    if nbeam>1:
#        factor=curbeam/Powbeam[-1]
        factor=curbeam/sum(Powbeam)
    else:
        factor=curbeam/Powbeam
    if nRF>1:
#        factorRF=currf/PowRF[-1]
        factorRF=currf/sum(PowRF)
    else:
        factorRF=currf/PowRF
    totohm=trpltout['totohm']['data'][-1]
    powad=fNBEC*(totohm-sum(ohmtol)/2)/factor              # additional required power of NB
    powadRF=(1.-fNBEC)*(totohm-sum(ohmtol)/2)/factorRF     # additional required power of RF
    if (nbeam==1):
        nbdat['nbdrive_naml']['PINJA'] = nbdat['nbdrive_naml']['PINJA']+powad*rlxfac
        if nbdat['nbdrive_naml']['PINJA']<0:
            nbdat['nbdrive_naml']['PINJA']=0
    else:
#        nbdat['nbdrive_naml']['PINJA'][-1] = nbdat['nbdrive_naml']['PINJA'][-1]+powad*rlxfac
        nbdat['nbdrive_naml']['PINJA'][0] = nbdat['nbdrive_naml']['PINJA'][0]+powad*rlxfac
        if nbdat['nbdrive_naml']['PINJA'][0]<0:
            nbdat['nbdrive_naml']['PINJA'][0]=0
    if (nRF==1):
        inone['NAMELIS2']['rfpow'] = inone['NAMELIS2']['rfpow']+powadRF*rlxfac
        if inone['NAMELIS2']['rfpow']<0:
            inone['NAMELIS2']['rfpow']=0
    else:
#        inone['NAMELIS2']['rfpow'][-1] = inone['NAMELIS2']['rfpow'][-1] + powadRF*rlxfac
#        inone['NAMELIS2']['rfpow'][-1] = inone['NAMELIS2']['rfpow'][-1] + powadRF*rlxfac
        inone['NAMELIS2']['rfpow'][0] = inone['NAMELIS2']['rfpow'][0] + powadRF*rlxfac
        if inone['NAMELIS2']['rfpow'][0]<0:
            inone['NAMELIS2']['rfpow'][0]=0
    root['SCRIPTS']['RunONETWO']['baserun12_v57.py'].run()
    print('BeamPower=',nbdat['nbdrive_naml']['PINJA']/1.e6,' MW')
    print('RFpower=',inone['NAMELIS2']['rfpow']/1.e6,' MW')
    print('Beam current=',int(trpltout['totb']['data'][-1])/1.e6,' MA')
    print('RF current=',int(trpltout['totrf']['data'][-1])/1.e6,' MA')
    print('BS current=',int(trpltout['totboot']['data'][-1])/1.e6,' MA')
    print('Ohmic current=',int(trpltout['totohm']['data'][-1])/1.e6,' MA')
    print(ncount)
    if (numit4noohmic[0]==1 and ncount>numit4noohmic[1]):
        break
