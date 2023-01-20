FROM nginx:latest
LABEL maintainer="Mehmet Unsal @mehmetunsal"
ENV KULLANICI="mehmet"
ARG RENK
RUN apt-get update -y && apt-get install -y curl htop wget
WORKDIR /gecici
ADD https://wordpress.org/latest.tar.gz .
WORKDIR /usr/share/nginx/html
COPY html/${RENK} .
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost/ || exit 1
CMD rm index.html;sed -e s/KULLANICI/"$KULLANICI"/ temp.html > index1.html; sed -e s/HOSTNAME/"$HOSTNAME"/ index1.html > index.html ; nginx -g 'daemon off;'