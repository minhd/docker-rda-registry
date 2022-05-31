FROM centos:7
MAINTAINER Minh Duc Nguyen <minh.nguyen@ardc.edu.au>

# repositories
RUN yum -y --setopt=tsflags=nodocs install epel-release && \
    rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

RUN yum clean all --enablerepo=*; yum -y update --disablerepo=epel

# httpd
RUN yum -y --setopt=tsflags=nodocs update && \
    yum -y --setopt=tsflags=nodocs install httpd curl wget && \
    yum clean all

# php and php development packages
RUN yum -y install php56w php56w-common php56w-mysql php56w-ldap php56w-xml php56w-mbstring php56w-bcmath php56w-pecl-xdebug && \
    yum clean all

# composer 2.2.x latest
RUN curl -o /usr/local/bin/composer https://getcomposer.org/download/latest-2.2.x/composer.phar && chmod +x /usr/local/bin/composer

# nodejs
RUN yum -y --setopt=tsflags=nodocs install nodejs npm && yum clean all
RUN npm install -g n
RUN n stable
RUN npm install -g yarn

# python and python development packages
RUN yum -y --setopt=tsflags=nodocs install https://repo.ius.io/ius-release-el7.rpm
RUN yum -y --setopt=tsflags=nodocs install python3 python3-pip python3-devel && yum clean all
RUN /usr/bin/pip3 install --upgrade pip 
RUN /usr/bin/pip3.6 install --upgrade pip

# git, mod_ssl and openssh
RUN yum -y --setopt=tsflags=nodocs install make git mod_ssl openssh

# solr-import-export-json tool
COPY src/solr-import-export-json /opt/solr-import-export-json
RUN cd /opt/solr-import-export-json && /usr/bin/python3 -m venv venv && venv/bin/pip3 install --upgrade pip && venv/bin/pip3 install -r requirements.txt
COPY conf/concepts.json /tmp/concepts.json
COPY bin/populate-concepts-collection.sh /bin/populate-concepts-collection.sh
RUN chmod +x /bin/populate-concepts-collection.sh

# pubsub
COPY src/pubsub /opt/apps/pubsub/current
RUN cd /opt/apps/pubsub/current/ && yarn install
COPY conf/.env.pubsub /opt/apps/pubsub/current/.env

# taskmanager
COPY src/taskmanager /opt/apps/taskmanager/current
RUN cd /opt/apps/taskmanager/current/ && rm -rf venv && rm -rf __pycache__ && /usr/bin/python3 -m venv venv && venv/bin/pip3 install --upgrade pip && venv/bin/pip3 install -r requirements.txt
RUN mkdir -p /var/log/taskmanager && mkdir -p /var/data/taskmanager
COPY conf/taskmanager-config.py /opt/apps/taskmanager/current/myconfig.py

# harvester
COPY src/harvester /opt/apps/harvester/current
RUN cd /opt/apps/harvester/current/ && rm -rf venv && rm -rf __pycache__ && /usr/bin/python3 -m venv venv && venv/bin/pip3 install --upgrade pip && venv/bin/pip3 install -r requirements.txt
RUN mkdir -p /var/data/harvester && setfacl -R -d -m apache:rwx /var/data/harvester && setfacl -R -m u:apache:rwx /var/data/harvester
RUN mkdir -p /var/log/harvester && mkdir -p /var/data/harvester
COPY conf/harvester-config.py /opt/apps/harvester/current/myconfig.py

# RDA Registry
COPY src/rda-registry /opt/apps/registry/current
RUN cd /opt/apps/registry/current/ && composer install -o
RUN mkdir -p /var/data/error && setfacl -R -d -m apache:rwx /var/data/error && setfacl -R -m u:apache:rwx /var/data/error
RUN mkdir -p /var/data/portal && setfacl -R -d -m apache:rwx /var/data/portal && setfacl -R -m u:apache:rwx /var/data/portal
RUN mkdir -p /var/data/activity && setfacl -R -d -m apache:rwx /var/data/activity && setfacl -R -m u:apache:rwx /var/data/activity
RUN mkdir -p /var/data/importer && setfacl -R -d -m apache:rwx /var/data/importer && setfacl -R -m u:apache:rwx /var/data/importer
RUN mkdir -p /var/data/registry && setfacl -R -d -m apache:rwx /var/data/registry && setfacl -R -m u:apache:rwx /var/data/registry
RUN mkdir -p /var/log/registry && setfacl -R -d -m apache:rwx /var/log/registry && setfacl -R -m u:apache:rwx /var/log/registry
COPY conf/rda-registry-vhost.conf /etc/httpd/conf.d/rda-registry-vhost.conf
COPY conf/.env.rda-registry /opt/apps/registry/current/.env
COPY conf/.htaccess /opt/apps/registry/current/.htaccess

# supervisor
RUN yum -y --setopt=tsflags=nodocs install supervisor
COPY conf/supervisord.conf /etc/supervisord.conf

# Force timezone to Australia/Sydney
RUN ln -sfn /usr/share/zoneinfo/Australia/Sydney /etc/localtime

# Set the Locale to prevent default being ASCII
ENV LANG en_US.UTF-8 
ENV LANGUAGE en_US:en 
ENV LC_ALL en_US.UTF-8

EXPOSE 80

RUN chown -R apache /var/data/registry
RUN chown -R apache /var/log/registry

CMD ["/usr/bin/supervisord"]