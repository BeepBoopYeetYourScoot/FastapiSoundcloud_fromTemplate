import soundcloud

# As per https://stackoverflow.com/questions/54753238/soundcloud-application-registration-form-is-closed
# Registering app is not required by Soundcloud
TOKEN = ...
client = soundcloud.client.Client(access_token=...)
