## /his script is used to manage the entire flow
## module import
import time
import numpy as np
import os
irun=root['SETTINGS']['PHYSICS']['irun']
#iEr=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_ER_FEEDBACK_FLAG'];
#iNe=root['INPUTS']['TGYROInput']['input.tgyro']['LOC_NE_FEEDBACK_FLAG'];
iEvolChan=root['SETTINGS']['PHYSICS']['iEvolChan'] # determine which channels to evolve when Er profile is evolved, The order is Te,Ti,ne,Er
root['SCRIPTS']['assit']['rcdtgyroswitch.py'].run()
lmtexch=root['SETTINGS']['PHYSICS']['lmtexch']
tol=1.e-3;
err=1.;
ncycle=0;
# we are not going to change the Density profile of Ar and this profile is used to keep as an constant over the iteration which maybe used in the script distributeIon2.py
# so the prepared inone file should contain the correct profile of Ar
root['SETTINGS']['TEMP']['n_ar']=root['INPUTS']['ONETWOInput']['inone']['NAMELIS1']['eni'].T[1]/1.e13
ncycle_max=root['SETTINGS']['PHYSICS']['ncyclemax']
root['SCRIPTS']['assit']['EccdCore.py'].run()
#root['SCRIPTS']['assit']['denfrac.py'].run()
# the density profile of W should be provided in the root['SETTINGS']['DEPENDENCIES']['W']
#root['SETTINGS']['TEMP']['ImpName']='W'
#root['SCRIPTS']['assit']['distributeIonDen.py'].run()
# define a function that test whether arrb contain elements a
def ainb(a, arrb):
    for item in arrb:
        if a==item:
            return 1
physics=root['SETTINGS']['PHYSICS']
itEr=physics['itEr']
root['SCRIPTS']['assit']['rcdiniNe.py'].run()
# normally, the rmin set in tgyro will not be ~0.2 to 0.3, so we will not flatten the profile manually any longer, 2017-5-22
#root['SCRIPTS']['assit']['rcdiniT.py'].run()
#root['SCRIPTS']['assit']['rcdiniEr.py'].run()
#root['SCRIPTS']['assit']['rcdiniNeCore.py'].run()
# define some tree entry
Input12=root['INPUTS']['ONETWOInput']
Input12Rec=root['INPUTSRec']['ONETWO']
Output12=root['OUTPUTS']['ONETWOOutput']
Output12Rec=root['OUTPUTSRec']['ONETWOOutput']
InputEFIT=root['INPUTS']['EFITInput']
InputEFITRec=root['INPUTSRec']['EFIT']
OutputEFIT=root['OUTPUTS']['EFITOutput']
OutputEFITRec=root['OUTPUTSRec']['EFITOutput']
InputProGen=root['INPUTS']['ProfileGenInput']
InputProGenRec=root['INPUTSRec']['ProfileGen']
OutputProGen=root['OUTPUTS']['ProfileGenOutput']
OutputProGenRec=root['OUTPUTSRec']['ProfileGenOutput']
InputTGYRO=root['INPUTS']['TGYROInput']
InputTGYRORec=root['INPUTSRec']['TGYRO']
OutputTGYRO=root['OUTPUTS']['TGYROOutput']
OutputTGYRORec=root['OUTPUTSRec']['TGYROOutput']
while(err>tol and ncycle<ncycle_max):
    root['SETTINGS']['TEMP']['iternum']=ncycle
#   onetwo part
    if irun[0]==1:
        root['SCRIPTS']['RunONETWO']['run12.py'].run();
        Input12Rec[ncycle]=OMFITtree("")
        for item in Input12.keys():
            Input12Rec[ncycle][item]=Input12[item].duplicate()
# EFIT part
    InputEFIT['g0file']=Output12['gfile'].duplicate()
    if irun[1]==1:
        InputEFITRec[ncycle]=OMFITtree("")
        for item in InputEFIT.keys():
            InputEFITRec[ncycle][item]=InputEFIT[item].duplicate()
#	root['INPUTSRec']['EFIT'][ncycle]=root['INPUTS']['EFITInput']	
        root['SCRIPTS']['RunEFIT']['baserunEFIT.py'].run()
##  record the result for 12 and EFIT
    Output12Rec[ncycle]=OMFITtree("")
    for item in Output12:
        Output12Rec[ncycle][item]=Output12[item].duplicate()
    OutputEFITRec['In'][ncycle]=Output12['gfile'].duplicate()
    OutputEFITRec['Out'][ncycle]=OMFITtree("")
    OutputEFITRec['Out'][ncycle]['gfile']=OutputEFIT['gfile'].duplicate()
    OutputEFITRec['Out'][ncycle]['afile']=OutputEFIT['afile'].duplicate()
##  prepare for the profile_gen 
    root['SCRIPTS']['assit']['addptcsrc.py'].run()   # the added particle source (if added) will exist in the input.profiles
    InputProGen['statefile']=Output12['statefile'].duplicate()
    InputProGen['gfile']=OutputEFIT['gfile'].duplicate()
##  prepare the g-file for the next run
    Input12['gfile']=OutputEFIT['gfile']
##  profiles_gen part
    if irun[2]==1:
        InputProGenRec[ncycle]=OMFITtree("")
        for item in InputProGen.keys():
                InputProGenRec[ncycle][item]=InputProGen[item].duplicate()
        root['SCRIPTS']['RunProfileGen']['baserunpg.py'].run();
    if lmtexch[0]==1:
	root['SCRIPTS']['assit']['lmtexch.py'].run()
    if root['SETTINGS']['PHYSICS']['irfshw']==1:
	OutputProGen['input.profiles']['omega0']=root['SETTINGS']['PHYSICS']['omega0']       
    OutputProGenRec[ncycle]=OutputProGen['input.profiles'].duplicate()
