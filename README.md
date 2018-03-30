# Slack Google Image Search
use a slack slash command to grab the top image from a google image search

# What is this?
Just a super simple script to use Google CSE to grab the top imgur image returned.
Note: unless you pay google, you'll be limited to 100 returns per day

# Install
1. Make sure Docker is installed
2. Pull repo onto you server and cd into repo dir
3. Build Docker image with: 

`docker build -t slack-image . `

4. Run Docker image with 

`docker run -d -p 5000:5000 -e API_KEY='$YourGoogleSearchAPIKEY' -e CX_KEY='$CXKey' -e SLACK_TOKEN='$YourSlackSlashCommandTOken' slack-image`

4. tada!

# Usage
If your slack slash command is "/image" :
Get the it's happening .gif by entering: "/image its happening"
