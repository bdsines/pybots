from botbuilder.schema import *
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials

class ChannelHandler():
    def __init__(self):
        self.APP_ID = 'e10a38fb-829b-4ff7-9182-ab1f9f35fcb8'
        self.APP_PASSWORD = 'OxlPL279t?qROfYK0Yso_KKqBN_jqj?V'
        # self.SERVICE_URL = 'https://slack.botframework.com'
        self.SERVICE_URL = 'https://teams.microsoft.com'
        self.CHANNEL_ID = 'msteams'
        self.BOT_ID = '28:e10a38fb-829b-4ff7-9182-ab1f9f35fcb8'
        self.RECIPIENT_ID = 'dandab@schneider.com'

    def sendmessage(self):
        credentials = MicrosoftAppCredentials(self.APP_ID, self.APP_PASSWORD)
        connector = ConnectorClient(credentials, base_url=self.SERVICE_URL)
        conversation = connector.conversations.create_conversation(ConversationParameters(
            bot=ChannelAccount(id=self.BOT_ID),
            members=[ChannelAccount(id=self.RECIPIENT_ID)]))

        connector.conversations.send_to_conversation(conversation.id, Activity(
                    type=ActivityTypes.message,
                    channel_id=self.CHANNEL_ID,
                    recipient=ChannelAccount(id=self.RECIPIENT_ID),
                    from_property=ChannelAccount(id=self.BOT_ID),
                    text='Hello World!!!'))

