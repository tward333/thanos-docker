#alertmanager
curl -X POST http://localhost:9093/-/reload
#prom snmp
curl -X POST http://localhost:9001/-/reload
#prom ceph
curl -X POST http://localhost:9002/-/reload
#prom other
curl -X POST http://localhost:9003/-/reload
#prom selfmon
curl -X POST http://localhost:9004/-/reload
