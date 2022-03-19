import sys, re, os, yaml, mdutils
from .template_yaml import TemplateYaml


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
            with open(template_directory + inc_file, 'r') as file: 
                yaml_object = yaml.safe_load(file)
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