import messagebird
#create instance of messagebird.client using API key
client=messagebird.Client("<your-api-key>")
try:
    msg=client.voice_message_create("+919712997761","Hey You,a little bird told me you wanted a call!",{"voice":"male"})
    print(msg.__dict__)
except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)