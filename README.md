# Comparative Analysis of Apache Iceberg and Delta Lake on AWS EMR Cluster

**Author:** Thomas Durlacher  
**Date:** 19 Jan 2024

## 1. Introduction

The project conducted a comprehensive performance comparison between two popular open-source table format and storage layer solutions - Apache Iceberg and Delta Lake. The evaluation took place on an AWS EMR (Elastic MapReduce) cluster, providing insights into their efficiency, scalability, and compatibility within a distributed big data processing environment. To make the performance measurements comparable, one dataset from the TPC-DS benchmarks was used to create tables with the two different table formats.

## 2. Repository

GitHub Repository: [https://github.com/DurlacherT/aws_emr_lakehouse](https://github.com/DurlacherT/aws_emr_lakehouse)

## 3. Objectives

- Evaluate the performance of Apache Iceberg and Delta Lake in terms of read and write operations with the help of the TPC-DS benchmark.
- Assess the scalability of both solutions as the size of the dataset increases.
- Analyze the query performance on complex analytical workloads.
- Investigate the ease of integration with AWS EMR services.
- Identify any notable advantages or limitations of each solution in the context of the project requirements.

## 4. Tools and Technologies

- **Apache Iceberg:** An open table format for big data that offers features like schema evolution, ACID transactions, and time travel capabilities.
- **Delta Lake:** A storage layer that brings ACID transactions to Apache Spark and big data workloads.
- **AWS EMR:** Elastic MapReduce service for easy deployment and scaling of big data processing frameworks like Apache Spark.
- **Pyspark:** Python API for Apache Spark.
- **AWS Glue:** A serverless data integration service.
- **S3:** AWS storage service.
- **Jupyter Notebook:** AWS workspace with Pyspark kernel.

## 5. Methodology

### Dataset Preparation:

Generate synthetic datasets of varying sizes to simulate real-world big data scenarios.

### Cluster Setup:

Deploy an AWS EMR cluster with Apache Spark and necessary dependencies for both Iceberg and Delta Lake.

### Data Ingestion:

Load datasets into tables using both Iceberg and Delta Lake formats.

### Performance Metrics:

- Measure the time taken for read and write operations.
- Evaluate the scalability by gradually increasing the dataset size.
- Execute complex analytical queries and measure query performance.

### Observations and Analysis:

Document any challenges encountered during setup and configuration. Compare and contrast the performance metrics obtained from both Iceberg and Delta Lake.

## 6. Expected Outcomes

- A detailed comparison report highlighting the strengths and weaknesses of Apache Iceberg and Delta Lake in the context of the project.
- Insights into the performance characteristics of both solutions under varying workloads and dataset sizes.
- Recommendations for selecting the appropriate solution based on specific use cases.
- Description and visual representation of different performance measurements.
