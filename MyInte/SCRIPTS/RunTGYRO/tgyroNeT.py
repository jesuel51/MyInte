# BackGround: Sometimes TGYRO can not converge when evolving T & W simultaneously.
# So here we shall try an technique , similar to that of fulltgyro. That is to evolve 1 parameter and fix it, then evolve another one.
tol=1.
TErr=2.
ncount=0
imergeDT=root['SETTINGS']['PHYSICS']['imergeDT']
DenFrac=root['SETTINGS']['PHYSICS']['DenFrac']
TeErrArr=[]
neErrArr=[]
w0ErrArr=[]
ErrArr=[]
while TErr>tol and ncount<3:
# Evolve T
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=1
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=1
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=0
    Te_old=root['INPUTS']['TGYROInput']['input.profiles']['Te']
    ne_old=root['INPUTS']['TGYROInput']['input.profiles']['ne']
    w0_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
    root['OUTPUTS']['TGYROOutput']=OMFITtree()
    root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()
    root['OUTPUTSRec']['TGYROOutput'][ncount*2]=root['OUTPUTS']['TGYROOutput']
    root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fixed T
    root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']=root['SETTINGS']['TEMP']['Ti']
    root['INPUTS']['TGYROInput']['input.profiles']['Ti_2']=root['SETTINGS']['TEMP']['Ti']
    root['INPUTS']['TGYROInput']['input.profiles']['Ti_3']=root['SETTINGS']['TEMP']['Ti']
    root['INPUTS']['TGYROInput']['input.profiles']['Ti_4']=root['SETTINGS']['TEMP']['Ti']
    root['INPUTS']['TGYROInput']['input.profiles']['Te']=root['SETTINGS']['TEMP']['Te']
#Evolve Ne
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=0
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=0
    root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
    root['OUTPUTS']['TGYROOutput']=OMFITtree()
    root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()
    root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
    root['SCRIPTS']['assit']['updateTnw.py'].run()
#Fix Ne
#    root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
    if imergeDT==1:
        root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*(DenFrac[0]+DenFrac[1])
        root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
        root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
    else:
        root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[0]
        root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[1]
        root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
        root['INPUTS']['TGYROInput']['input.profiles']['ni_4']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
    Te_new=root['SETTINGS']['TEMP']['Te']
    ne_new=root['SETTINGS']['TEMP']['ne']
    w0_new=root['SETTINGS']['TEMP']['w0']
    normTeErr=norm(abs((Te_old-Te_new)/Te_new))
    normneErr=norm(abs((ne_old-ne_new)/ne_new))
    normw0Err=norm(abs((w0_old-w0_new)/(w0_new+1)))
    Err=(normTeErr+normneErr+normw0Err)/3.
    ncount=ncount+1
    print(str(ncount)+'ITERATION')
    print('NormErr=',Err)
    TeErrArr.append(normTeErr)
    neErrArr.append(normneErr)
    w0ErrArr.append(normw0Err)
    ErrArr.append(Err)
root['SETTINGS']['TEMP']['TeErrArr']=TeErrArr
root['SETTINGS']['TEMP']['neErrArr']=neErrArr
root['SETTINGS']['TEMP']['w0ErrArr']=w0ErrArr
root['SETTINGS']['TEMP']['ErrArr']=ErrArr
