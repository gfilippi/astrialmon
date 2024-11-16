#!/bin/bash

if test -f /tmp/amon_lock; then
   echo "[ERROR] Hailo hw already locked by: "
   cat /tmp/amon_lock
else
   echo `whoami` > /tmp/amon_lock
fi


