import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_apigateway as apigateway
from constructs import Construct


class API(Construct):

    def __init__(self, scope: Construct, construct_id: str,
                 dynamodb_table_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.api = apigateway.RestApi(self, "flashcarads-api")
        flashcards = self.api.root.add_resource('flashcards')
        user_flashcards = flashcards.add_resource('{user_id}')
        flashcard = user_flashcards.add_resource('{flashcard_id}')

        self.get_user_flashcards_lambda = lambda_.Function(
            self,
            'get_user_flashcards',
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.from_asset(
                'backend/api/runtime/get_user_flashcards'),
            handler='lambda_function.handler',
            environment={"DYNAMODB_TABLE_NAME": dynamodb_table_name},
        )
        user_flashcards.add_method(
            'GET',
            apigateway.LambdaIntegration(
                self.get_user_flashcards_lambda
                #  request_templates={
                #      "application/json":
                #      '{ "statusCode": "200" }'}
            ))

        self.put_flashcard_lambda = lambda_.Function(
            self,
            'put_flashcard',
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.from_asset('backend/api/runtime/put_flashcard'),
            handler='lambda_function.handler',
            environment={"DYNAMODB_TABLE_NAME": dynamodb_table_name},
        )

        user_flashcards.add_method(
            'PUT',
            apigateway.LambdaIntegration(
                self.put_flashcard_lambda,
                #  request_templates={
                #      "application/json":
                #      '{ "statusCode": "200" }'}
            ))
