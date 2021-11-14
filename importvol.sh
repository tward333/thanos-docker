
#nuke existing vol -- optional
docker volume rm prometheus_grafana-storage2
#do the import
docker volume create prometheus_grafana-storage2
voltar=$(ls grafana*.tar)
docker run --rm -v prometheus_grafana-storage2:/data  -v $(pwd):/backup ubuntu bash -c "tar xvf /backup/$voltar -C /data --strip 3"

#inspect the result -- optional
docker run --rm -it -v prometheus_grafana-storage:/data1  -v prometheus_grafana-storage2:/data2  -v $(pwd):/backup ubuntu bash 
