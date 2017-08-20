from pusher import Pusher

from homeGrown.settings import PUSHER_KEYS


class PusherAPI(object):
    """docstring for Pusher"""
    pusher = Pusher(
        app_id=PUSHER_KEYS['APP_ID'],
        key=PUSHER_KEYS['KEY'],
        secret=PUSHER_KEYS['SECRET'],
        cluster=PUSHER_KEYS['CLUSTER'],
        ssl=PUSHER_KEYS['SSL']
    )

    def trigger(self, channel, event, data):
        self.pusher.trigger(channel, event, data)

    def __init__(self):
        super(PusherAPI, self).__init__()
