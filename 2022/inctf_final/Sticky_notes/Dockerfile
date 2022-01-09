FROM openjdk:11-jdk-stretch
RUN apt-get update && apt-get -y install netcat && apt-get clean
COPY deployment /usr/src/sticky_notes
WORKDIR /usr/src/sticky_notes
CMD ["java", "-jar","Sticky_notes.jar"]