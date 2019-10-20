# Prototau API - Offical Documentation
--

## Structure

###1. Introduction to the readme & Prototau API (PAPI)
###2. 
###3. Database Development Details


## 1. Introduction to the Readme

####What this README is:
<ul>
	<li>
		A guidance in usage of the API in general, how to retireve/postupdate/delete: i.e. what routes exist and how to use them to get data.
	</li><br>
	<li>
		Serves as an ever updating development plan for the API, in the 		case of future extension.
	</li><br>
	
	<li>
		Neccessary implementation details of all the systems invovled, DB:s, architecture, hosting platform, etc.
	</li><br>
</ul>

#### What this README isn't:
<ul>
	<li>
		Complete instructions, full implementation details, tutorial on any subsystem involved (e.g. MongoDB, Python, API:s). For more general questions regarding the tech stack, turn your attention towards the data analytics team or stackOverflow.
	</li><br>
	<li>
		Full complete plans about the future, e.g. including upcoming changes. 
	</li><br>
</ul>

## 2. Workspace setup and how to work on PAPI

## 3. Database Development Details

### 3.1 Misc

Prototau API relies on a SQL database however, the exact architetecture depends on in the API is deployed locally (i.e. running in an on-board "raspberry pi" or if it's deployed on the cloud.

<b>Local DB and API deployment</b>

sqlLite and local flask server

<b>Remote DB and API deployment</b>

heroku deployed flask wsgi server with added 

### 3.2 Schema updates

