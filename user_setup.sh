#!/bin/bash


for i in `find /home/ -wholename "/home/user??" -type d`;
do
  #echo $i

  u=`echo $i | awk -F/ '{print $NF}' `

  echo $u

  \cp /opt/astrialmon/bashrc $i/.bashrc
  \cp /opt/astrialmon/bash_profile $i/.bash_profile
  \cp /opt/astrialmon/bash_login $i/.bash_login

  chown -R $u:$u $i
  passwd -d $u
  
  chfn -f "testuser" $u

done
