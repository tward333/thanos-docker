#!/bin/bash

name=$RANDOM
url='http://localhost:9093/api/v1/alerts'

echo "firing up alert $name" 

# change url o
curl -XPOST $url -d "[{ 
	\"status\": \"firing\",
	\"labels\": {
		\"alertname\": \"$name\",
		\"service\": \"test-service\",
		\"severity\":\"pagetward\",
		\"instance\": \"$name.test.net\"
	},
	\"annotations\": {
		\"summary\": \"this alert is bullshit!\",
		\"description\": \"this alert is bullshit!\"
	},
	\"generatorURL\": \"http://prometheus.int.example.net/<generating_expression>\"
}]"

echo ""

echo "press enter to resolve alert"
read

echo "sending resolve"
curl -XPOST $url -d "[{ 
	\"status\": \"resolved\",
	\"labels\": {
		\"alertname\": \"$name\",
		\"service\": \"test-service\",
		\"severity\":\"log\",
		\"instance\": \"$name.test.net\"
	},
	\"annotations\": {
		\"summary\": \"this alert is bullshit!\",
		\"description\": \"this alert is bullshit!\"
	},
	\"generatorURL\": \"http://prometheus.int.example.net/<generating_expression>\"
}]"

echo ""