##-------------------------------------------
## tgyro part
##-------------------------------------------
##  update input file for tgyro
    InputTGYRO['input.profiles']=OutputProGen['input.profiles'].duplicate();
# the fusion power may needs to be scaled here since the fueling ions concentration is not identical for ONETWO and TGYRO 
#    root['SCRIPTS']['assit']['scalefus.py'].run()
# the ions density should also be changed from ONETWO to tgyro
# the density profile of He should be provided in the root['SETTINGS']['DEPENDENCIES']['He']
#    root['SETTINGS']['DEPENDENCIES']['He']=root['OUTPUTS']['ProfileGenOutput']['input.profiles']['ne']*root['SETTINGS']['PHYSICS']['ForDenFrac'][0]  #this is one method for specifying the Helium density, we can also use some other method for sure
#    root['SETTINGS']['TEMP']['ImpName']='He'
#    root['SCRIPTS']['assit']['distributeIonDen.py'].run()    
    if root['SETTINGS']['PHYSICS']['reconsImp']!='':
    # if the impurity(normally the W) profile needs to be calculated, then calculate the radiation in a seperated ONETWO run using getradiation.py and updateradiation for the input.profiles using updateradiation
    # we need to run the ONETWO again here to get the radiation profile and the radiation profile in TGYRO should be accordingly changed
        root['SCRIPTS']['assit']['getradiation.py'].run()
    # the radition power needs to be updated
        root['SCRIPTS']['assit']['updateradiation.py'].run()
# scale the source according to the physics requirement
    InputTGYRO['input.profiles']['flow_beam']=OutputProGen['input.profiles']['flow_beam']*physics['beamsrcscale'];
    InputTGYRO['input.profiles']['flow_mom']=OutputProGen['input.profiles']['flow_mom']*physics['beamtorqscale'];
# recover the Ar density if needed
    if root['SETTINGS']['TEMP'].has_key('n_ar'):
        InputTGYRO['input.profiles']['ni_4']=root['SETTINGS']['TEMP']['n_ar']
    InputTGYRO['input.profiles.geo']=OutputProGen['input.profiles.geo'];
##  note that the momentum flux profile is negative, the sign will be changed here
    if root['SETTINGS']['PHYSICS']['iabstorque']==1:
        InputTGYRO['input.profiles']['flow_mom']=abs(InputTGYRO['input.profiles']['flow_mom'])
    if root['SETTINGS']['PHYSICS']['imergeDT']==1:
        InputTGYRO['input.tgyro']['TGYRO_DT_METHOD']=2
        root['SCRIPTS']['assit']['mergeDT.py'].run()
    if root['SETTINGS']['PHYSICS']['ievoHe']==1:
        InputTGYRO['input.tgyro']['TGYRO_DT_METHOD']=2
        InputTGYRO['input.tgyro']['LOC_SCENARIO']=3
        InputTGYRO['input.tgyro']['TGYRO_DEN_METHOD0']=1
        InputTGYRO['input.tgyro']['TGYRO_DEN_METHOD1']=-1
        InputTGYRO['input.tgyro']['TGYRO_DEN_METHOD2']=2
        InputTGYRO['input.profiles']['pow_e']=InputTGYRO['input.profiles']['pow_e_aux']
        InputTGYRO['input.profiles']['pow_i']=InputTGYRO['input.profiles']['pow_i_aux']
        
# the sign of omega0 must be identical to the momentum
    InputTGYRO['input.profiles']['omega0']=sign(InputTGYRO['input.profiles']['flow_mom'][-1])*array([abs(item) for item in InputTGYRO['input.profiles']['omega0']])
# determine whether to use the hybrid q profile in the core region, it won't run by default
    root['SCRIPTS']['assit']['maphybridq.py'].run()
##  run tgyro
    if irun[3]==1:
   	if ainb(ncycle,itEr):
            if physics['iEstimateEr']==1:
                InputTGYRO['input.tgyro']['LOC_TE_FEEDBACK_FLAG']=iEvolChan[0]
                InputTGYRO['input.tgyro']['LOC_TI_FEEDBACK_FLAG']=iEvolChan[1]
                InputTGYRO['input.tgyro']['TGYRO_DEN_METHOD0']=iEvolChan[2]
		InputTGYRO['input.tgyro']['LOC_ER_FEEDBACK_FLAG']=iEvolChan[3]
#	root['INPUTSRec']['TGYRO'][ncycle]=root['INPUTS']['TGYROInput']	
        InputTGYRORec[ncycle]=OMFITtree("")
        for item in InputTGYRO.keys():
            InputTGYRORec[ncycle][item]=InputTGYRO[item].duplicate()
        root['SCRIPTS']['RunTGYRO']['baseruntgyro.py'].run();
    ##  record the TGYRO output
        root['OUTPUTSRec']['TGYROOutput'][ncycle]=OMFITtree("")
        for item in OutputTGYRO.keys():
            OutputTGYRORec[ncycle][item]=OutputTGYRO[item].duplicate()
    # treat the issues rest,mainly interp the profile and construct the profile to the ONETWO
        root['SCRIPTS']['assit']['cpltcyc.py'].run()
        if ainb(ncycle,itEr):
            root['SCRIPTS']['assit']['rcvtgyroswitch.py'].run()
    ncycle=ncycle+1;                # it should be the last command
