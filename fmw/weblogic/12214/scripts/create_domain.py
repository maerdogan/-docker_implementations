binarypath='/u01/oracle'
rdomain='/u01/oracle/domains/denemeDomain1'
username='weblogic'
passwd='welcome1'
port=7001

nmport=int(port)

readTemplate(binarypath+'/wlserver/common/templates/wls/wls.jar')
cd('Servers/AdminServer')
cmo.setListenAddress('localhost')
setOption('ServerStartMode','prod')
print 'listenport adımı'
set('ListenPort', nmport)

print 'listenport tamam'
create('AdminServer','SSL')

cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', nmport+1)
cd('/')

cd('Security/base_domain/User/'+username)
cmo.setPassword(passwd)
setOption('ServerStartMode','prod')
setOption('OverwriteDomain', 'true')
writeDomain(rdomain)
closeTemplate()
