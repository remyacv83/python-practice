from twilio.rest import TwilioRestClient
    # put your own credentials here
ACCOUNT_SID = 'ACf674bf5791e44bc6fbfe9d8bd5e4de95'
AUTH_TOKEN = '6a866f14e92d60e3685faf087c560617'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
                        to = '7146228330',
                        from_ = '9495652516',
                        body = 'text from python code'
                    )
