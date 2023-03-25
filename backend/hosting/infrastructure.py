import aws_cdk.aws_amplify as amplify
from constructs import Construct

import os


class Hosting(Construct):

    def __init__(self, scope: Construct, construct_id: str, api_url: str,
                 region: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        amplify_app = amplify.CfnApp(
            self,
            'bric-a-brac',
            name="bric-a-brac",
            repository=os.getenv('GITHUB_REPOSITORY'),
            access_token=os.getenv('GITHUB_ACCESS_TOKEN'),
        )

        amplify_branch = amplify.CfnBranch(
            self,
            'main_branch',
            app_id=amplify_app.attr_app_id,
            branch_name="main",
            enable_auto_build=True,
            enable_performance_mode=False,
            enable_pull_request_preview=False,
            environment_variables=[
                amplify.CfnBranch.EnvironmentVariableProperty(name="ENDPOINT",
                                                              value=api_url),
                amplify.CfnBranch.EnvironmentVariableProperty(name="REGION",
                                                              value=region),
            ],
        )