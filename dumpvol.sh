#do the volume dump
date=$(date +%Y%m%d%H%M)
backupfile=grafana.$date.tar
docker run --rm --volumes-from grafana2 -v $(pwd):/backup ubuntu tar cvf /backup/$backupfile /var/lib/grafana/
#upload the dump to repo
#rsync -avP grafana*.tar root@192.168.5.1:/opt/docker/tmpstore
rclone copy $backupfile locals3:/deployblob/prometheus/


#copy prometheus data directly to repo
rclone copy  ./data/prometheus/other/ locals3:/deployblob/prometheus/data/

