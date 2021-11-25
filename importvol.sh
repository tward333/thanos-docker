
#nuke existing vol -- optional
#docker volume rm prometheus_grafana-storage
#do the import
docker volume create prometheus_grafana-storage
voltar=$(ls grafana*.tar)
docker run --rm -v prometheus_grafana-storage:/data  -v $(pwd):/backup ubuntu bash -c "tar xvf /backup/$voltar -C /data --strip 3; chown -R 472.472 /data"

#inspect the result -- optional
#docker run --rm -it -v prometheus_grafana-storage:/data1  -v prometheus_grafana-storage2:/data2  -v $(pwd):/backup ubuntu bash 
