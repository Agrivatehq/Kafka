- Install Java
```
sudo apt update
sudo apt install default-jdk
```

- Download Apache Kafaka

```wget http://www-us.apache.org/dist/kafka/2.4.0/kafka_2.13-2.4.0.tgz
```

- Extract and Move it
```
tar xzf kafka_2.13-2.4.0.tgz
mv kafka_2.13-2.4.0 /usr/local/kafka
```

- Setup Kafka Systemd Unit Files


Next, create systemd unit files for the Zookeeper and Kafka service. This will help to manage Kafka services to start/stop using the systemctl command.

First, create systemd unit file for Zookeeper with below command:

```vim /etc/systemd/system/zookeeper.service
```

> Add the following code to the zookeeper.service

```
[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
ExecStart=/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties
ExecStop=/usr/local/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

> Next, to create a Kafka systemd unit file using the following command:

```
vim /etc/systemd/system/kafka.service
```

Add the following code to kafka.service.
Add the below content. Make sure to set the correct JAVA_HOME path as per the Java installed on your system.

```
[Unit]
Description=Apache Kafka Server
Documentation=http://kafka.apache.org/documentation.html
Requires=zookeeper.service

[Service]
Type=simple
Environment="JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64"
ExecStart=/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties
ExecStop=/usr/local/kafka/bin/kafka-server-stop.sh

[Install]
WantedBy=multi-user.target
```

- Reload the systemd daemon to apply new changes.

```
systemctl daemon-reload
```

- Start the Kafka server

Kafka required ZooKeeper so first, start a ZooKeeper server on your system. You can use the script available with Kafka to get start a single-node ZooKeeper instance.

```
sudo systemctl start zookeeper
```


Now start the Kafka server and view the running status:

```
sudo systemctl start kafka
sudo systemctl status kafka
```


- Create a Topic in Kafka

```
cd /usr/local/kafka
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic

```

The replication-factor describes how many copies of data will be created. As we are running with a single instance keep this value 1.

Set the partitions options as the number of brokers you want your data to be split between. As we are running with a single broker keep this value 1.

You can create multiple topics by running the same command as above. After that, you can see the created topics on Kafka by the running below command:

```
bin/kafka-topics.sh --list --zookeeper localhost:2181
```

- Send Messages to Kafka

The “producer” is the process responsible for put data into our Kafka. The Kafka comes with a command-line client that will take input from a file or from standard input and send it out as messages to the Kafka cluster. The default Kafka sends each line as a separate message.

```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic

> hello

```
- Using Kafka Consumer

Kafka also has a command-line consumer to read data from the Kafka cluster and display messages to standard output.

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning

> hello
```

*****

Python kafka library

1. Confluent-kafka
2. [python-kafka](https://pypi.org/project/kafka-python/)
3. pyKafka


*****

- [kafka-python explained in 10 lines of code](https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1)
- [PyKafka: Fast, Pythonic Kafka, at Last!](https://blog.parse.ly/post/3886/pykafka-now/)
- [Setting up kafka cluster](https://medium.com/@kekayan/a-guide-to-kafka-clustering-in-ubuntu-18-04-5eac0eaf08a2)
- [Manually delete kafka topics](https://medium.com/@contactsunny/manually-delete-apache-kafka-topics-424c7e016ff3)
- [Kafka Python tutorial](https://www.youtube.com/playlist?list=PLxoOrmZMsAWxXBF8h_TPqYJNsh3x4GyO4)
- [Realtime Maps - Kafka, Python, Leaflet.js](https://www.youtube.com/playlist?list=PL2UmzTIzxgL7Bq-mW--vtsM2YFF9GqhVB)
