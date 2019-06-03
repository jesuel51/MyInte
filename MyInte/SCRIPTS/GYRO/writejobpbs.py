# sometimes, when TOROIDAL_GRID is larger than the cores that we used, GYRO will not work well
# thus the jobgyro.pbs need to be produced again
TOROIDAL_GRID=root['INPUTS']['GYROInput']['input.gyro']['TOROIDAL_GRID']
jobfilepath=root['SETTINGS']['extpath']['jobgyrofile']
quen=root['SETTINGS']['SETUP']['quen']
if quen=='parallel11':
    jobfile=jobfilepath+'/jobgyro.pbs_parallel'
    nodes=root['SETTINGS']['SETUP']['nodes']
else:
    jobfile=jobfilepath+'/jobgyro.pbs'
    nodes=1
jobfile_temp=jobfilepath+'/jobgyro.pbs_temp'
F=open(jobfile)
F_temp=open(jobfile_temp,'w')
for line in F:
    #print(line)
    #print(isinstance(line,str))
    if line.find('nodes')!=-1:
#        print(line)
        line='#PBS -l nodes='+str(nodes)+':ppn='+str(int(ceil(TOROIDAL_GRID/nodes)))+'\n'
    if line.find('gyro -e')!=-1:
#        print(line)
	line='gyro -e . -n '+str(TOROIDAL_GRID)
    F_temp.write(line)
F.close()
F_temp.close()
# then change the jobpbs.file
root['INPUTS']['GYROInput']['subjob']['jobgyro.pbs']=OMFITpythonTask(jobfile_temp)
