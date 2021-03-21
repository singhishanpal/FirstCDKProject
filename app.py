#!/usr/bin/env python3

from aws_cdk import core

from my_first_cdk_project.my_first_cdk_project_stack import MyFirstCdkProjectStack


app = core.App()
MyFirstCdkProjectStack(app, "my-first-cdk-project")
MyFirstCdkProjectStack(app, "my-first-cdk-project1")
MyFirstCdkProjectStack(app, "my-first-cdk-project2")
MyFirstCdkProjectStack(app, "my-first-cdk-project3")
MyFirstCdkProjectStack(app, "my-first-cdk-project4")
print("Working in the develop brannch")





app.synth()
