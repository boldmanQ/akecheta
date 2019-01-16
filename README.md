# Akecheta

## What can i do

**Akecheta** is a platform to auto-deploy container applications in **kubernetes-cluster**
中文介绍：http://boldman.top/post/li-yong-k8s-pyclientbian-xie-rong-qi-zi-dong-hua-b/
## The basics
Use **Kubernetes** python client to create Resouces(Namespace、Secret、Configmap、Volume、Deployment or ohters controler、Service、Ingress).

The whole process of a server start up deploying and being able to be accessed can be done automatically through it.

## How
### Before
* container registry is health
* k8s-cluster api-master is health to access

### Use

* Run **akecheta**，
* Define settings by admin page. (the settings include applications-server info and container registry address. such root-domain、application env...)
* Post **Domain** and **Server** info to http://akecheta:80/, then akecheta can create k8s-resources all we need.

### Then
When you post the applicaiton-server name and access-domain to akecheta, it return a task-id and deploy status. You can get result by http://akecheta:80/task-id/


Finall, Success to automatic deploy！you can watch it by kubernets-dashboard or kubelet.
