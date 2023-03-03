### Worker Node(s)
|Protocol|Direction|Port Range|Purpose|Used By|
|---|---|---|---|---|
|TCP|Inbound|10250|Kubelet API|Self, Control plane|
|TCP|Inbound|30000-32767|NodePort Services†|All|
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
> ```
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
$ echo '{"exec-opts": ["native.cgroupdriver=systemd"]}' | sudo tee /etc/docker/daemon.json
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
$ sudo systemctl restart kubelet

# Get join Token
kubeadm token list | awk 'NR == 2 {print $1}'
$ sudo kubeadm join 172.31.3.109:6443 --token 1aiej0.kf0t4on7c7bm2hpa --discovery-token-ca-cert-hash sha256:0e2abfb56733665c0e6204217fef34be2a4f3c4b8d1ea44dff85666ddf722c02

##Get Discovery Token CA cert Hash
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
##Get API Server Advertise address
kubectl cluster-info | awk 'NR == 1 {print $7}'
##Join a new Kubernetes Worker Node a Cluster
sudo kubeadm join \
  <control-plane-host>:<control-plane-port> \
  --token <token> \
  --discovery-token-ca-cert-hash sha256:<hash>
$ kubectl get nodes -o wide