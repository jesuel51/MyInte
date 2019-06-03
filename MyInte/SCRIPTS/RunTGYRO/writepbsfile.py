# this script is used to setup the core and node for ONETWO run
filename=root['INPUTS']['TGYROInput']['subjob']['jobtgyro.pbs'].filename
# read the parameters
nodes=root['SETTINGS']['SETUP']['nodes']
ncore=root['SETTINGS']['SETUP']['ncore']
ppn=int(ncore/nodes)
quen=root['SETTINGS']['SETUP']['quen']
# open file and write the file
fid=open(filename,'r+')
cmds=fid.readlines()
fid.close()
fidd=open(filename,'w+')
for item in cmds:
    if item.find('#PBS -q')!=-1:
	item = '#PBS -q '+quen+'\n'
    elif item.find('#PBS -l nodes')!=-1:
        item='#PBS -l nodes='+str(nodes)+':ppn='+str(ppn)+'\n'
    elif item.find('tgyro -e')!=-1:
        item='tgyro -e . -n '+str(ncore)
    fidd.write(item)
fidd.close()
# besides, the number of core for every TGLF run should be specified
p_tgyro=root['SETTINGS']['PHYSICS']['p_tgyro']
for item in range(1,p_tgyro+1):
    root['INPUTS']['TGYROInput']['input.tgyro']['DIR']['TGLF'+str(item)]=int(ncore/p_tgyro)
