#!/bin/bash

\cp /opt/astrialmon/bashrc /home/root/.bashrc
\cp /opt/astrialmon/bash_profile /home/root/.bash_profile
\cp /opt/astrialmon/bash_login /home/root/.bash_login


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

  # copy bin commands
  \cp -R /opt/astrialmon/bin $i/

  # remove non useful commands
  rm $i/bin/amon_client.py
  rm $i/bin/runme.sh

  # clone astrial_primer if needed
  if [ -d /opt/astrial_primer ]; then
     if [ -f $i/astrial_primer ]; then
        rm -rf $i/astrial_primer
     fi

     cp -r /opt/astrial_primer $i/
     chown -R $u:$u $i/astrial_primer
  fi

done
