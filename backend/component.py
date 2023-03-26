import aws_cdk as cdk
from constructs import Construct

from backend.api.infrastructure import API
from backend.database.infrastructure import Database
from backend.hosting.infrastructure import Hosting


class Backend(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        database = Database(
            self,
            "FlashcardsDatabase",
        )
        api = API(
            self,
            "FlashcardsAPI",
            dynamodb_table_name=database.dynamodb_table.table_name,
        )
        hosting = Hosting(
            self,
            "FlashcardsHosting",
            api.api.url,
            self.region,
        )

        database.dynamodb_table.grant_read_write_data(
            api.get_user_flashcards_lambda)
        database.dynamodb_table.grant_read_write_data(api.put_flashcard_lambda)
        database.dynamodb_table.grant_read_write_data(
            api.delete_flashcard_lambda)

        self.api_endpoint = cdk.CfnOutput(
            self,
            "FlashcardsAPIEndpoint",
            value=api.api.url,
        )
