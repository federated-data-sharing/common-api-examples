# Common API - Worked examples

## Introduction

This repository contains some worked examples of how to use the Federated Data Sharing Common API, especially when developing analysis plans that require setting up containerised scripts.

> Note: The examples have been defined for the work in progress Version 1.1.0 of the Common API. Please refer to the [Common API](https://github.com/federated-data-sharing/common-api) for details of the API itself.

## Preparing for federated analysis

As a scientist, statistician or data scientist, you may be used to developing scripts working directly with data - your `R` or `python` scripts can load the data directly, or maybe you're using a spreadsheet package or a statistical tool which wraps up the analysis plan for you. If you're using federated analysis this may not be an option for you - the data is held remotely. Your interaction with the data will be via the programming interface ("API") or a tool that uses it. Whereas you would normally expect a high degree of iteration (or "trial and error") when working with local data, you need to plan for a different form of iteration.

Data platforms that implement the Common API commit to helping reduce the friction of remote access in a number of ways intended to help you:

- Implementing a *standard* API, which means you don't have to keep learning new ways of getting metadata or processing their data
- Providing detailed and up-to-date metadata on data they share through the API, giving you enough detail to adapt your analysis to what data is really there
- Letting you run *your* code on the data through the use of [docker containers](https://www.docker.com/resources/what-container)
- Supporting iterative sessions - where you can run your analysis as often as needed to answer your research questions (within some fair usage limits)

In return, you should revisit your analysis plan and structure it to the remote arrangement. You may want to consider:

- whether you will be interacting with one or more than one remote site (also known as a "node") 
- whether you will be interacting with a mix of nodes at different levels of sharing (also known as "Level 0", "Level 1" or "Level 2" nodes)
- setting a number of stages or phases for your analysis in order to get early feedback on the process and build trust in the data and your connection with the remote sites.
- whether integrating data from multiple sources is important for your analysis algorithm (for example to develop a machine learning model)

Examples of staging or phasing analysis might reflect a standard research or data science life cycle:

- exploratory analysis: systematically validating, summarising or exploring the remote data early on in orde
- quality checks, outlier analysis
- sampling
- visualisation
- data engineering or integration (or at least creating a standard data frame for analysis)
- statistical tests
- modelling data
- validating models

A modular and composable approach to your analysis code will allow you to iterate at each stage and if necessary combine the analysis into reproducible process. This should reduce frustrations with not having direct access to data.
