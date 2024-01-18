class Subscriber:
    def __init__(self, name):
        self.name = name
        self.subscribed_channels = []

    def subscribe(self, channel):
        self.subscribed_channels.append(channel)
        channel.add_subscriber(self)

    def unsubscribe(self, channel):
        if channel in self.subscribed_channels:
            self.subscribed_channels.remove(channel)
            channel.remove_subscriber(self)
        else:
            print(f"*** {self.name} is not a subscriber of {channel.name} channel! ***")

    def update(self, video):
        print(f"{self.name} received an update: New video '{video}' is uploaded!")


class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def upload_video(self, video):
        print(f"{self.name} uploaded a new video: '{video}'")
        self.notify_subscribers(video)

    def notify_subscribers(self, video):
        for subscriber in self.subscribers:
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
# Alice received an update: New video 'Python Programming Basics' is uploaded!
# Bob received an update: New video 'Python Programming Basics' is uploaded!

channel2.upload_video("Delicious Pasta Recipe")
# Bob received an update: New video 'Delicious Pasta Recipe' is uploaded!
# Charlie received an update: New video 'Delicious Pasta Recipe' is uploaded!

subscriber2.unsubscribe(channel1)
subscriber3.unsubscribe(channel1)
# *** Charlie is not a subscriber of Tech Talk channel! ***

channel1.upload_video("Advanced Python Topics")
# Alice received an update: New video 'Advanced Python Topics' is uploaded!
