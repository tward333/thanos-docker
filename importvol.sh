latesttar=$(rclone ls locals3:/deployblob/prometheus/|tail -1|awk {'print $2'})
rclone copy locals3:/deployblob/prometheus/$latesttar .
#nuke existing vol -- optional
#docker volume rm prometheus_grafana-storage
#do the import
docker volume create prometheus_grafana-storage
#voltar=$(ls grafana*.tar)
#docker run --rm -v prometheus_grafana-storage:/data  -v $(pwd):/backup ubuntu bash -c "tar xvf /backup/$voltar -C /data --strip 3; chown -R 472.472 /data"

docker run --rm -v prometheus_grafana-storage:/data  -v $(pwd):/backup ubuntu bash -c "tar xvf /backup/$latesttar -C /data --strip 3; chown -R 472.472 /data"

#inspect the result -- optional
#docker run --rm -it -v prometheus_grafana-storage:/data1  -v prometheus_grafana-storage2:/data2  -v $(pwd):/backup ubuntu bash 

#pull down prometheus datadir directly
rclone copy locals3:/deployblob/prometheus/data/ ./data/prometheus/other/
~                                                                                
