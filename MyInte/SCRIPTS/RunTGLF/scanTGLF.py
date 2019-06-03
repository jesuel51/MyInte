# this script is used to do the stability analysis (linear mode) or transport analysis (nonlinear mode) for all the radius
# the relevant parameters are
# root['SETTINGS']['PLOTS']['iview'] determine which iteration index to analysis
# root['SETTINGS']['SETUP']['tglf_flag'] determine whether to run TGLF in linear mode or nonlinear mode
# Case linear: root['SETTINGS']['SETUP']['kyarr'], determine which kyrho are required to be calculated
# Case nonlinear: no parameter
# firstly, we want TGYRO to map the information of input.profile to input.tglf
iview=root['SETTINGS']['PLOTS']['iview']
for item in root['INPUTSRec']['TGYRO'][iview].keys():
    if item.find('input')!=-1:
        root['INPUTS']['TGYROInput'][item]=root['INPUTSRec']['TGYRO'][iview][item]
# execulate the TGYRO
inputs=[(root['INPUTS']['TGYROInput']['input.profiles'],'input.profiles'),
        (root['INPUTS']['TGYROInput']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['TGYROInput']['input.tgyro'],'input.tgyro'),
        (root['INPUTS']['TGYROInput']['subjob']['jobtgyro.pbs'],'jobtgyro.pbs'),
        (root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh'],'monitePBStgyro.sh')
	]
for k in range(1,13):
    inputs.append((root['INPUTS']['TGYROInput']['inputtglf']['input.tglf'+str(k)],'input.tglf'+str(k)))
# run TGYRO with 0 iteration to give input for TGLF
Iterations=root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RELAX_ITERATIONS']
root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RELAX_ITERATIONS']=0
##----------------------
### output
##----------------------
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
outputs=['out.tgyro.gyrobohm']
for k in range(1,p_tgyro+1):
#    root['INPUTS']['TGYROInput']['input.tgyro']['DIR']['TGLF'+str(k)]=1
    outputs.append('TGLF'+str(k)+'/out.tglf.localdump')
#print(outputs)    
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable ='chmod 777 monitePBStgyro.sh; ./monitePBStgyro.sh'
jobquene=root['SETTINGS']['SETUP']['jobquene']
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh ;'
#executable =executable + 'pbsMonitor  -jn 2 -cn 12 -exe tgyro_cfetr -e . -n 24'
executable =executable + 'pbsMonitor -jq '+jobquene+' -jn 2 -cn 12 -exe TGYRO_CFETR -e . -n 24'

ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
root['INPUTS']['TGYROInput']['input.tgyro']['TGYRO_RELAX_ITERATIONS']=Iterations
#-----------------------
# load the results for TGYRO to map the plasma background to the TGLF
#-----------------------
root['OUTPUTS']['TGYROOutput']['out.tgyro.gyrobohm']=OMFITasciitable('out.tgyro.gyrobohm')
for k in range(1,p_tgyro+1):
#    print(k)
    root['OUTPUTS']['TGYROOutput'][k]=OMFITgaCode(outputs[k])
# determine whether to do some scale to the out.tglf.localdump
if root['SETTINGS']['SETUP'].has_key('TGLFinputscale'):
    for key in root['SETTINGS']['SETUP']['TGLFinputscale']:
        if key in root['OUTPUTS']['TGYROOutput'][1].keys():
            print(key)
            for k in range(1,p_tgyro+1):
                root['OUTPUTS']['TGYROOutput'][k][key]=root['OUTPUTS']['TGYROOutput'][k][key]*root['SETTINGS']['SETUP']['TGLFinputscale'][key]
#---------------------------------------
#  start to run TGLF and store the resultse
# --------------------------------------
count=1
try:
    print root['OUTPUTS']['TGLFScan'].keys()
except:
    root['OUTPUTS']['TGLFScan']=OMFITtree()

kyarr=root['SETTINGS']['SETUP']['kyarr']
for k in range(1,p_tgyro+1):
    root['INPUTS']['TGLFInput']['input.tglf']=root['OUTPUTS']['TGYROOutput'][k]
    try:
        print(root['OUTPUTS']['TGLFScan'][k].keys())
    except:
        root['OUTPUTS']['TGLFScan'][k]=OMFITtree()
    if root['SETTINGS']['SETUP']['tglf_flag']=='nonlin':     # record the nonlinear result
        root['OUTPUTS']['TGLFScan'][k]['nonlin']=OMFITtree()
        root['SCRIPTS']['RunTGLF']['baserunTGLF.py'].run()
        for item in root['OUTPUTS']['TGLFOutput'].keys():
            root['OUTPUTS']['TGLFScan'][k]['nonlin'][item]=root['OUTPUTS']['TGLFOutput'][item]
    else:                                                   # record the linear result
        root['OUTPUTS']['TGLFScan'][k]['lin']=OMFITtree()
        root['OUTPUTS']['TGLFScan'][k]['lin']['input.tglf']=root['INPUTS']['TGLFInput']['input.tglf']
        for ky in kyarr:
            root['INPUTS']['TGLFInput']['input.tglf']['KY']=ky
            if ky not in root['OUTPUTS']['TGLFScan'][k]['lin'].keys():
                root['SCRIPTS']['RunTGLF']['baserunTGLF.py'].run()
                root['OUTPUTS']['TGLFScan'][k]['lin'][str(ky)[0:4]]=OMFITtree()
                for item in root['OUTPUTS']['TGLFOutput'].keys():
                    root['OUTPUTS']['TGLFScan'][k]['lin'][str(ky)[0:4]][item]=root['OUTPUTS']['TGLFOutput'][item]
            
