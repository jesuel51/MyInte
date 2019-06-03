#!/bin/bash

#pbsID=$(qsub /scratch/home/xiangjian/Documents/project/OMFIT-source/modules/ONETWO/FILES/job.pds)
pbsID=$(qsub jobgyro.pbs)
echo "GYRO_begins"
#echo $pbsID
echo "The job $pbsID is submitted..."
tt=$(qstat | grep "$pbsID")
sleep 1
while [ ${#tt} -gt 0 ] ; do
  echo "The job $pbsID is still running..."
  sleep 10
  tt=$(qstat | grep "$pbsID")
done

#echo "The job $pbsID is completed!"
echo "GYRO completed!!"
