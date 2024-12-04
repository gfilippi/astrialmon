#!/bin/bash

if test -f /tmp/amon_lock; then
   own=`cat /tmp/amon_lock`
   echo "removing lock owned by: $own"
   rm -f /tmp/amon_lock
   echo "OK"
fi


