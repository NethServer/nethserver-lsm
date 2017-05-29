==============
nethserver-lsm
==============

This package configures LSM - Link Status Monitor.

When a new red interface is added:

- LSM is configured to execute a ping to a well-known remote IP address.
  If the link quality is not good enough, the system will fire ``wan-uplink-update`` event.

- collectd is configured to graph the content of ``/var/lib/lsm/status.rtt``

See also: 

- https://github.com/NethServer/lsm
- https://github.com/NethServer/nethserver-firewall-base

Database
========

Example: ::

  lsm=service
      status=disabled
