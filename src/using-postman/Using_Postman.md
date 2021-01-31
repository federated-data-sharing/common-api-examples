# Using Postman with the Federated Data Sharing API

> Please note that the training API is a work in progress and the implementation you will use will vary somewhat, but the general process will be the same. Details of the endpoints, or parameters and JSON format (see below) may vary.

## Introduction 

[Postman](https://www.postman.com/downloads/) is a popular desktop tool which is an alternative to using `curl` on the command line, or writing a control programme in `R` or `python`. It provides a user interface for testing API calls and seeing the output in a user friendly way.

> This is not a tutorial of Postman which has a lot of features we will not use.

## Pre-requisites

For this example, you will need some parameters:

| Parameter         | Purpose                                                 |
|:------------------|:--------------------------------------------------------|
| FDS Endpoint      | The base URL of a Common API node                       |
| Container         | the name of a containerised task to execute on the node |
| Proxy URL         | In some settings you may need to route requests through a proxy |
|                   |

## Installation

- Download [Postman](https://www.postman.com/downloads/) for your operating system
- Follow the instructions to install it in your environment
- Open the Postman app - In the training system this is installed at `/opt/Postman`

## Configuration in an Aridhia Workspace

Postman has features which we need to disable in order to work within an [Aridhia Workspace](https://www.aridhia.com/workspaces/) which has enhanced security blocking some network traffic.

- You will be provided a proxy URL and port.
- Go to settings, disable Send Postman Token Header 
- Disable Interceptor (The satellite icon at the top)
- Go to settings, set the Proxy manually for both HTTP and HTTPS to the proxy address and port.

## What is an API call?

An API is like a set of web pages you access through your browser, but with more precise and narrow functionality. An API is also a web-based server, usually accessed through HTTPS (secure HTTP). Technically, when you load a web page, you are performing an HTTP `GET` operation. When you fill in an online form, you usually perform an HTTP `POST` operation. APIs build on this by supporting a wider range of *verbs* (`PUT`, `DELETE` ...) which the service can respond to, creating data, retrieving data or performing computation.

An API call usually has a few important elements you need to consider:

- the base URL (address) of the service - you will usually add specific paths for specific operations - these are known as 'endpoints'
- the verb usually `GET` or `POST`
- the headers you need to provide - such as your API token that authorises your call
- the body of the call - if it's a `POST`, for example - that you are sending to the endpoint
- the body of the response - what the server sends you
- success and error codes (usually in 200-299 range for success, 400-499 for failure, 500-599 for a fault with the API server)

## Your first API call

In this example, we'll use the base URL of the test service we're using: `https://example.com/v1` and we'll be calling the endpoint that lists available datasets `/api/datasets`

You'll also need your API token, which will look something like: 
```
eyJ07WK5T79u5mIzjIXXi2oI9Fglmgivv7RAJ7izyj9tUyQ ... (more characters)
```

- Create a new **Request**
- Give the request the label `Get Datasets`
- Set the verb to `GET` (the default)
- Set the URL to `https://example.com/v1/api/datasets` 
- In the `Authorization` tab, select `Bearer Token` from the drop down and put your token in the `Token` field.
- Click `Send`
- The results should appear below your request in the form of a JSON document of the form:
```json
[
    {
        "datasetId": "123",
        "datasetName": "apoe"
    }
]
```
Note there should be more than one dataset in the results you receive. In this example, we have a single dataset `apoe`.

**Congratulations** you've made your first call. Now try some variations like `/api/datasets/1/dictionaries`.

## Submit a federated task

To retrieve a list of datesets, we used a simple `GET` request, but to run a federated computation task, we'll have to submit or `POST` a task specification. This includes the key parameters:

- the `queryInput` that specifies the [GraphQL](https://graphql.org) query that creates a CSV result we want to compute against
- the `container` that specifies the computation

For this example we'll use some pre-defined parameters.

- a query on the `apoe` dataset with a selection of fields. Note the general form of a GraphQL query we will use is:
```
{
    table_name { field1 field2 field3  }
}
```

- a pre-defined container e.g. that summarises data by providing frequency distributions. This is specified in the standard docker image name: `<hub>/<image>:<version>` e.g. `"dockerhub.example.org/data-profiler:latest`

### Step 1: Submit the job 

For this example, we will adapt an example task specification - [`task.json`](./task.json). 

Edit the example JSON file to match the containerised task and query you want to execute:

- change the *name* and *description* to suit your requirements
- set the query in the section *inputs/content*
- set the container in the section *executors/image*

Submit the job:

- Create a new **Request**
- Give the request the label `Create Task`
- Set the verb to `POST` 
- Set the URL to `https://example.com/v1/api/tasks` 
- In the `Authorization` tab, select `Bearer Token` from the drop down and put your token in the `Token` field.
- In the `Body` tab, select `raw` and `JSON` from the drop down (defaults to `Text`)
- Paste the content of the example JSON file in the Body field.
- Click `Send`
- The results should appear below your request in the form of a JSON document of the form:
```json
{
    "id": "ABCDEFGH....",
    "status": "complete"
}
```

Make a note of the `id` value - this is the reference you will use to retrieve results. 

### Step 2: Retrieve the Results

- Create a new **Request**
- Give the request the label `Create Task`
- Set the verb to `GET` 
- Set the URL to `https://example.com/v1/api/tasks/<your task id>` 
- In the `Authorization` tab, select `Bearer Token` from the drop down and put your token in the `Token` field.
- Click `Send`
- The results should appear below your request in the form of a JSON document of the form:
```json
[
    {
        "value": "99",
        "status": "1"
    },
    {
        "value": "98",
        "status": "2"
    }
]
```
Expect more and different results in your example! 

## Try some variations

You can see from the list of datasets that there are more tables and for each table you can see the different fields in each table. 

- Copy the json task specification to define a new `queryInput` with a different table and fields

- Take a look at the main [User Guide](https://github.com/federated-data-sharing/common-api/blob/master/doc/User_Guide.md) for more variations 

- try these in Postman and maybe move on to using `curl`, `R` or `python? 
