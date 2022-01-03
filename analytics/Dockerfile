FROM docker.io/redhat/ubi8-minimal

RUN microdnf install yum
RUN yum -y install zip && yum -y clean all  && rm -rf /var/cache
RUN yum -y install unzip && yum -y clean all  && rm -rf /var/cache
RUN mkdir -p /u01/setups
RUN yum -y install wget
COPY analytics/setups/* /u01/setups/
WORKDIR /u01/setups
RUN chmod 755 /u01/setups/run.sh
#RUN /bin/sh /u01/setups/run.sh
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
#RUN unzip fmw_12.2.1.4.0_infrastructure.jar.part01.rar
#RUN wget https://doc-0o-ag-docs.googleusercontent.com/docs/securesc/d0mlh4eon85sohlq0h6hlblades9qfll/v4jjbsfap5a95rr6912odk0gmbv9lhej/1641237225000/15694112088232936265/15694112088232936265/1A5yuRnfnKBXdEVfT5B2yd3jjdvlJbIuW?e=download&authuser=0&nonce=l0k5i5os4ogt0&user=15694112088232936265&hash=u74it52qbg774jem2cigrejo5chdm1sn
