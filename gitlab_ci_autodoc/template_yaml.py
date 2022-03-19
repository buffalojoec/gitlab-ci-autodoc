import mdutils, re, yaml



class TemplateYaml:


    # --- Self


    def __init__(self, directory, yaml_file):

        self.directory = directory
        self.yaml_file = yaml_file
        self.yaml_object = yaml.safe_load(
            open(self.directory + self.yaml_file, 'r')
        )
        
        self.name = list(self.yaml_object.keys())[0]
        self.image = self.yaml_object[self.name]['image']
        
        self.description = self.parse_description()
        self.input_vars = self.extract_input_vars()
        self.output_vars = self.extract_output_vars()
        
        self.output_artifacts = []
        if 'artifacts' in self.yaml_object[self.name].keys() \
            and 'paths' in self.yaml_object[self.name]['artifacts'].keys():
            self.output_artifacts = self.yaml_object[self.name]['artifacts']['paths']


    # --- Util

    
    def parse_description(self):
        description = ""
        for line in open(self.directory + self.yaml_file, 'r').readlines():
            if re.search("^\s*\#\*\*", line):
                description += line.replace("#**", "").strip() + " "
            elif re.search("^[a-zA-Z0-9]", line):
                break
        return description.strip()


    def extract_input_vars(self):
        
        # First gather all the vars provided in the YAML under "variables"
        variables = []
        if 'variables' in self.yaml_object[self.name].keys():
            variables = list(self.yaml_object[self.name]['variables'].keys())

        evaluated_vars = set()
        initialized_vars = set()
        for line in self.yaml_object[self.name]['script']:

            # Gather all variables that were evaluated (with a "$")
            #       throughout the script section
            for match in re.findall(
                r'\$[a-zA-Z0-9\-_]{1,}',
                line
            ):
                evaluated_vars.add(
                    match.replace("$", "").strip()
                )

            # Also check to see if any vars have been intialized
            #       in the script section (ie. $TAG: TAG=)
            for match in re.findall(
                r'[a-zA-Z0-9\-_]{1,}\s*=',
                line
            ):
                initialized_vars.add(
                    match.replace("=", "").strip()
                )
        
        # Finally take the total evaluated variables minus the vars in
        #       the "variables" section minus the intialized vars
        # It also can't start with "CI_" (GitLab predefined vars)
        input_vars = []
        for v in evaluated_vars:
            if v not in variables and v not in initialized_vars and v[:3] != "CI_":
                input_vars.append(v)

        return input_vars


    def extract_output_vars(self):

        # Simply parse out any variables that get written to a ".env" file
        output_vars = set()
        for line in self.yaml_object[self.name]['script']:
            for match in re.findall(
                r'echo \"[a-zA-Z0-9\$=]{1,}\" >> [a-zA-Z0-9]{1,}\.env',
                line
            ):
                output_vars.add(
                    re.split(r'\=\s*\$',
                        match.split(">>")[0]
                            .replace("\"", "")
                            .replace("echo", "")
                    )[0].strip()
                )
        return list(output_vars)


    # --- Markdown

    
    def to_markdown(self):
        markdown = """# {}
""".format(self.name)
        markdown += """{}
___
""".format(self.description)
        markdown += """#### Input Variables:
```shell
"""
        for x in self.input_vars:
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
        markdown += """#### Base Image
```shell
{}
```
___
""".format(self.image)
        
        return markdown