


# test_deploy_template
This job template will deploy a jar to OpenShift.
___
#### Input Variables:
```shell

OPENSHIFT_REGION
OPENSHIFT_PROJECT
```
#### Output Variables:
```shell
TAG
```
#### Output Artifacts:
```shell

some_app.jar
```
___
#### Base Image
```shell
alpine:latest
```
___
# test_build_template
This job template will build with Kaniko.
___
#### Input Variables:
```shell
IMAGE_PATH
DOCKERFILE

```
#### Output Variables:
```shell
TAG
```
#### Output Artifacts:
```shell
```
___
#### Base Image
```shell

kaniko:latest
```
___
