# Bazi uygulamalar isini yapip kapanmasi gerekir.Replicaset,Deployment,StatefulSet,DeamonSet hepsinde silinen pod tekrar otomatik baslar.Deploy edilen uygulama yapmasi gerkli olan islemi belirli bir sayidan pod ile basariyla tamamlar ise podlar kapanir.basarili olmadan fail ederse o zaman job objesi podu yeniden baslatir
# Job ve CronJob
**job ve cronjob** konusuyla ilgili dosyalara buradan erişebilirsiniz.
***
Job objelerinin listelenmesi

```
$ kubectl get job
```
***
Job objelerinin silinmesi

```
$ kubectl delete job "job_ismi

Ör: kubectl delete job myjob
```
***
CronJob objelerinin listelenmesi

```
$ kubectl get cronjob
```
***
CronJob objelerinin silinmesi

```
$ kubectl delete cronjob "cronjob_ismi

Ör: kubectl delete cronjob mycronjob
```