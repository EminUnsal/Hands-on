# Podlar sirasiyla olusturulur. Ilk olarak silinirken en son olusturulan silinir
# Her podun kendi PersistensVolume vardir
# Service kisminda .spec.clusterIp=none denir. cunku bir cluster ip istemeyiz .uyg ulasmak istendiginde olusturulan podlardan birinin ip'sine yonlendiriliriz
# StatefulSet
**statefulset** konusuyla ilgili dosyalara buradan erişebilirsiniz.
***
StatefulSet objelerinin listelenmesi

```
$ kubectl get statefulset
```
***
StatefulSet objelerinin silinmesi

```
$ kubectl delete statefulset "statefulset_ismi"

Ör: kubectl delete statefulset my-statefulset
```
***