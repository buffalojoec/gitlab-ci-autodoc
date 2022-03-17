
test_deploy_template
====================
Deploy a Spring Boot jar to OpenShift
___
#### Input Variables:
```shell
OPENSHIFT_NAMESPACE
OPENSHIFT_SECRET

JAVA_JAR_NAME
```
#### Input Artifacts:
```shell
Java .jar application
```
#### Output Variables:
```shell

OPENSHIFT_ROUTE
HELM_DEPLOYMENT_VERSION
OSE_MANIFEST_FILE
```
#### Output Artifacts:
```shell
manifest.json
```
___
#### Base Image
```shell
alpine:latest
```
___
