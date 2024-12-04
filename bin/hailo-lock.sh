#!/bin/bash

if test -f /tmp/amon_lock; then
   USR=`cat /tmp/amon_lock`
   echo
   echo "[ERROR] Hailo hw already locked by: $USR"
   echo
else
   echo `whoami` > /tmp/amon_lock
   echo "OK"
fi


