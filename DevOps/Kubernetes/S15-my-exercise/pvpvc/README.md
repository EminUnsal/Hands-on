# Eephemeral volume'ler Pod'un yasam suresi  boyunca datalari saklariz.(node icinde )EmptyDir,HostPath
# PV ise cluster disinda oldugu icin worker node bir problem olsa bile veriye ulasilabilir
# Persistent Volume ve Persistent Volume Claim
AccessModes ayni anda birden fazla pod'a baglanildiginda ne sekilde bir davranis gosterir
ReadWriteOnce | Okuma yazma-tek node |ReadOnlyMany | sadece okuma |ReadWriteMany | okuma yazma-birden fazla node
persistentVolumeReclaimPolicy | recycle(volume silinmez ama bilgiler silinir) | delete |retain(volume ve bilgiler silinmez)
**pv ve pvc** konusuyla ilgili dosyalara buradan erişebilirsiniz.

***
NFS Server 
```
$ docker volume create nfsvol 

$ docker network create --driver=bridge --subnet=10.255.255.0/24 --ip-range=10.255.255.0/24 --gateway=10.255.255.10 nfsnet

$ docker run -dit --privileged --restart unless-stopped -e SHARED_DIRECTORY=/data -v nfsvol:/data --network nfsnet -p 2049:2049 --name nfssrv ozgurozturknet/nfs:latest

```
***
Persistent Volume objelerinin listelenmesi

```
$ kubectl get pv
```
***
Persistent Volume objelerinin silinmesi

```
$ kubectl delete pv "pv_ismi

Ör: kubectl delete pv mypv
```
***
Persistent Volume Claim objelerinin listelenmesi

```
$ kubectl get pvc
```
***
Persistent Volume objelerinin silinmesi

```
$ kubectl delete pvc "pvc_ismi

Ör: kubectl delete pvc mypvc
```
***