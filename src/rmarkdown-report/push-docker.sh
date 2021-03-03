# Tag and push the container to the $ACR_REGISTRY
sudo docker tag rmarkdown-report "$ACR_REGISTRY/rmarkdown-report:latest"
sudo docker push "$ACR_REGISTRY/rmarkdown-report:latest"