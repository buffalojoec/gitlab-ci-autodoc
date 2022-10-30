# GitLab CI Auto-Doc

`gitlab_ci_autodoc` will automatically create markdown documentation for a 
GitLab CI/CD job template written in YAML.
___
Launch via:
```shell
python3 -m gitlab_ci_autodoc "./sample/"
```
___
Each directory gets one markdown file, and it will contain documentation sections for
each YAML file detected in the directory.
```shell
--sample
  --example.yml
  --sample.yml
  --doc.md  -> created for both files
```
___
Input/output vars and artifacts are extracted from the YAML automatically.

To add a description to your YAML file, add a comment above your YAML code with the following syntax:
```yaml
#** This is a description.
#** You can write multiple lines and they
#** will be appended.
```
