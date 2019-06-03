#-*-Python-*-
# Created by xiangjian at 2015/05/04 16:20

#-*-Python-*-
# Created by xiangjian at 2015/05/03 15:02
## the cores you used should be equal to the toroidal_grid
root['SCRIPTS']['GYRO']['writejobpbs.py'].run()
# What are the input files
k=root['SETTINGS']['PLOTS']['iview']
#root['INPUTS']['GYROInput']['input.profiles']=root['INPUTSRec']['TGYRO'][k]['input.profiles']
#root['INPUTS']['GYROInput']['input.profiles.geo']=root['INPUTSRec']['TGYRO'][k]['input.profiles.geo']
inputs=[(root['INPUTS']['GYROInput']['input.profiles'],'input.profiles'),
        (root['INPUTS']['GYROInput']['input.profiles.geo'],'input.profiles.geo'),
        (root['INPUTS']['GYROInput']['input.gyro'],'input.gyro'),
        (root['INPUTS']['GYROInput']['subjob']['jobgyro.pbs'],'jobgyro.pbs'),
        (root['INPUTS']['GYROInput']['subjob']['monitePBSgyro.sh'],'monitePBSgyro.sh')
        ]
##----------------------
### output
##----------------------
outputs=['out.gyro.freq', 'out.gyro.run','out.gyro.units',
#       'out.gyro.gbflux','out.gyro.gbflux_i','out.gyro.gbflux_mom',
        'out.gyro.k_perp_squared','out.gyro.phase_space'
         ]
##executable = str(root['SETTINGS']['SETUP']['executable'])
#executable ='chmod 777 monitePBSgyro.sh ; ./monitePBSgyro.sh'
executable ='pbsMonitor -jq parallel11 -jn 2 -cn 8 -exe gyro -e . -n 16'
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
    root['OUTPUTS']['GYROOutput'][item]=OMFITasciitable(item)
#root['OUTPUTSRec']['GYROOutput'][k]=root['OUTPUTS']['GYROOutput']
