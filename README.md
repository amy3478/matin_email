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

## 4 Templates included4

- 1-column layout, blue-yellow theme
![alt text](https://github.com/amy3478/matin_email/blob/master/src/etc/screenshoots/tmp_1_col.png "1 column layout")
- 1-column layout, black-gold theme
- 2-column layout, blue-yellow theme
- 2-column layout, black-gold theme

## How to create a newsletter

- 

Run `npm start` to kick off the build process. A new browser tab will open with a server pointing to your project files.

Run `npm run build` to inline your CSS into your HTML along with the rest of the build process.

## Litmus Tests (config.json)

Testing in Litmus requires the images to be hosted publicly. The provided gulp task handles this by automating hosting to an AWS S3 account. Provide your Litmus and AWS S3 account details in the `example.config.json` and then rename to `config.json`. Litmus config, and `aws.url` are required, however if you follow the [aws-sdk suggestions](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-configuring.html) you don't need to supply the AWS credentials into this JSON.

```json
{
  "aws": {
    "region": "us-east-1",
    "accessKeyId": "YOUR_ACCOUNT_KEY",
    "secretAccessKey": "YOUR_ACCOUNT_SECRET",
    "params": {
        "Bucket": "elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
    },
    "url": "https://s3.amazonaws.com/elasticbeanstalk-us-east-1-THIS_IS_JUST_AN_EXAMPLE"
  },
  "litmus": {
    "username": "YOUR_LITMUS@EMAIL.com",
    "password": "YOUR_ACCOUNT_PASSWORD",
    "url": "https://YOUR_ACCOUNT.litmus.com",
    "applications": ["ol2003","ol2007","ol2010","ol2011","ol2013","chromegmailnew","chromeyahoo","appmail9","iphone5s","ipad","android4","androidgmailapp"]
  }
}
```

For a full list of Litmus' supported test clients(applications) see their [client list](https://litmus.com/emails/clients.xml).

**Caution:** AWS Service Fees will result, however, are usually very low do to minimal traffic. Use at your own discretion.


