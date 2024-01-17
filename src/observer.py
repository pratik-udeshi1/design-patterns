class Subscriber:
    def __init__(self, name):
        self._name = name
        self._subscribed_channels = []

    def subscribe(self, channel):
        self._subscribed_channels.append(channel)
        channel.add_subscriber(self)

    def unsubscribe(self, channel):
        self._subscribed_channels.remove(channel)
        channel.remove_subscriber(self)

    def update(self, video):
        print(f"{self._name} received an update: New video '{video}' is uploaded!")


class YouTubeChannel:
    def __init__(self, name):
        self._name = name
        self._subscribers = []

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def upload_video(self, video):
        print(f"{self._name} uploaded a new video: '{video}'")
        self.notify_subscribers(video)

    def notify_subscribers(self, video):
        for subscriber in self._subscribers:
            subscriber.update(video)


# Client code
subscriber1 = Subscriber("Alice")
subscriber2 = Subscriber("Bob")
subscriber3 = Subscriber("Charlie")

channel1 = YouTubeChannel("Tech Talk")
channel2 = YouTubeChannel("Cooking Delights")

subscriber1.subscribe(channel1)
subscriber2.subscribe(channel1)
subscriber2.subscribe(channel2)
subscriber3.subscribe(channel2)

channel1.upload_video("Python Programming Basics")
channel2.upload_video("Delicious Pasta Recipe")

subscriber2.unsubscribe(channel1)

channel1.upload_video("Advanced Python Topics")
