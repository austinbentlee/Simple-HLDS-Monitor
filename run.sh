#!/bin/ksh
export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/usr/X11R6/bin:/usr/local/bin:/usr/local/sbin"

host="192.168.1.105" #your HLDS server
ports="27015 27016 27017 27018 27019" #your HLDS server port(s)
email="youremail@example.com" #your email to receive alerts at. note you will have to set up the 'mail' program

for port in $ports; do
    python3 /home/austin/hl1monitoring/hl1monitor.py $host $port
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo $host $port offline | mail -s "CRITICAL: HLDS Host Offline" $email
    fi
done

exit $retVal
