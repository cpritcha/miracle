# DeployR Dockerfile

# Mount Points
# /home/deployr/deployr/7.4.1/deployr/database  MongoDB 

FROM centos:7

RUN yum -y update; yum clean all; yum -y install wget libicu-devel psmisc gcc-c++ which epel-release
RUN yum -y install R-core R-core-devel

WORKDIR /opt/
RUN wget --no-cookies --no-check-certificate --header \
        "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" \
        "http://download.oracle.com/otn-pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz"; \
    tar xzf jdk-8u65-linux-x64.tar.gz; \
    alternatives --install /usr/bin/java java /opt/jdk1.8.0_65/bin/java 2; \
    alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_65/bin/jar 2; \
    alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_65/bin/javac 2; \
    alternatives --set jar /opt/jdk1.8.0_65/bin/jar; \
    alternatives --set javac /opt/jdk1.8.0_65/bin/javac; \
    rm -rf jdk-8u65-linux-x64.tar.gz

RUN wget https://github.com/deployr/deployr-rserve/releases/download/v7.4.1/deployrRserve_7.4.1.tar.gz; \
    R CMD INSTALL deployrRserve_7.4.1.tar.gz; \
    rm -rf deployrRserve_7.4.1.tar.gz
RUN adduser --uid 1000 deployr
USER deployr
WORKDIR /home/deployr/
RUN mkdir download; \
    wget http://deployr.revolutionanalytics.com/7.4.1/download/bundles/release/DeployR-Open-Linux-7.4.1.tar.gz -P download; \
    cd download && tar xzf DeployR-Open-Linux-7.4.1.tar.gz
ADD installDeployROpen.sh download/installFiles/
USER root
RUN chown deployr:deployr download/installFiles/installDeployROpen.sh && \
    mkdir -p /miracle/projects && \
    chown -R deployr:deployr /miracle
USER deployr
RUN cd download/installFiles/ && export JAVA_HOME=/opt/jdk1.8.0_65/ && chmod +x installDeployROpen.sh && sync && ./installDeployROpen.sh --no-ask --nolicense
ADD startAll.sh deployr/7.4.1/

USER root
# Hardwired Libraries for luxedemo -- can remove later
RUN R -e "install.packages(c('data.table','raster','rasterVis', 'sqldf', 'lattice', 'latticeExtra'), repos='https://cran.rstudio.com/')"
 
RUN chown deployr:deployr deployr/7.4.1/startAll.sh
USER deployr

RUN chmod +x deployr/7.4.1/startAll.sh && sync && ln -s /miracle/projects /home/deployr/deployr/7.4.1/deployr/external/data/public
RUN rm -rf download

EXPOSE 7400 7406

CMD ["/home/deployr/deployr/7.4.1/startAll.sh"]
