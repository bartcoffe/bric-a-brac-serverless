import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_apigateway as apigateway
from constructs import Construct


class API(Construct):

    def __init__(self, scope: Construct, construct_id: str,
                 dynamodb_table_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.get_flashcards_lambda = lambda_.Function(
            self,
            'API_handler',
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.from_asset('backend/api/runtime/get_flashcards'),
            handler='lambda_function.handler',
            environment={"DYNAMODB_TABLE_NAME": dynamodb_table_name},
        )
        self.api = apigateway.RestApi(self, "flashcarads-api")

        flashcards = self.api.root.add_resource('flashcards')
        flashcards.add_method(
            'GET',
            apigateway.LambdaIntegration(
                self.get_flashcards_lambda,
                #  request_templates={
                #      "application/json":
                #      '{ "statusCode": "200" }'}
            ))

        # flashcard = flashcards.add_resource('{flashcard_id}')
        # flashcard.add_method('POST')
        # flashcard.add_method('GET')
        # flashcard.add_method('PUT')
        # flashcard.add_method('DELETE')