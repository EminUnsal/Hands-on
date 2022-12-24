Bir Uygulamamiz var ve butun worker-node'larda calismasi gerekli. 
Mesela worker nodelardan loglari toplayan bir uygulama vve merkezzi bir log sunucuna
bu loglari  gonderiyor
her node'da calismasini istedigimiz uygulamalar icin
Pod manuel silinse bile hemen pod'un silindigi node'da Control Plane bir pod tekrar olusturur

# DaemonSet
**daemonset** konusuyla ilgili dosyalara buradan erişebilirsiniz.
***
DaemonSet objelerinin listelenmesi

```
$ kubectl get daemonset
```
***
DaemonSet objelerinin silinmesi

```
$ kubectl delete daemonset "daemonset_ismi"

Ör: kubectl delete daemonset my-daemonset
```
***