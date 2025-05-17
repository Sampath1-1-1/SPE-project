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