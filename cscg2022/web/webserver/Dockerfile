FROM php:8.1-apache
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN apt-get update && apt-get upgrade -y

RUN cp /usr/local/etc/php/php.ini-production /usr/local/etc/php.ini && \
    sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/"     /usr/local/etc/php.ini && \
    sed -i 's/Listen 80/Listen 1024/' /etc/apache2/ports.conf

COPY src/ /var/www/html/
COPY flag /flag
RUN mv /flag /flag_$(tr -dc A-Za-z0-9 </dev/urandom | head -c 64)
RUN chmod 777 /flag*
RUN mkdir /var/www/html/uploads && chmod 777 -R /var/www/html/uploads
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf 

