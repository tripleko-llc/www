from jinja2 import Environment, FileSystemLoader

import os


env = Environment(loader=FileSystemLoader("templates"))
sections = ["About", "Charts", "Contact"]
bucketname = os.environ["DEFAULT_BUCKET"]
#cdnlink = f"https://{bucketname}.s3-us-west-2.amazonaws.com"
cdnlink = "https://d1w1feoid5k5rc.cloudfront.net"

about = [
        {
            "title": "A Mess of Applications",
            "body": "These days, there are applications for everything.  Collaboration software, internal wikis, ticketing software, learning management systems, content delivery systems, chat software, sales tracking, blogging, email, video conferencing and more.  There are even applications that <em>keep track of your other applications</em>.<br><br>If you have the money, you can pay for licenses and support for each of these applications, which typically ensures that they will \"plug in\" to each other smoothly.  If you're trying to save a dime and you opt for the free, open-source versions, then the integrations (if they exist) won't be as mature, and there isn't any support if you run into problems.  Often all you get is a long wiki page describing three or four hundred API endpoints.<br><br>"
            },
        {
            "title": "Custom Integrations",
            "body": "We offer bespoke software to handle application integration for small businesses.  You have two applications (or more) that need to exchange and process information in a very specific and automated way, and there simply isn't anything pre-built out there for you to use.  We fill in the missing link so your operations can continue running smoothly.<br><br>"
            },
        {
            "title": "Security",
            "body": "Your data and privacy are important to us.  We will only request the minimum necessary access for your integration to be properly constructed.  Everything is built with an eye on security.<br><br>"
            },
        {
            "title": "Support",
            "body": "We will work with you to understand the problem as thoroughly as possible, and then start brainstorming solutions.  You'll be kept in the loop throughout the design and execution process, and we'll continue tweaking and modifying features as you need them.<br><br>We will agree on a reasonable timeframe of support and maintenance, with the option to renegotiate for extensions at the end of the contract.<br><br>"
            }
        ]


