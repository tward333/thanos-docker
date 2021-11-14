#alertmanager
curl -X POST http://localhost:9093/-/reload
#prom oneoff
curl -X POST http://localhost:9003/-/reload
#prom selfmon
curl -X POST http://localhost:9004/-/reload
