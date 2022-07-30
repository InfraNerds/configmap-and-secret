[![Build](https://github.com/Thiagosnts/configmap-and-secret/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Thiagosnts/configmap-and-secret/actions/workflows/docker-image.yml)


#### Replace variables the configmap e secrets
`step codefresh`
[![Build](icon-3.svg)](https://github.com/Thiagosnts/configmap-and-secret/actions/workflows/docker-image.yml)

**Example de Pipeline:**

```yml
version: "1.0"
stages:
  - "Clone"

steps:
 
  Download_Templates:
    title: "Templates Kubernetes"
    type: "git-clone"
    repo: "${{k8s_templates}}" 
    revision: "master"
    git: "${{context}}"
    stage: "Clone"

  Replace_Config:
    stage: "Clone"
    title: Replace variables the configmap e secrets.
    type: atqipiranga/configmap-and-secret
    arguments:
      PATH_CONFIGMAP: ./k8s_templates/configmap.yml
      PATH_SECRET: ./k8s_templates/secret.yml
      CONFIGMAP:
        - 'url=http://example.com'
        - 'port=3000'
      SECRET:
        - 'user=user'
        - 'pass=pass'
  
  Show teplates:
     title: 'Define Environment'
     stage: "Clone"
     image: codefreshio/ci-helpers
     fail_fast: false
     commands:
     - cat ./k8s_templates/configmap.yml
     - cat ./k8s_templates/secret.yml

```

**Example Templates Required:**
ConfigMap
```json
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata":
    { "name": "${app_name}-configmap", "namespace": "${project_name}" },
  "data": {}
}
```

Secret
```json
{
  "apiVersion": "v1",
  "kind": "Secret",
  "metadata": { "name": "${app_name}-configmap", "namespace": "${project_name}" },
  "type": "Opaque",
  "stringData": {}
}
```


**Result:**
ConfigMap
```json
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata":
    { "name": "${app_name}-configmap", "namespace": "${project_name}" },
  "data": {"url":"http://example.com","port":"3000"
}
}
```
Secret
```json
{
  "apiVersion": "v1",
  "kind": "Secret",
  "metadata": { "name": "${app_name}-configmap", "namespace": "${project_name}" },
  "type": "Opaque",
  "stringData": {"user":"user","pass":"pass"}
}
```
