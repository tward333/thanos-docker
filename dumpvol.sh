#do the dump
date=$(date +%Y%m%d%H%M)
docker run --rm --volumes-from grafana2 -v $(pwd):/backup ubuntu tar cvf /backup/grafana.$date.tar /var/lib/grafana/
#upload the dump to repo
#rsync -avP grafana*.tar root@192.168.5.1:/opt/docker/tmpstore
