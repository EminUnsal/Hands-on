# Ingress
**ingress** konusuyla ilgili dosyalara buradan erişebilirsiniz.
***
https://kubernetes.github.io/ingress-nginx/deploy/
**IngressController uzerinde  ayarlamalar yapmak istersek Annotations bolumunde duzenleme yapabiliriz. Her IC gore icerikler gdegisiyor**
**Ingress objelerinin listelenmesi**

```
$ kubectl get ingress
```
***
Ingress objelerinin silinmesi

```
$ kubectl delete ingress "statefulset_ingress"

Ör: kubectl delete ingress my-ingress
```
***