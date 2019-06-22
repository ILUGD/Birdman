# Birdman
## About
'Birdman NotASPAMbox' is an  automated mail and social media publishing command line interface.

## Checklist
1. [x] Created the frontend CLI.
2. [ ] Connected frontend to the REST API
3. [ ] Connect Twitter API to REST API
4. [ ] Connect Telegram API to REST API
5. [ ] Connect SMTP Lib to REST API (for mailing list)
6. [ ] Connect Github API to REST API (for github bot) 

## Tech Stack
1. Python 3.7
2. Django REST Framework
3. PostgreSQL
4. Meetup API
5. Telegram,Twitter,Github bot API
6. smtplib

## Working
Birdman works by  asking the user for relevant data for publishing for eg. meetup link, poster link, meetup theme, talks etc. and outputs it as a template and shares the  output to all social media networks wherever required.
<img src="http://0x0.st/zMIG.jpg">
```
  $ birdman 
  Venue Decided(y/n):
  Meetup Link:
  Poster Link:
  Telegram Username:
  Talks Decided (y/n):
```
A sample Output will look like this:
```  
  Processing ↑ (saving to .birdman/<date>/meetup.txt)
  
  Join us for the next ILUG-D Meetup on <Date/Time> at <Venue> 
  Event Page :<Meetup Link>

  Would you like to edit this ? (y/n)
```
If talks are not decided the CFP email to the mailing list and twitter will look like this.
Issues labeled as not delivered will also be pingd using the Github API
```
  
  Processing ↑ saving to .birdman/<date>/meetup.txt

  Call for Proposal is open for the next next ILUG-D Meetup on <Date/Time>. Raise an Issue at https://github.com/ILUGD/talks.

  Would you like to edit this ? (y/n):
```
A copy of the meetup.txt file would be send through the Telegram Bot to any admin for approval.

## Extras 
To create a new meetup page -
```
$ birdman --new-meetup
  Venue:
  Date:
  Time: 
  Talk (Talk Title- Github link):
  Any More(y/n)?:n #If in case
  Talk (Talk Title- Github link):
  Processing ↑ (saving to .birdman/<date>/meetupPage.txt)
  
  Join us for the next ILUG-D Meetup on <Date/Time> at <Venue> 
  Event Page :<Meetup Link>
  Talks: <Talk Name> - <Github Link>
  Would you like to edit this ? (y/n)
  Send CFP ?(y/n):
  Awaiting admin response.. Exiting.
```
Skip the questions by selecting valid flags like birdman --venue --talks wouldnt ask you if venue and talks were decided
## Contributing 
### Folder Structure
- The API folder contains everything we need to build a REST-API for the frontend CLI to communicate with. 
- The frontend contains all things to deal with the frontend so dont import code from API to there.
### Testing 
All new features should have a test in the specific tests.py files

## Tasks
1. Create a REST API for logging,DB management using postgres
2. Make a Twitter, Telegram bot.
3. Use SMPTlib for sending mails to mailing list 

## Features
1. Mailing list support 
2. Twitter, Telegram posting
3. Automatic CFP (Call for Proposal) Announcement

## Footnotes
Feedback form announcement will be triggered automatically after 1 hour of meetup ending on twitter,telegram and mailing list

