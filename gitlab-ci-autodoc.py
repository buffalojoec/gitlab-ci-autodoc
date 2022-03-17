import sys, re, os, yaml, mdutils


class DocYaml:
    def __init__(self, yaml_object):
        self.description = yaml_object['description']
        self.input_vars = yaml_object['input_vars']
        self.input_artifacts = yaml_object['input_artifacts']
        self.output_vars = yaml_object['output_vars']
        self.output_artifacts = yaml_object['output_artifacts']

    def to_markdown_object(self):
        print("\nDOC.YML VALUES:\n")
        print("description: {}".format(self.description))
        print("input_vars: {}".format(self.input_vars))
        print("input_artifacts: {}".format(self.input_artifacts))
        print("output_vars: {}".format(self.output_vars))
        print("output_artifacts: {}".format(self.output_artifacts))
        print("\n")


class TemplateYaml:
    def __init__(self, yaml_object):
        self.name = list(yaml_object.keys())[0]
        self.image = yaml_object[self.name]['image']
        self.artifacts = yaml_object[self.name]['artifacts']
    
    def to_markdown_object(self):
        print("\nTEMPLATE YML VALUES:\n")
        print("name: {}".format(self.name))
        print("image: {}".format(self.image))
        print("artifacts: {}".format(self.artifacts))
        print("\n")


if __name__ == "__main__":

    template_directory = sys.argv[1]
    print("Commencing auto-doc on directory: {}".format(template_directory))

    def yaml_only(x): return re.search("(*.yml|*.yaml)", x) 
    included_files = os.listdir(template_directory)

    if len(included_files) != 2: 
        print("Error: You must include \"doc.yml\" and one other yaml file in the directory.")
        print("\nNo other yaml files are allowed.")
        exit(100)
    else:
        for inc_file in included_files:
            with open(template_directory + inc_file, 'r') as file: yaml_object = yaml.safe_load(file)
            if inc_file == "doc.yml":
                # Doc.yml vars and artifacts
                doc_yaml = DocYaml(yaml_object)
                doc_yaml.to_markdown_object()
            else:
                # Actual template job details
                template_yaml = TemplateYaml(yaml_object)
                template_yaml.to_markdown_object()
                
        mdFile = mdutils.MdUtils(
            file_name = template_directory + "doc.md",
            title = template_yaml.name)
        mdFile.create_md_file()