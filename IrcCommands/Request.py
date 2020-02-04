#Called when pm'd with
#	!request
def run(user, msg, ircClient, conf, api, time):
    ircClient.msg(user, 'This is a test!')
    print(f'{time} Printed a test message for {user}.')