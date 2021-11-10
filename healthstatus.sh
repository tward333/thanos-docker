
#success output is an empty string. Any other status means something is wrong
output=$(cd  /opt/docker/thanos-docker-compose && docker-compose ps|grep -v 'Up\|---\|Ports' )
file="/home/httpd/html/thanos_status.txt"

if [ -z "$output" ]
  then echo 'OK' > $file
  else echo 'something is down, check thanos status' > $file
fi





