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
- __1-column layout, black-gold theme **(Recommended)**__  
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_1_col_gold.png "1 column layout gold")
- __2-column layout, blue-yellow theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_2_col.png "2 column layout")
- __2-column layout, black-gold theme__
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_2_col_gold.png "2 column layout gold")

### 2 item layouts
- with the cover image
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/with.png)
- without the cover image
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/without.png)

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

Before run the script, you need to install some Python packages.
```bash
pip3 install ImageScraper
pip3 install beautifulsoup4
```

Run the script
```bash
cd src/etc
python3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>
```
or 
```bash
python3 scraper.py --url <rss-url> --num <num-of-article-to-fetch> --tmp <path-to-the-template> --keyword <keyword-to-filter-image>
```

#### rss-url: 
the URL got from Step 1
#### num-of-article-to-fetch: 
the number of articles to fetch
#### path-to-the-template: 
one of 4 templates below

* tmp_1_col.html
* tmp_1_col_gold.html
* tmp_2_col.html
* tmp_2_col_gold.html

#### keyword-to-filter-image:
(__OPTIONAL__) a keyword used to filter the image grabbed from the article. It has been set to **master** by default. **master** is the keyword to get the main image from New York Times RSS. 

Website | Keyword
--- | --- 
New York Times | master
Science News | main

#### Example 
Use the command below to
**create a 1-column gold theme newsletter with 5 articles from New York Times Science**
```bash
python3 scraper.py -u http://rss.nytimes.com/services/xml/rss/nyt/Science.xml -n 5 -t ../pages/tmp_1_col_gold.html -k master
```

### Step 3: __Build the newsletter__
Because MATIN newsletter project uses Foundation Email framework, we need to build the final version that has inline CSS code. Run the command below.
```bash
npm run build
```
**By running the code above, a new tab will be open in your default browser. It always opens index.html by default. In order to see the newsletter you created in Step2, just simply append the name of the template file to the url address. It should look like http://localhost:3xxx/tmp_1_col.html if your newsletter uses tmp_1_col.html as the template.**

This will create/update the final html file in **dist** directory. For instance, if you run the code below
```bash
python3 scraper.py -u http://rss.nytimes.com/services/xml/rss/nyt/Science.xml -n 5 -t ../pages/tmp_1_col_gold.html -k master
npm run build
```
The file **dist/tmp_1_col_gold.html** should be updated. 

### Step 4: __Create a newsletter on MATIN__
- Login to the Admin panel
- Choose **Newsletter** from **Components** dropdown
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/newsletter1.png)
- On Newsletter tab, choose **New** to create a newsletter
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/newsletter2.png)
- Choose **No Template** and save
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/newsletter3.png)
- The created newsletter will be shown on the list. Click it to edit
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/newsletter4.png)
- Copy the HTML code from the file generated in the previous step to **HTML Content** textarea
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/newsletter5.png)

### Step 5: __Test__
Now you can select the newsletter to preview or send a testing copy to yourself.


## Todo
- Complete the pipeline of fetching secondary content once the content is confirmed

