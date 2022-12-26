# Affinity bir podun nerede olusturulacagini belirtir.Pod'a gore bir tanim var.Su pod surada olussun deniyorsa node affinity
# Worker node'un uzerinden sadece su podlar calissin.Taint and Toleration.Taintli nodelari tolera etmek icin podlara toleration kismini ekleriz.Taint ve Toleration
***
Node'lara taint ekleme.
```
$ kubectl taint node "node_ismi" "anahtar=değer:eylem"

Ör: kubectl taint node minikube platform=production:NoSchedule
```
***
Node'lardan taint kaldırma.
```
$ kubectl taint node "node_ismi" "anahtar-"

Ör: kubectl taint node minikube platform-
```