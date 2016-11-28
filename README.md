# MATIN Newsletter Template

This project is for auto-generating MATIN's newsletters. It is built on [Foundation for Emails](http://foundation.zurb.com/emails), a framework for creating responsive HTML devices that work in any email client. It also includes a Python script to fetch RSS feeds.

## Installation

To use this project, your computer needs [Node.js](https://nodejs.org/en/) 0.12 or greater.

### Clone this project

To get started, run the following command to clone the project:

```bash
git clone https://github.com/amy3478/matin_email.git
```

### Setup

To set up the project, navigate to the project folder in your command line, and install the needed dependencies:

```bash
cd matin_email
npm install
```

## 4 Templates included

- __1-column layout, blue-yellow theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_1_col.png "1 column layout")
- __1-column layout, black-gold theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_1_col_gold.png "1 column layout gold")
- __2-column layout, blue-yellow theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_2_col.png "2 column layout")
- __2-column layout, black-gold theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_2_col_gold.png "2 column layout gold")

## How to create a newsletter

### Step 1: __Prepare a RSS URL__

Get the RSS feed link from MATIN 
```
https://matin.gatech.edu/feedaggregator/feed.rss
```
For how to prepare the RSS feed on MATIN, please refer to [the document](https://docs.google.com/document/d/15XePN1W5p0ezKn5U-3q2sTGUM7fyOPp822i_80fsHds/edit?usp=sharing).

Or get a RSS feed url from other sites. Below are two examples used for testing the project
```
https://www.sciencenews.org/feeds/headlines.rss
http://rss.nytimes.com/services/xml/rss/nyt/Science.xml
```

### Step 2: __Run the script to fetch the feed__

Run the command below
```bash
cs src/etc
python3 scraper.py [RSS_URL] [num] ../pages/[template_file_name] [keyword]
```
#### [RSS_URL]: the URL got from Step 1
#### [num]: the number of articles to fetch
#### [template_file_name]: one of 4 templates below
* tmp_1_col.html
* tmp_1_col_gold.html
* tmp_2_col.html
* tmp_2_col_gold.html
#### [keyword] (__optional__): a keyword used to filter the image grabbed from the article. It has been set to **master** by default. **master** is the keyword to get the main image from New York Times RSS. 

Website | Keyword
--- | --- 
New York Times | master
Science News | main
