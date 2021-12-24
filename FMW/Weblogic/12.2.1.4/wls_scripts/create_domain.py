#!/usr/bin/sh
mkdir -p /u01/oracle/domains/denemeDomain1/servers/AdminServer/security
echo "username=weblogic" >> /u01/oracle/domains/denemeDomain1/servers/AdminServer/security/boot.properties
echo "password=welcome1" >> /u01/oracle/domains/denemeDomain1/servers/AdminServer/security/boot.properties

nohup /u01/oracle/domains/denemeDomain1/bin/startWebLogic.sh &
nohup /u01/oracle/domains/denemeDomain1/bin/startNodeManager.sh &

sleep infinity 
