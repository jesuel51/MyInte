# this script is used to do the using TGYRO itself
# set the parameters
root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_MODE']=2
# here we can choose which iteration deserves to analysis,it should be more flexible
k=root['SETTINGS']['PLOTS']['iview']
root['INPUTS']['TGYROInput']['input.tgyro']=root['INPUTSRec']['TGYRO'][k]['input.tgyro']
root['INPUTS']['TGYROInput']['input.profiles']=root['INPUTSRec']['TGYRO'][k]['input.profiles']
try:
    root['INPUTS']['TGYROInput']['input.profiles.geo']=root['INPUTSRec']['TGYRO'][k]['input.profiles.geo']
    root['INPUTS']['TGYROInput']['subjob']['jobtgyro.pbs']=root['INPUTSRec']['TGYRO'][k]['jobtgyro.pbs']
    root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh']=root['INPUTSRec']['TGYRO'][k]['monitePBStgyro.sh']
except:
    print('Geometry information does not exist!')
# Run TGYRO in stability analysis mode
inputs=[(root['INPUTS']['TGYROInput']['input.profiles'],'input.profiles'),
        (root['INPUTS']['TGYROInput']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['TGYROInput']['input.tgyro'],'input.tgyro'),
        (root['INPUTS']['TGYROInput']['subjob']['jobtgyro.pbs'],'jobtgyro.pbs'),
        (root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh'],'monitePBStgyro.sh')
        ]
##----------------------
### output
##----------------------
outputs=['out.tgyro.wi_elec','out.tgyro.wi_ion',
	'out.tgyro.wr_elec','out.tgyro.wr_ion'
         ]
p_tgyro=len(root['INPUTS']['TGYROInput']['input.tgyro']['DIR'].keys())
for k in range(1,p_tgyro+1):
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
##executable = str(root['SETTINGS']['SETUP']['executable'])
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh'
##executable += " > OMFITlog.txt ; "

#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')

#-----------------------
# load the result
#-----------------------
root['OUTPUTS']['TGYROOutput']['spectrum']=OMFITtree()
for item in outputs[0:4]:
    root['OUTPUTS']['TGYROOutput']['spectrum'][item]=OMFITasciitable(item)
for k in range(1,p_tgyro+1):
    root['OUTPUTS']['TGYROOutput'][k]=OMFITgaCode(outputs[3+k])
