# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.generic.compute import Rack
from diagrams.generic.blank import Blank
from diagrams.onprem.client import User
from diagrams.onprem.monitoring import Prometheus
from diagrams.onprem.monitoring import Thanos
from diagrams.onprem.monitoring import Grafana
from diagrams.aws.storage import SimpleStorageServiceS3Bucket

graph_attr = {
    "splines": "line",
    "concentrate":"false",
}

#with Diagram("sysstat monitoring", show=False, graph_attr=graph_attr, direction="LR"):
with Diagram("sysstat monitoring 1.0", show=False, direction="TB"):
    james =  User("James")
    query = Thanos("querier")
    with Cluster("Data sources"):
        ceph_source = Rack("ceph")
        snmp_source = Rack("snmp")
        other_source = Rack("other")
    with Cluster("Prometheus ingest -- Retention 1d on local disk"):
        prometheus_ceph = Prometheus("ceph")
        prometheus_ceph_sc = Thanos("sidecar") 
        prometheus_ceph - prometheus_ceph_sc
        prometheus_snmp = Prometheus("snmp")
        prometheus_snmp_sc = Thanos("sidecar")
        prometheus_snmp - prometheus_snmp_sc
        prometheus_other = Prometheus("other")
        prometheus_other_sc = Thanos("sidecar")
        prometheus_other - prometheus_other_sc

    with Cluster("Front-end"):
        with Cluster(""):
            grafana = Grafana("grafana")
        render = Grafana("grafrender")
        query_fe = Thanos("querier-frontend")
    with Cluster("Store gateway"):
        every_store = Thanos("store")
    with Cluster("Object storage"):
        bucket_every = SimpleStorageServiceS3Bucket("everything")
    with Cluster("Compactors"):
        every_compact = Thanos("compactor")
        

##fronend
    james >> grafana
    query_fe >> query
    grafana - render
    grafana >> query_fe 
##ingest
    prometheus_ceph_sc >> Edge(color="darkgreen") >> bucket_every
    prometheus_snmp_sc >> Edge(color="darkgreen") >> bucket_every
    prometheus_other_sc >> Edge(color="darkgreen") >> bucket_every
    ceph_source >> prometheus_ceph 
    snmp_source >> prometheus_snmp
    other_source >> prometheus_other
##backend
    every_compact >> Edge(color="darkgreen") >> bucket_every
    every_store >> Edge(color="darkgreen") >> bucket_every
    query >> Edge(color="deepskyblue") >> every_store
    query >> Edge(color="deepskyblue") >> prometheus_ceph_sc 
    query >> Edge(color="deepskyblue") >> prometheus_snmp_sc 
    query >> Edge(color="deepskyblue") >> prometheus_other_sc 

