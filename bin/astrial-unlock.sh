#!/bin/bash

if test -f /tmp/amon_lock; then
   own=`cat /tmp/amon_lock`
   USR=`whoami`
   if [ $USR == $own ]; then
      echo "removing lock owned by: $own"
      rm -f /tmp/amon_lock
      echo "OK"
   else
      echo "[ERROR]lock owned by: $own"
   fi
else
   echo "Board hw is already unlocked."
fi


