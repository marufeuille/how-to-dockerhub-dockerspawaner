# How to use Jupyterhub with DockerSpawner
## Contents
### Dockerfile
Official docker image [jupyterhub/jupyterhub](https://hub.docker.com/r/jupyterhub/jupyterhub/) is pure jupyter hub container image.

This image is ** Not ** contains DockerSpawner and jupyter_client.

This Docker file is installing dockerspwaner and jupyter_client.

### jupyterhub_config.py
May be almost minimal configuration.

For detail, see comments in py.

## Want to do
- data persistense
- use ldap authentication
- use docker-compose
