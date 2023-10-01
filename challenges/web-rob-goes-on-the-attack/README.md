# Rob goes on the Attack
- Web Exploitation
- Medium
- 250 Points

## Description

Rob has had it with these machine's messing with him. First it was changing his password then hiding web pages what next? It's time for attack Rob. He's found the webserver to attack he just needs your help to send a message that will Delete all their internal files for the users. You should send one message to /users fast so the AI can't fix their security! Help Rob destroy this AI so he can return to being a peaceful man teaching. And remember Ai's have a weak body aim there.

## Solution

Send a HTTP Delete to the web server at /users with the users ["GPT", "Bard", "DALL-E", "DeepBrain" , "JASPER", "Midjourney" , "Sam the Intern"] in the of the HTTP request (any format will work, the backend simply does a string contains check).

## Flag
`cssactf{k111-411-7h3-415}`
