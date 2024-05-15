# Use an official openjdk runtime as a parent image, as Kafka clients run on Java
FROM openjdk:11-jdk-slim

# Set the working directory
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y wget tar bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Kafka version and installation directory
ENV KAFKA_VERSION="3.7.0" SCALA_VERSION="2.13" KAFKA_HOME=/opt/kafka

# Download and install Kafka binaries for the kafka-console-consumer
RUN wget https://dlcdn.apache.org/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz -O /tmp/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz && \
    tar -xzf /tmp/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz -C /opt && \
    ln -s /opt/kafka_$SCALA_VERSION-$KAFKA_VERSION $KAFKA_HOME && \
    rm /tmp/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz

CMD ["sh", "-c", "/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server ${KAFKA_BROKER_URL} --topic ${KAFKA_TOPIC} --from-beginning"]
