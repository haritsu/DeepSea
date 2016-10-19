
begin:
  salt.state:
    - tgt: {{ salt['pillar.get']('master_minion') }}
    - sls: ceph.events.begin_prep

sync:
  salt.state:
    - tgt: '*'
    - sls: ceph.sync

mine_functions:
  salt.state:
    - tgt: '*'
    - sls: ceph.mine_functions

repo:
  salt.state:
    - tgt: '*'
    - sls: ceph.repo

common packages:
  salt.state:
    - tgt: '*'
    - sls: ceph.packages.common

updates:
  salt.state:
    - tgt: '*'
    - sls: ceph.updates

restart:
  salt.state:
    - tgt: '*'
    - sls: ceph.updates.restart

complete:
  salt.state:
    - tgt: {{ salt['pillar.get']('master_minion') }}
    - sls: ceph.events.complete_prep

