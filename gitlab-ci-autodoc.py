import sys, re, os, yaml, mdutils


class DocYaml:
    def __init__(self, yaml_object):
        self.description = yaml_object['description']
        self.input_vars = yaml_object['input_vars']
        self.input_artifacts = yaml_object['input_artifacts']
        self.output_vars = yaml_object['output_vars']
        self.output_artifacts = yaml_object['output_artifacts']

    def to_markdown(self):
        markdown = """{}
___
""".format(self.description)
        markdown += """#### Input Variables:
```shell
"""
        for x in self.input_vars:
            markdown += """{}
""".format(x.strip())
        markdown += """```
#### Input Artifacts:
```shell
"""
        for x in self.input_artifacts:
            markdown += """{}
""".format(x.strip())
        markdown += """```
#### Output Variables:
```shell
"""
        for x in self.output_vars:
            markdown += """{}
""".format(x.strip())
        markdown += """```
#### Output Artifacts:
```shell
"""
        for x in self.output_artifacts:
            markdown += """{}
""".format(x.strip())
        markdown += """```
___
"""
        return markdown


class TemplateYaml:
    def __init__(self, yaml_object):
        self.name = list(yaml_object.keys())[0]
        self.image = yaml_object[self.name]['image']
        self.artifacts = yaml_object[self.name]['artifacts']
    
    def to_markdown(self):
        return """#### Base Image
```shell
{}
```
___
""".format(self.image)


if __name__ == "__main__":

    template_directory = sys.argv[1]
    print("Commencing auto-doc on directory: {}".format(template_directory))

    def yaml_only(x): return re.search("(.*.yml|.*.yaml)", x) 
    included_files = list(filter(yaml_only, os.listdir(template_directory)))

    if len(included_files) != 2: 
        print("\nError: You must include \"doc.yml\" and one other yaml file in the directory.")
        print("\nNo other yaml files are allowed.")
        exit(100)
    else:
        for inc_file in included_files:
            with open(template_directory + inc_file, 'r') as file: yaml_object = yaml.safe_load(file)
            if inc_file == "doc.yml":
                doc_yaml = DocYaml(yaml_object)
            else:
                template_yaml = TemplateYaml(yaml_object)
                
        mdFile = mdutils.MdUtils(
            file_name = template_directory + "doc.md",
            title = template_yaml.name)
        mdFile.write(doc_yaml.to_markdown())
        mdFile.write(template_yaml.to_markdown())
        mdFile.create_md_file()