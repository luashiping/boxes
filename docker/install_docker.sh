#!/bin/bash
## 参考链接：https://yq.aliyun.com/articles/666944
## 卸载旧的docker，如果搭建k8s，centos自带的docker会报错，因此最好使用官方最新的docker版本
yum remove docker \
           docker-client \
           docker-client-latest \
           docker-common \
           docker-latest \
           docker-latest-logrotate \
           docker-logrotate \
           docker-selinux \
           docker-engine-selinux \
           docker-engine

##
yum install -y yum-utils \
               device-mapper-persistent-data \
               lvm2

## 启用Docker源
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

## 安装docker-ce
yum install docker-ce -y