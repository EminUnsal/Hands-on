# FROM mcr.microsoft.com/java/jdk:8-zulu-alpine
# COPY /source /usr/src/uygulama
# WORKDIR /usr/src/uygulama
# RUN javac uygulama.java
# CMD ["java", "uygulama"]

# # docker cp javauygulama:/usr/src/uygulama . 
# # Daha sonra yeni bir image olusturdum .image boyutu kuculdu
# FROM mcr.microsoft.com/java/jre:8-zulu-alpine
# COPY /uygulama /uygulama
# WORKDIR /uygulama
# CMD ["java", "uygulama"]

#With Multi-Stage Build
FROM mcr.microsoft.com/java/jdk:8-zulu-alpine AS derleyici
COPY /source /usr/src/uygulama
WORKDIR /usr/src/uygulama
RUN javac uygulama.java

FROM mcr.microsoft.com/java/jre:8-zulu-alpine
WORKDIR /uygulama
COPY --from=derleyici /usr/src/uygulama .
# COPY --from=derleyici /usr/src/uygulama .   --from komutu multistage'e ozgu degildir --from=nginx:latest seklinde yazip herhangi bir Dockerfile'da kullanabiliriz
CMD ["java", "uygulama"]