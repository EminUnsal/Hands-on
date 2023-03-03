### Control-plane (Master) Node(s)
|Protocol|Direction|Port Range|Purpose|Used By|
|---|---|---|---|---|
|TCP|Inbound|6443|Kubernetes API server|All|
|TCP|Inbound|2379-2380|`etcd` server client API|kube-apiserver, etcd|
|TCP|Inbound|10250|Kubelet API|Self, Control plane|
|TCP|Inbound|10259|kube-scheduler|Self|
|TCP|Inbound|10257|kube-controller-manager|Self|
|TCP|Inbound|22|remote access with ssh|Self|
|UDP|Inbound|8472|Cluster-Wide Network Comm. - Flannel VXLAN|Self|
> **Ignore this section for AWS instances. But, it must be applied for real servers/workstations.**
> - Find the line in `/etc/fstab` referring to swap, and comment out it as following.
> ```bash
> # Swap a usb extern (3.7 GB):
> #/dev/sdb1 none swap sw 0 0
> or,
> - Disable swap from command line
> ```bash
> free -m
> sudo swapoff -a && sudo sed -i '/ swap / s/^/#/' /etc/fstab #A swap file is a system file that creates temporary storage space on a solid-state drive or hard disk when the system runs low on memory. The file swaps a section of RAM storage from an idle program and frees up memory for other programs.
- Hostname change of the nodes, so we can discern the roles of each nodes. For example, you can name the nodes (instances) like `kube-master, kube-worker-1`
$ sudo hostnamectl set-hostname <node-name-master-or-worker>
- Install helper packages for Kubernetes.
$ sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
- Update app repository and install Kubernetes packages and Docker.
$ sudo apt-get update -q
$ sudo apt-get install -qy kubelet=1.23.5-00 kubectl=1.25.6-00 kubeadm=1.23.5-00 docker.io
- Start and enable Docker service.
$ sudo systemctl start docker
$ sudo systemctl enable docker
- Add the current user to the `Docker group`, so that the `Docker commands` can be run without `sudo`.
$ sudo usermod -aG docker $USER
$ newgrp docker
- As a requirement, update the `iptables` of Linux Nodes to enable them to see bridged traffic correctly. Thus, you should ensure `net.bridge.bridge-nf-call-iptables` is set to `1` in your `sysctl` config and activate `iptables` immediately.
$ cat << EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
$ sudo sysctl --system
## Part 2 - Setting Up Master Node for Kubernetes
- Pull the packages for Kubernetes beforehand
$ sudo kubeadm config images pull
- By default, the Kubernetes cgroup driver is set to system, but docker is set to systemd. We need to change the Docker cgroup driver by creating a configuration file `/etc/docker/daemon.json` and adding the following line then restart deamon, docker and kubelet:
$ echo '{"exec-opts": ["native.cgroupdriver=systemd"]}' | sudo tee /etc/docker/daemon.json
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
$ sudo systemctl restart kubelet
- Let `kubeadm` prepare the environment for you. Note: Do not forget to change `<ec2-private-ip>` with your master node private IP.
$ sudo kubeadm init --apiserver-advertise-address=172.31.19.154 --pod-network-cidr=10.244.0.0/16
> :warning: **Note**: If you are working on `t2.micro` or `t2.small` instances,  use the command with `--ignore-preflight-errors=NumCPU` as shown below to ignore the errors.
###################################################
####################################################
 $ sudo kubeadm init --apiserver-advertise-address=<ec2 private ip> --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=NumCPU
> **Note**: There are a bunch of pod network providers and some of them use pre-defined `--pod-network-cidr` block. Check the documentation at the References part. We will use Flannel for pod network and Flannel uses 10.244.0.0/16 CIDR block. 

- In case of problems, use following command to reset the initialization and restart from Part 2 (Setting Up Master Node for Kubernetes).
$ sudo kubeadm reset
####################################################
####################################################
Your Kubernetes control-plane has initialized successfully!
$ kubeadm join 172.31.3.109:6443 --token 1aiej0.kf0t4on7c7bm2hpa --discovery-token-ca-cert-hash sha256:0e2abfb56733665c0e6204217fef34be2a4f3c4b8d1ea44dff85666ddf722c02
> Note to the Instructor: Note down the `kubeadm join ...` part in order to connect your worker nodes to the master node. Remember to run this command with `sudo`.
- Run following commands to set up local `kubeconfig` on master node.
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
- Activate the `Flannel` pod networking and explain briefly the about network add-ons on `https://kubernetes.io/docs/concepts/cluster-administration/addons/`.
$ kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
* Network trafigi olusutrmak icin flannel kullaniyoruz
- Master node (also named as Control Plane) should be ready, show existing pods created by user. Since we haven't created any pods, list should be empty.
$ kubectl get nodes
- Show the list of the pods created for Kubernetes service itself. Note that pods of Kubernetes service are running on the master node.
$ kubectl get pods -n kube-system
- Show the details of pods in `kube-system` namespace. Note that pods of Kubernetes service are running on the master node.
kubectl get pods -n kube-system -o wide
- Get the services available. Since we haven't created any services yet, we should see only Kubernetes service.
$ kubectl get services
$ kubectl api-resources
## Part 4 - Deploying a Simple Nginx Server on Kubernetes
$ kubectl get nodes
$ kubectl get pods
$ kubectl get pods -o wide --all-namespaces
$ kubectl run nginx-server --image=nginx  --port=80
- Get the list of pods in default namespace on master and check the status and readyness of `nginx-server`
$ kubectl get pods -o wide
- Expose the nginx-server pod as a new Kubernetes service on master.
$ kubectl expose pod nginx-server --port=80 --type=NodePort
- Get the list of services and show the newly created service of `nginx-server`
$ kubectl get service -o wide
$ kubectl delete service nginx-server
$ kubectl delete pods nginx-server

- To delete a worker/slave node from the cluster, follow the below steps.
$ kubectl cordon kube-worker-1
$ kubectl drain kube-worker-1 --ignore-daemonsets --delete-emptydir-data
$ kubectl delete node kube-worker-1
---------
- Remove and reset settings on the worker node.
$ sudo kubeadm reset
- Note: If you try to have worker rejoin cluster, it might be necessary to clean `kubelet.conf` and `ca.crt` files and free the port `10250`, before rejoining.
>  sudo rm /etc/kubernetes/kubelet.conf
>  sudo rm /etc/kubernetes/pki/ca.crt
>  sudo netstat -lnp | grep 10250
>  sudo kill <process-id>
