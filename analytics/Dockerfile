FROM docker.io/redhat/ubi8-minimal

#RUN microdnf install yum
#RUN yum -y install zip && yum -y clean all  && rm -rf /var/cache
#RUN yum -y install unzip && yum -y clean all  && rm -rf /var/cache
#RUN mkdir -p /u01/setups
RUN yum -y install wget
COPY analytics/setups/read.me /u01/setups/
WORKDIR /u01/setups
RUN wget https://drive.google.com/file/d/1A5yuRnfnKBXdEVfT5B2yd3jjdvlJbIuW/view?usp=sharing
