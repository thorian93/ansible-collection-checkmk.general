---
- hosts: My_site # Sitename
#  debugger: on_failed
#  connection: local

  roles:
  - tribe29.checkmk.agent
