# this script is used to run fully the tgyro, evolve all the properties, n&T&w;
# since we found that when all the evolution switch are turned on, TGYRO is difficult to converge itself;
# but we when evolve n&T or T&w simultaneously, it's easy for tgyro to converge
# so the basic ideal of this script is TO Fix one and evolve the other one,and finally get all the parameters converged;
# for example ,we evolve n&T first, then fixed n&T and evolve w, then fix w , evolve n&T, then repeat the process
# we shall set 4 options here
ifulltgyrooption=root['SETTINGS']['PHYSICS']['ifulltgyrooption']
tol=1.
Err=2.
imergeDT=root['SETTINGS']['PHYSICS']['imergeDT']
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
DenFrac=root['SETTINGS']['PHYSICS']['DenFrac']
ncount=0
TeErrArr=[]
neErrArr=[]
w0ErrArr=[]
ErrArr=[]
while Err>tol and ncount<3:
    if ifulltgyrooption==1:
#Evolve n&T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
	Te_old=root['INPUTS']['TGYROInput']['input.profiles']['Te']
	ne_old=root['INPUTS']['TGYROInput']['input.profiles']['ne']
	w0_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fix the n&T
        root['INPUTS']['TGYROInput']['input.profiles']['ne']=root['SETTINGS']['TEMP']['ne']
	if imergeDT==1:
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*(DenFrac[0]+DenFrac[1])
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
	else:
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[0]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[1]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_4']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_2']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_3']=root['SETTINGS']['TEMP']['Ti']	
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_4']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Te']=root['SETTINGS']['TEMP']['Te']
# Evolve Er
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=0
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
#Fix Er
        root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
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
    elif ifulltgyrooption==2:
# Evolve w&T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
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
# Fix the w&T
        root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_2']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_3']=root['SETTINGS']['TEMP']['Ti']	
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_4']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Te']=root['SETTINGS']['TEMP']['Te']
# Run TGYRO to evolve Ne
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fix ne
        root['INPUTS']['TGYROInput']['input.profiles']['ne']=root['SETTINGS']['TEMP']['ne']
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
    elif ifulltgyrooption==3:
# Evolve n&w
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
	Te_old=root['INPUTS']['TGYROInput']['input.profiles']['Te']
	ne_old=root['INPUTS']['TGYROInput']['input.profiles']['ne']
	w0_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Distribute the n&w
        root['INPUTS']['TGYROInput']['input.profiles']['ne']=root['SETTINGS']['TEMP']['ne']
	if imergeDT==1:
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*(DenFrac[0]+DenFrac[1])
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
	else:
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_1']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[0]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_2']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[1]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_3']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[2]
	    root['INPUTS']['TGYROInput']['input.profiles']['ni_4']=root['INPUTS']['TGYROInput']['input.profiles']['ne']*DenFrac[3]
        root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
# Evolve T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=0
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# update T
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_2']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_3']=root['SETTINGS']['TEMP']['Ti']	
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_4']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Te']=root['SETTINGS']['TEMP']['Te']
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
    elif ifulltgyrooption==4:
# Evolve w&T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
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
# Distribute the w
        root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
# Run TGYRO to evolve n&T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fixed n
        root['INPUTS']['TGYROInput']['input.profiles']['ne']=root['SETTINGS']['TEMP']['ne']
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
    elif ifulltgyrooption==5:
# Evolve n&T
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
	Te_old=root['INPUTS']['TGYROInput']['input.profiles']['Te']
	ne_old=root['INPUTS']['TGYROInput']['input.profiles']['ne']
	w0_old=root['INPUTS']['TGYROInput']['input.profiles']['omega0']
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fix T
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_1']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_2']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_3']=root['SETTINGS']['TEMP']['Ti']	
        root['INPUTS']['TGYROInput']['input.profiles']['Ti_4']=root['SETTINGS']['TEMP']['Ti']
        root['INPUTS']['TGYROInput']['input.profiles']['Te']=root['SETTINGS']['TEMP']['Te']
# Run TGYRO to evolve Ne&w
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=1
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=0
        root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG']=1
   	root['OUTPUTS']['TGYROOutput']=OMFITtree()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run()	
  	root['OUTPUTSRec']['TGYROOutput'][ncount*2+1]=root['OUTPUTS']['TGYROOutput']
        root['SCRIPTS']['assit']['updateTnw.py'].run()
# Fix w
        root['INPUTS']['TGYROInput']['input.profiles']['omega0']=root['SETTINGS']['TEMP']['w0']
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
    else:
	print('ERROR,Please Choose Your Right FULLTGYRO Option!')
root['SETTINGS']['TEMP']['TeErrArr']=TeErrArr
root['SETTINGS']['TEMP']['neErrArr']=neErrArr
root['SETTINGS']['TEMP']['w0ErrArr']=w0ErrArr
root['SETTINGS']['TEMP']['ErrArr']=ErrArr
