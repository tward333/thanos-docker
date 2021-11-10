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
with Diagram("sysstat monitoring 2.0", show=False, direction="TB"):
    james =  User("James")
    tward =  User("tward")
    query = Thanos("querier")
    alert = Prometheus("Alertmanager")
    with Cluster("Data sources"):
        ceph_source = Rack("ceph")
        snmp_source = Rack("snmp")
        other_source = Rack("other")
        thanos_source = Thanos("selfmon")
    with Cluster("Prometheus ingest -- Retention 180d on local disk"):
        prometheus_ceph = Prometheus("ceph")
        prometheus_ceph_sc = Thanos("sidecar") 
        prometheus_ceph - prometheus_ceph_sc
        prometheus_snmp = Prometheus("snmp")
        prometheus_snmp_sc = Thanos("sidecar")
        prometheus_snmp - prometheus_snmp_sc
        prometheus_other = Prometheus("other")
        prometheus_other_sc = Thanos("sidecar")
        prometheus_other - prometheus_other_sc
        prometheus_selfmon = Prometheus("selfmon")
        prometheus_selfmon_sc = Thanos("sidecar")
        prometheus_selfmon - prometheus_selfmon_sc

    with Cluster("Front-end"):
        grafana = Grafana("grafana")
        #with Cluster(""):
        #    grafana = Grafana("grafana")
        #    grafana2 = Grafana("grafana-fallback")
        render = Grafana("grafrender")
        query_fe = Thanos("querier-frontend")
    with Cluster("Store gateway"):
        ceph_store = Thanos("ceph-store")
        snmp_store = Thanos("snmp-store")
        other_store = Thanos("other-store")
    with Cluster("Object storage"):
        bucket_ceph = SimpleStorageServiceS3Bucket("ceph")
        bucket_snmp = SimpleStorageServiceS3Bucket("snmp")
        bucket_other = SimpleStorageServiceS3Bucket("other")
    with Cluster("Compactors"):
        ceph_compact = Thanos("ceph-compactor")
        snmp_compact = Thanos("snmp-compactor")
        other_compact = Thanos("other-compactor")
        

##fronend
    james >> grafana
    james >> Edge(style="dashed", color="red") >> tward
    #grafana - Edge(style="dashed", color="red", label="manual failover", minlen="0.1") - grafana2
    query_fe >> query
    grafana - render
    #grafana2 - render
    grafana >> query_fe 
    #grafana2 >> Edge(color="red", style="dashed", taillabel="fallback targets", minlen="2" ) >> prometheus_ceph 
    #grafana2 >> Edge(color="red", style="dashed") >> prometheus_snmp 
    #grafana2 >> Edge(color="red", style="dashed") >> prometheus_other 
    grafana >> Edge(color="red", style="dashed", taillabel="fallback targets", minlen="2" ) >> prometheus_ceph 
    grafana >> Edge(color="red", style="dashed") >> prometheus_snmp 
    grafana >> Edge(color="red", style="dashed") >> prometheus_other 
    prometheus_selfmon_sc >> alert >> Edge(style="dashed", color="red", minlen="2", headlabel="slack #prometheus-alertmanager") >> tward
##ingest
    prometheus_ceph_sc >> Edge(color="darkgreen") >> bucket_ceph
    prometheus_snmp_sc >> Edge(color="darkgreen") >> bucket_snmp
    prometheus_other_sc >> Edge(color="darkgreen") >> bucket_other
    ceph_source >> prometheus_ceph 
    snmp_source >> prometheus_snmp
    other_source >> prometheus_other
    thanos_source >> prometheus_selfmon
##backend
    ceph_compact >> Edge(color="darkgreen") >> bucket_ceph
    snmp_compact >> Edge(color="darkgreen") >> bucket_snmp
    other_compact >> Edge(color="darkgreen") >> bucket_other
    ceph_store >> Edge(color="darkgreen") >> bucket_ceph
    snmp_store >> Edge(color="darkgreen") >> bucket_snmp
    other_store >> Edge(color="darkgreen") >> bucket_other
    query >> Edge(color="deepskyblue") >> ceph_store
    query >> Edge(color="deepskyblue") >> snmp_store
    query >> Edge(color="deepskyblue") >> other_store
    query >> Edge(color="deepskyblue") >> prometheus_ceph_sc 
    query >> Edge(color="deepskyblue") >> prometheus_snmp_sc 
    query >> Edge(color="deepskyblue") >> prometheus_other_sc 
    query >> Edge(color="deepskyblue") >> prometheus_selfmon_sc 

