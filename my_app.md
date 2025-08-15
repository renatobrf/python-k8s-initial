# access my app
ref: https://minikube.sigs.k8s.io/docs/handbook/accessing/
- kubectl get svc
- kubectl expose deployment python-k8s-initial --type=NodePort --port=8080
- minikube service python-k8s-initial --url
