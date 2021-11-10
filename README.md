full monitoring stack using docker to tie it all together

components:
```
prometheus - data ingress from multiple source types
thanos - prometheus downsampling + retention + HA using object storage
grafana - dashboards
alertmanager - push alert conditions to multiple channels with complex rules. Mostly useful for slack pings in the current form
webhook-logger - dumps webhook bodies into a txt file for situations where there's nowhere else to put it and to avoid clogging slack
	https://github.com/tomtom-international/alertmanager-webhook-logger
```


extras:
```
diagram -  python script to generate infra diagrams as code - https://github.com/mingrammer/diagrams
```

TODO:
* remake this using better public-facing examples
* rework alert webhook into something more useful, like a nagios alert
* better automated deployment
