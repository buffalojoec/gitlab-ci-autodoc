from gitlab_ci_autodoc import TemplateYaml
import mdutils, os, re, sys


# Let's extract the autodoc data automagically.
# When we're done, we'll clean up the markdown &
#   reach a decision on multiple files per directory


directory = sys.argv[1]

def yaml_only(x): return re.search("(.*.yml|.*.yaml)", x) 
yaml_files_detected = list(filter(yaml_only, os.listdir(directory)))

mdFile = mdutils.MdUtils(
    file_name = sys.argv[1] + "doc.md")

for yaml_file in yaml_files_detected:
    template_yaml = TemplateYaml(directory, yaml_file)
    mdFile.write(template_yaml.to_markdown())

mdFile.create_md_file()