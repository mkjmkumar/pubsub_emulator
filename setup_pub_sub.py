from google.cloud import pubsub_v1
import time
import os

os.environ["PUBSUB_EMULATOR_HOST"] = "localhost:8085"
time.sleep(20)

project_id = "mwpfin"
topic_name = "nyse"
subscription_name = "finackSub"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

topic = publisher.create_topic(topic_path)

print('Topic created: {}'.format(topic))

subscriber = pubsub_v1.SubscriberClient()
topic_path = subscriber.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

subscription = subscriber.create_subscription(
        subscription_path, topic_path)

print('Subscription created: {}'.format(subscription))

for n in range(1, 10):
    data = u'Message number {}'.format(n)
    # Data must be a bytestring
    data = data.encode('utf-8')
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data)
    print('Published {} of message ID {}.'.format(data, future.result()))

print('Published messages.')

