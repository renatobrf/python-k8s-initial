# required files
- build.yaml
- .secrets.baseline
- deploy/env/application.yaml
- Java - pom.xml, server.xml
- Python - app.py, requirements.txt, pyproject.toml
- Go - main.go, go.mod, go.sum, Makefile, e2e.sh, goproject.yaml
- Node - package.json, scripts, unit-test, lint, e2e, start, compile

## build, push and pull req
- docker build -t renatobrf/python-k8s-initial .
- docker push renatobrf/python-k8s-initial
- docker pull renatobrf/python-k8s-initial

## apply the deployment
- kubectl apply -f deployment.yaml

## check the logs
- kubectl get pods
- kubectl logs <pod-name>
- kubectl describe pod <pod-name>
- kubectl label namespace default env=nonprod --overwrite

## steps
- kubectl create namespace nome
- sudo snap install helm --classic
- deploy 2 monitor operator and donwload de agent image
