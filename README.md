# Data Pipeline: Twitter Sentiment Analysis


![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white
)
![Elastic](https://img.shields.io/badge/Elastic_Search-005571?style=for-the-badge&logo=elasticsearch&logoColor=white
)
![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white
)


## Table of Contents
  - [Introduction](#introduction)
  - [Technologies](#technologies)
  - [Architecture](#architecture)
  - [How it works](#how-it-works)
  - [Notes](#notes)
  - [Screenshots](#screenshots)

---

## Introduction
This projects do sentiment analysis for some tweets concering airports to check the satisfaction of the clients.

---

## Technologies

AWS is heavily used here for the analysis.
- AWS cloud9
- Amazon Kinesis Data firehose
- AWS lambda
- Amazon comprehend
- ElasticSearch (OpenSearch)
- Amazon S3

---

## Architecture
![Arch](images/Architecture.png)

---

## How it works
- For the sake of simplicity, we simulate the flow of tweets instead of having a dev account on twitter. Please find attached `Data input` folder.
- Using AWS Cloud9 IDE, we send some tweets every specific period of time (we can do this based on some distribution) to kinesis firehose
- Firehose delivers the data to Lambda to send it to Amazon comprehend for sentiment analysis (assuming all the tweets are in English)
- The sentiment analysis is returned and sent to elasticSearch (openSearch) for further analysis and visualization


---


## Notes
- This architecture is for eductional purposes. You may notice it is not the perfect architecture.
- We can pass the tweets to Amazon translate before Amazon comprehend to make sure all the tweets are in English
- Other Services are available for analysis and visualization, such as Athena and Quicksight. Yet, I prefered elasticSearch since it is supported by Kinesis Firehose
- Please find attached the code for cloud9 and Lambda


---


# Screenshots

![hits](images/opensearch_hit.png)
![vis1](images/visualization_1.png)
![vis2](images/visualization_2.png)