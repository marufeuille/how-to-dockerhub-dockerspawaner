FROM jupyterhub/jupyterhub
RUN pip install dockerspawner && conda install jupyter_client
CMD ["jupyterhub"]
