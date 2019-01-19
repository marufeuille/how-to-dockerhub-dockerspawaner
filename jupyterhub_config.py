# Use PAM Authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

# Set Hubs ip addr and port
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.port = 8000

# Use Docker Spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# Set use dockerimage
c.DockerSpawner.image = 'jupyter/scipy-notebook'
c.DockerSpawner.remove_containers = True

# Set use netowork name for container (docker network)
c.DockerSpawner.network_name = 'jupyterhub-network'

# Tell Hub Ip to Container  
c.DockerSpawner.hub_ip_connect = public_ips()[0]

# misc
c.Spawner.http_timeout = 30
c.Authenticator.admin_users = set()
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.delete_invalid_users = True
c.PAMAuthenticator.open_sessions = False
