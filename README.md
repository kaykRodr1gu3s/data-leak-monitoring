## Index
1. [overview](#overview)
2. [Requirements](#requirements)
3. [Instalation](#instalation)
4. [Configuration](#configuration)
5. [Executing](#executing)
6. [Event on splunk](#event-on-splunk)


## Overview

This project focuses on collecting data from Pastefo and Pastebin using web-scraping techniques. The primary objective is to gather valuable information from these sources and subsequently upload the collected data to an index on Splunk using the Splunk SDK.

### Data Collection

The data collection process involves:

  + Web Scraping: Implementing robust web-scraping techniques to extract data from Pastefo and Pastebin. This involves handling various challenges such as dynamic content, pagination, and data extraction from different HTML structures.
  
  + data Parsing: Processing the scraped data to extract relevant information, ensuring data consistency, and handling any anomalies or missing values.

### Data Upload

The collected data will be uploaded to a Splunk index, leveraging the capabilities of the Splunk SDK. This process includes:

  + Data Transformation: Converting the extracted data into a format suitable for Splunk ingestion. This may involve structuring the data into JSON.
  + Splunk SDK Integration: Utilizing the Splunk SDK to programmatically create indexes and upload data.


This project aims to create a comprehensive solution for collecting, processing, and analyzing data from Pastefo and Pastebin, providing valuable insights through Splunk’s powerful analytics capabilities.




## Requirements

+ Splunk
+ Python 
+ Chocolatey
+ git

## Instalation
  
  #### Splunk
  
  For install the splunk enterprise, you need to login in [splunk](https://www.splunk.com/). When you log in , you need to [download](https://www.splunk.com/en_us/download.html)

  #### Chocolatey 

  For install chocolatey in your windows, just read the documentation on [chocolatey[(https://chocolatey.org/install#individual)

  #### Make

  For install the make for utilizing the Makefile, you just need to execute `choco install make`

  #### Python

  For install the python, just check the [python download page](https://www.python.org/downloads/) and select which version you want.

  #### git
  For install the git, execute the powershell command ` winget install --id Git.Git -e --source winget ` or `sudo apt-get install git`
  
## Configuration

For clone the repository,use this git command `git clone https://github.com/kaykRodr1gu3s/data-leak-monitoring.git`.
For configure the enviroment , change the directory using the command `cd data-leak-monitoring`. For configure the the virtual enviroment and install the libraries , use this make command `make install`

In the [pastefo](https://github.com/kaykRodr1gu3s/data-leak-monitoring/blob/main/Pastefo/main.py) or [pastebin](https://github.com/kaykRodr1gu3s/data-leak-monitoring/blob/main/Pastebin/main.py), you can change the index name that will be created on splunk, change this parte of code `pastebin = Pastebin("pastebin")` or `pastefo = Pastefo("pastefo")`, by default will be the name pastefo and pastebin, you can change if you want.

#### .env file

The [.env](https://github.com/kaykRodr1gu3s/data-leak-monitoring/blob/main/.env) is the enviroment variables, for configure, put your username and your password for connect in your splunk apllication. In the code, i'm using the username and the password, you can use token and outher just read [splunk-sdk](https://github.com/splunk/splunk-sdk-python), there have many ways to configure your .env file.


## Executing


With all configured, just need to execute the code the make command is: `make pastefo` or `make pastebin`. This command will execute the [pastebin](https://github.com/kaykRodr1gu3s/data-leak-monitoring/blob/main/Pastebin/main.py) or [paste](https://github.com/kaykRodr1gu3s/data-leak-monitoring/tree/main/Pastefo)


## Event on splunk

For visualize the event on splunk, open your splunk enterprise and go to seach&report and put `index=>index that you create<`
