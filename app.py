#!/usr/bin/env python3
import os

import aws_cdk as cdk

from bric_a_brac_serverless.bric_a_brac_serverless_stack import BricABracServerlessStack

app = cdk.App()
BricABracServerlessStack(
    app,
    "BricABracServerlessStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
                        region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
