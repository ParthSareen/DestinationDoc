from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC1df7f15bdc28b034b5305877e9db73d0'
auth_token = '8bf146a8c8d76cd51544c85ca9f49e92'
client = Client(account_sid, auth_token)
timeMinutes = 'five'
doctorNumber = '+16475265284'
call = client.calls.create(
                        url='http://twimlets.com/echo?Twiml=%3C%3Fxml%20version%3D%221.0%22%20encoding%3D%22UTF-8%22%3F%3E%0A%3CResponse%3E%0A%20%20%20%20%3CSay%20voice%20%3D%20%22alice%22%3EHello%20I%20represent%20a%20Destination%20Doc%20patient.%20I%20am%20on%20my%20way%20to%20your%20location%2C%20please%20book%20an%20appointment%20for%20earliest%20' + timeMinutes + '%20minutes.%20Thank%20you.%3C%2FSay%3E%0A%3C%2FResponse%3E&',
                        to= doctorNumber,
                        from_='+14388004097'
                    )

print(call.sid)
