# Exploratory Data Analysis Module

Author: [Laura Uzcategui](https://github.com/laurauzcategui)

** Exploratory Data Analysis - Lessons &amp; Project from Data Analyst Nanodegree**

The purpose of this repository is to gather all exercises from lessons and Project done over Data Analyst Nanodegree from [Udacity](www.udacity.com)

### What is Exploratory Data Analysis - EDA ?

 Exploratory data analysis or EDA. Is the examination of data and relationships among variables, through both numerical, and graphical methods.

 It often takes place before more formal, more rigorous statistical analysis.

### Setup of your environment with Docker

In order to work with this Module one of the requirements is
[R Programming Language](https://www.r-project.org/about.html) and/or [R Studio](https://www.rstudio.com/)

As I was lazy to install this on any of my laptops and as I want it to be able to have it build from wherever I'm working from I decided to use Docker.

I decided to use [Rocker](https://github.com/rocker-org/rocker) project, which allow you to use R by providing docker images ready for you to use.

I've build my own docker [image](./r-docker/Dockerfile), since I wanted to have ready few libraries straight away instead of installing every time I use the container.

#### Build the docker image

In order to start using the container install Docker and run the following command to build your image:

`docker-compose build`

#### Run R-Studio from the container

I have used [Docker compose ](https://docs.docker.com/compose/gettingstarted/) but feel free to explore around by just using the image above if you like.

Before running the container, create a `.env` file with the following lines:

```
PASS=
LOCAL_VOL=
```

And put any values for mapping the password and the directory you want to map to for storing your R scripts.

Run the container with:

`docker-compose up`

#### Login to RStudio

[Login here :) ](http://localhost:8787/)

User: rstudio <br/>
Password : the password you have setup into your `.env` file

Have Fun !
