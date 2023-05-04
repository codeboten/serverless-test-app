# Serverless app to test Collector layer

This is a minimal serverless Python application to test sending a trace over OTLP to the Collector layer.

## Requirements

* [Serverless CLI](https://www.serverless.com/framework/docs/install-standalone)
* AWS credentials
* Destination for OTLP data (I used Lightstep)

## Setup

1. Install serverless-python-requirements plugin

   ```bash
   serverless plugin install -n serverless-python-requirements
   ```

2. Update config.yaml to configure your OTLP destination

3. Deploy and invoke the application:

   ```bash
   serverless deploy
   # call the deployed method
   serverles invoke --function hello
   ```
