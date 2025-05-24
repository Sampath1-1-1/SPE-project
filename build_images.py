import os

commands = [
    "docker build -t sampath333/middleware:latest /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/MiddleWare",
    "docker build -t sampath333/model-service:latest /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Model-service",
    "docker build -t sampath333/frontend:latest /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/frontend",
    "docker push sampath333/middleware:latest",
    "docker push sampath333/model-service:latest",
    "docker push sampath333/frontend:latest",

    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/mysql-secret.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/mysql.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/model-service.yaml",
    "kubectl apply -f /home/aaradhya-ghota/SoftwareProduction/Major_Project_spe/Backend/Kubernates/middleware.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/frontend.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/elasticsearch.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/kibana.yaml",
    "kubectl apply -f /home/sampathkumar/Desktop/Major_Project_spe/Major_Project_spe/Backend/Kubernates/logstash.yaml"
    ]

for cmd in commands:
    print(f"\nRunning: {cmd}")
    os.system(cmd)




/home/sampathkumar/Desktop/Major_Project_spe/ansible/playbooks/deploy.yml
/home/sampathkumar/Desktop/Major_Project_spe/ansible/roles/deploy_k8s/tasks/main.yml
/home/sampathkumar/Desktop/Major_Project_spe/ansible/roles/deploy_k8s/templates/manifests.j2
/home/sampathkumar/Desktop/Major_Project_spe/ansible/roles/deploy_k8s/vars/main.yml
/home/sampathkumar/Desktop/Major_Project_spe/ansible/deploy.yml
/home/sampathkumar/Desktop/Major_Project_spe/ansible/inventory.yml




/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/kubernetes/roles/deploy_k8s/tasks/main.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/kubernetes/roles/deploy_k8s/templates/manifests.j2
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/kubernetes/roles/deploy_k8s/vars/main.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/kubernetes/deploy.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/kubernetes/inventory.yml



/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/roles/docker-compose/tasks/main.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/roles/docker-compose/templates/docker-compose.j2
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/roles/docker-compose/templates/initsql.j2
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/roles/docker-compose/templates/logstash.conf..j2
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/roles/docker-compose/vars/main.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/deploy.yml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/ansible/Docker-compose/inventory.yml




/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/elasticsearch.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/frontend.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/kibana.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/logstash.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/middleware.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/model-service.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/mysql-secret.yaml
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Kubernates/mysql.yaml

/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/MiddleWare/app.py
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/MiddleWare/Dockerfile
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/MiddleWare/requirements.txt

/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Model-service/app.py
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Model-service/Dockerfile
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Model-service/feature_extraction.py
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Model-service/model.pkl
/home/sampathkumar/Desktop/Major_Project_spe (copy)/Backend/Model-service/requirements.txt



/home/sampathkumar/Desktop/Major_Project_spe (copy)/Jenkinsfile

/home/sampathkumar/Desktop/Major_Project_spe (copy)/tests/test_app.py

# /home/sampathkumar/Desktop/Major_Project_spe (copy)/frontend/src/utils/api.js


