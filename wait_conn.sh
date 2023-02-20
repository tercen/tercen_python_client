#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

FAIL=0
PREV_FAIL=0


for TRY in {1 .. 60}
do
    exec 6<>/dev/tcp/$1/$2 || FAIL=$((FAIL+1))
    exec 6>&- # close output connection
    exec 6<&- # close input connection
    
    if (( FAIL > PREV_FAIL )); then
    	# No one is listening
        PREV_FAIL=$FAIL
        sleep 5
    else
        echo "Listen to $1:$2 successful"
        break
    fi
done
