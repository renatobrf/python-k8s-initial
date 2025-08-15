# access my app
ref: https://minikube.sigs.k8s.io/docs/handbook/accessing/
- kubectl get svc
- kubectl expose deployment hello-minikube1 --type=NodePort --port=8080
- minikube service hello-minikube1 --url
