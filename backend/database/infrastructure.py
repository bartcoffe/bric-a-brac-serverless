import aws_cdk as cdk
import aws_cdk.aws_dynamodb as dynamodb
from constructs import Construct


class Database(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        partition_key = dynamodb.Attribute(name="user_id",
                                           type=dynamodb.AttributeType.STRING)
        sort_key = dynamodb.Attribute(name="id",
                                      type=dynamodb.AttributeType.STRING)
        self.dynamodb_table = dynamodb.Table(
            self,
            "DynamoDBTable",
            partition_key=partition_key,
            sort_key=sort_key,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )