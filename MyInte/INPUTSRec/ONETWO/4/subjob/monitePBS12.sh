#!/bin/bash

#pbsID=$(qsub /scratch/home/xiangjian/Documents/project/OMFIT-source/modules/ONETWO/FILES/job.pds)
#rm -r *
echo 'onetwo starts:'
pbsID=$(qsub job12.pbs)
echo $pbsID
echo "The job $pbsID is submitted..."
#echo "dangerous"
tt=$(qstat | grep "$pbsID")
sleep 1
while [ ${#tt} -gt 0 ] ; do
  echo "The job $pbsID is still running..."
  sleep 16
  tt=$(qstat | grep "$pbsID")
done

#echo "The job $pbsID is completed!"
echo "oentwo completed!"
