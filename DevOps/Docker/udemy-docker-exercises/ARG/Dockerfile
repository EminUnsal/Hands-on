FROM ubuntu:latest
WORKDIR /gecici
# ENV PASSW=sdasd buna container icinde erisiriz
# Varsayilan olan bir deger de girilebilir-->VERSION=3.8.1
#ARG ile olusturulan degerler container icinden ulasilamaz.ENV ile farki budur
ARG VERSION            
ADD https://www.python.org/ftp/python/${VERSION}/Python-${VERSION}.tgz .
CMD ls -al