#Called when pm'd with
#	!discord
def run(user, msg, ircClient, conf, api, time):
    ircClient.msg(user, 'The place to talk about the bot or just chat: https://discord.gg/TN43w3E')
    print(f'{time} Printed discord invite for {user}.')