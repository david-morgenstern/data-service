minikube start

cd fast_api
helm install fast-api ./fast-api-chart/fast-api-chart-0.1.0.tgz 

kubectl expose pod {podname} --type=NodePort 8080

