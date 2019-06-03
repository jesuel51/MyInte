# What are the input files
inputtgyro=root['INPUTS']['TGYROInput']
inputs=[(inputtgyro['input.profiles'],'input.profiles'),
        (inputtgyro['input.profiles.geo'],'input.profiles.geo'),
        (inputtgyro['input.tgyro'],'input.tgyro'),
#        (root['INPUTS']['TGYROInput']['subjob']['jobtgyro.pbs'],'jobtgyro.pbs'),
        (inputtgyro['subjob']['monitePBStgyro.sh'],'monitePBStgyro.sh')
	]
ptgyro=len(inputtgyro['input.tgyro']['DIR'])
for k in range(1,ptgyro+1):
    inputs.append((inputtgyro['inputtglf']['input.tglf'+str(k)],'input.tglf'+str(k)))
##----------------------
### output
##----------------------
#outputs=['out.tgyro.alpha',
#         'out.tgyro.flux_e','out.tgyro.flux_i','out.tgyro.flux_i2','out.tgyro.flux_i3','out.tgyro.flux_target',
#         'out.tgyro.power_e','out.tgyro.power_i',
#         'out.tgyro.profile','out.tgyro.profile2','out.tgyro.profile3',
#	 'out.tgyro.mflux_e','out.tgyro.mflux_i','out.tgyro.mflux_i2','out.tgyro.mflux_i3',
#	 'out.tgyro.gyrobohm','out.tgyro.gradient',
#	 'out.tgyro.geometry.1','out.tgyro.nu_rho',
#         'out.tgyro.residual','out.tgyro.control',
#	 'out.tgyro.geometry.2','out.tgyro.run',
#	 'input.profiles.gen','input.tgyro.gen'
#         ]
outputs=['out.tgyro.alpha',
         'out.tgyro.flux_e','out.tgyro.flux_i1',
         'out.tgyro.evo_ne','out.tgyro.evo_te','out.tgyro.evo_ti','out.tgyro.evo_er',
         'out.tgyro.evo_n1',
         'out.tgyro.power_e','out.tgyro.power_i',
         'out.tgyro.profile','out.tgyro.profile_e','out.tgyro.profile_i1',
         'out.tgyro.mflux_e','out.tgyro.mflux_i',
         'out.tgyro.gyrobohm','out.tgyro.gradient',
         'out.tgyro.geometry.1','out.tgyro.nu_rho',
         'out.tgyro.residual','out.tgyro.control',
         'out.tgyro.geometry.2','out.tgyro.run',
         'input.profiles.gen','input.tgyro.gen'
         ]
n_ion=inputtgyro['input.tgyro']['LOC_N_ION']
if n_ion>1:
    for k in range(2,n_ion+1):
        outputs.append('out.tgyro.flux_i'+str(k))
        outputs.append('out.tgyro.profile_i'+str(k))
        outputs.append('out.tgyro.mflux_i'+str(k))
        outputs.append('out.tgyro.evo_n'+str(k))
    
for k in range(1,ptgyro+1):
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
for k in range(1,ptgyro+1):
    outputs.append('TGLF'+str(k)+'/out.neo.localdump')
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh'
#executable = 'pbsMonitor -cn 12 -exe tgyro_cfetr -e . -n 12'
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh;'
###################
## here, we the cores to be used are calculated and may varied 
#np_tgyro=len(root['INPUTS']['TGYROInput']['input.tgyro']['DIR'].keys())
#np_tglf=root['INPUTS']['TGYROInput']['input.tgyro']['DIR']['TGLF1']
#jobquene=root['SETTINGS']['SETUP']['jobquene']
#n_core=np_tgyro*np_tglf
#ncore_pnode=24.
#nnode=ceil(n_core/ncore_pnode)
#executable =executable + 'pbsMonitor -jq '+jobquene+' -jn '+str(nnode)+' -cn '+str(int(ncore_pnode))+' -exe tgyro -e . -n '+str(n_core)
## keep the cores in tglf running consistent the settings namelist
# note that the core used in TGYRO calculation is 2 times the ONETWO calculation
nodes=root['SETTINGS']['SETUP']['nodes']
ncore=root['SETTINGS']['SETUP']['ncore']
jobquene=root['SETTINGS']['SETUP']['jobquene']
executable =executable + ' pbsMonitor -jq '+jobquene+' -jn '+str(nodes)+' -cn '+str(ncore)+' -exe tgyro -e . -n '+str(ncore*nodes)
##executable += " > OMFITlog.txt ; "

#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')

#-----------------------
# load the results
#----------------------
for item in outputs[0:-ptgyro*2]:
    root['OUTPUTS']['TGYROOutput'][item]=OMFITasciitable(item)
count=1
for item in outputs[-ptgyro*2:-ptgyro]:
    root['OUTPUTS']['TGYROOutput']['out.tglf.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
count=1
for item in outputs[-ptgyro:]:
    root['OUTPUTS']['TGYROOutput']['out.neo.localdump_'+str(count)]=OMFITgaCode(item)
    count=count+1
