# Worker nodelardan loglari toplayan bir uygulamamiz var ve bu butun worker-node'larda calismasi gerekli ve merkezi bir log sunucuna
bu loglari  gonderiyor.Her node'da calismasini istedigimiz uygulamalar icin DaemonSet objesini kullaniriz
#Pod manuel silinse bile hemen pod'un silindigi node'da Control Plane bir pod tekrar olusturur

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
