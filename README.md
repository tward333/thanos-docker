full monitoring stack using docker to tie it all together

BRANCH INFO - this is a cut-down version without thanos, for very small deployments

components:
```
prometheus - data ingress from multiple source types
grafana - dashboards
alertmanager - push alert conditions to multiple channels with complex rules. Mostly useful for slack pings in the current form
```


extras:
```
diagram -  python script to generate infra diagrams as code - https://github.com/mingrammer/diagrams
```

TODO:
* update diagram for this branch
* better automated template deployment
