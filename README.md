# python-k8s-initial

## build and push
- docker build -t renatobrf/python-k8s-initial .
- docker push renatobrf/python-k8s-initial

## apply the deployment
- kubectl apply -f deployment.yaml

## check the logs
- kubectl get pods
- kubectl logs <pod-name>
