# RBAC
**Role contains namespaces.Rolebinding subject kisminda rolun kime baglanacagi belirlenir** 

**Not: Cluster rolleri rolebinding ile kullanip sadece ns seviyesinde atama yapilabilir**

**ClusterRole contains cluster**

**ClusterRole is used for NonNamesaces objects like nodes**

ClusterRole 

*admin

*cluster-admin--> Bir kullaniciya cluster seviyesinde admin yetkisi vermek icin

*view--> Tum kaynaklarda okuma

*edit--> Tum kaynaklarda duzenleme

kubectl get rolebindings.rbac.authorization.k8s.io -n production