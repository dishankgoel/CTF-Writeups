FROM mysql:8.0.27

COPY sql.sql /docker-entrypoint-initdb.d
RUN sed -i "s/thisisadummyvalue/$(tr -dc A-Za-z0-9 </dev/urandom | head -c 64)/g" /docker-entrypoint-initdb.d/sql.sql
ENV MYSQL_ROOT_PASSWORD=root MYSQL_USER=user MYSQL_PASSWORD=VerySafePassword1337 MYSQL_DATABASE=fileuploadplatform

