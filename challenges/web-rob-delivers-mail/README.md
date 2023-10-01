# Rob delivers mail
- Web Exploitation
- Hard
- 400 Points

## Description

Rob's fight with AI is over. He's returned home to relax. Unfortunately for him some new Mail needs to be sent via the Post to those fourth years who were asking about their grades. Knowing that sending a physical copy takes years you decide to update the grades on the Borealis website with Rob's approval. Rob isn't too sure what the URL to update grades is so hopefully you can Get some Help.

He has given you his login cookie: "Cookie":"c60bd23c9022fe5dd8fa8837036ec9789a27e28666ae5a54606f275451383c89" to send the grades. The students asking for their grades are "Ethan": "A+", "Noah": "A+", "Cody": "A+", "Anthony": "A+". You've been told by Rob Borealis has a terrible server so the website won't load and can't handle more than one request at a time when updating grades.

## Solution

Send a HTTP Get request to the server with the body containing the cookie value to /help first then send the HTTP post to /updateGrades with cookie and students in the body.

## Flag
`cssactf{p057m4n-m411-d311v32y}`