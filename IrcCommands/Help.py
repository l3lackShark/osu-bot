#Called when pm'd with
#	!help
def run(user, msg, ircClient, conf, api, time):
    ircClient.msg(user, 'WIP')
    print(f'{time} Printed command list for {user}.')