# Cambridge College 2023 🎓

Hello everyone, and welcome to the exciting world of analytics! In this project, we are going to use a tool called [Kedro](https://kedro.org/) to predict customer churn at a bank. That's a technical way of saying we'll be identifying which customers are likely to stop using the bank's services.

This is a fantastic opportunity for you to dip your toes into the world of data science, and don't worry - you don't need any prior experience or technical knowledge to get started.

## What do you need to setup for this demo to work?

Before we dive in, you'll need a couple of things:

1. [A GitHub account](https://github.com/join) 
2. [A Gitpod account](https://gitpod.io/login/)

GitHub is a platform where people store and share code. Gitpod, on the other hand, is a platform that allows you to code right from your browser, without needing to set anything up on your personal computer.

## What should you expect?

Throughout this project, you will learn about:

- The basics of using Kedro, a Python framework for creating reproducible, maintainable, and modular data science code.
- Presenting your findings in a clear and understandable way with [Kedro-Viz](https://demo.kedro.org/).

## How was this work created? 

[We used ChatGPT](https://chat.openai.com/share/9a244617-9fe9-43bf-ab30-9e528a9269cd) to: 

 - Analyse the dataset from Kaggle
 - Create code for data processing and modelling
 - Convert the code into a Kedro project

## Access your workspace and see your project

Now that you're set up and have a sense of what to expect, let's jump right in and start predicting customer churn!

Get access to your workspace by opening: https://gitpod.io/github.com/yetudada/cambridge-college-2023

A typical Kedro project structure looks like the following:

```
kedro-tutorial/
|-- conf/
|   |-- base/
|       |-- catalog.yml
|       |-- parameters.yml
|   |-- local/
|-- docs/
|-- notebooks/
|-- src/
    |-- kedro_tutorial/
        |-- pipelines/
            |-- data_preprocessing/
                |-- nodes.py
                |-- pipeline.py
            |-- modelling/
                |-- nodes.py
                |-- pipeline.py
        |-- pipeline_registry.py
|-- requirements.txt
```

## Get into your project

We will need to change directories into your project by running: 

```
cd kedro-tutorial
```

 ## Install the requirements to run this project

 We need to install all of the libraries and packages that this project depends on to run, use this command:

 ```
 pip install -r src/requirements.txt
 ```

## Run your pipeline

You're going to do your first pipeline run: 

```
kedro run
```

## Visualise the pipeline 

Next, we're going to visualise pipeline using [Kedro-Viz](https://demo.kedro.org/), run: 

```
kedro viz
```
