#-*-Python-*-
# Created by xiangjian at 2015/05/04 16:20

#-*-Python-*-
# Created by xiangjian at 2015/05/03 15:02

# What are the input files

inputs=[(root['INPUTS']['TGYROInput']['input.profiles'],'input.profiles'),
        (root['INPUTS']['TGYROInput']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['TGYROInput']['input.tgyro'],'input.tgyro'),
        (root['INPUTS']['TGYROInput']['subjob']['monitePBStgyro.sh'],'monitePBStgyro.sh')
	]
for k in range(1,13):
    inputs.append((root['INPUTS']['TGYROInput']['inputtglf']['input.tglf'+str(k)],'input.tglf'+str(k)))
##----------------------
### output
##----------------------
outputs=['TGLF5/out.tglf.localdump']
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh'
#executable = 'pbsMonitor -cn 12 -exe tgyro_cfetr -e . -n 12'
executable ='chmod 777 monitePBStgyro.sh ; ./monitePBStgyro.sh;'
#executable =executable + 'pbsMonitor -jn 2 -cn 12 -exe tgyro_cfetr -e . -n 24'
executable =executable + 'pbsMonitor -cn 24 -exe tgyro -e . -n 24'
##executable += " > OMFITlog.txt ; "

#-----------------------
# Execute ONETWO
#-----------------------
ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable)
#ret_code=OMFITx.executable(root, inputs=inputs, outputs=outputs, executable=executable,clean='true')

#-----------------------
# load the results
#-----------------------
for item in outputs:
    root['OUTPUTS']['TGYROOutput'][item]=OMFITgaCode(item)
