# GitLab CI Auto-Doc

`gitlab-ci-autodoc.py` will automatically create documentation for a job template.

___

1. Create a subfolder for your template to live in. Say `sample/`.
2. Write your template and give it a name. Say `eample.yml`.
3. Write the template's requirements in `doc.yml` according to following schema:

```yaml
description: Description of your template
input_vars:
  - VAR_1
  - VAR_2
  - PATH_TO_ARTIFACT_1
input_artifacts:
  - Description of ARTIFACT_1
output_vars:
  - VAR_1
  - VAR_2
  - PATH_TO_ARTIFACT_1
output_artifacts:
  - Description of ARTIFACT_1
```