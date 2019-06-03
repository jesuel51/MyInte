# this script is used to setup the core and node for ONETWO run
filename=root['INPUTS']['ONETWOInput']['subjob']['job12.pbs'].filename
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
    elif item.find('onetwo_cfetr')!=-1:
        item='onetwo_cfetr -np '+str(ncore)
    fidd.write(item)
fidd.close()
