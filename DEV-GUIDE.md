# Automatic Challenge Installation to CTFd

## Overview 

To automatically upload all of our challenges to the CTFd website, follow these steps. This guide assumes that the challenges are uploaded in a GitHub repository and follows a standard folder structure (e.g. have README.md, files/ folder if necessary, docker/ folder if necessary, etc. You should base the folder structure to this repo's). 

We will use ctfcli to upload our challenges to the website, and this ctfcli tool needs a `challenge.yml` for each challenge folder for it to work. Luckily, we made a script that automatically generates those yml files in the right folder. You must still check if the yml files contain the information you want, as we might have made things a default or a different value, and you no longer want to keep the same behaviour. 

Once that's done, you commit and push the changes to the challenges GitHub repository, like this one! After that, we will move to the proxmox server. Assuming we have the CTFd and its VM set up, you will then need to clone the challenges GitHub repository. Do this in the same folder as where your CTFd is in, so this repo. and the CTFd should be "siblings" and share the same parent folder. 

Then, you need to run the install command on each challenge. That can be tiring, so we made a script for that, which will automatically install all the challenges and put them to the CTFd website. After this is done, you should be able to see the challenges in the `/admin/challenges` page of the CTFd website. Note that if a challenge has a docker folder, you will need to manually run `docker-compose up -d` in that challenge folder in the VM console.

A more detailed set-up instructions will follow below.

## 1. Generate challenge.yml

You should generate the challenge.yml files for each challenge by installing a package and running the following scripts, one by one:
```bash
pip install pyyaml 
python yml-maker.py
```

### This is what the README of a challenge should look like:

Each challenge must have a README.md file that follows the format below, so that the script `yml-maker.py` works properly. Also, this seems to be the standard README based on the existing challenges in our repos. Thus, this is what a README.md for a challenge should look like.

**Note:** You can use either `-` or `*` for bullet points in the metadata section (Information under Challenge Name).

```markdown
# Challenge Name
- Revision 0
- Category Name
- Difficulty
- Point Value Points
- Type: standard (optional)
- State: visible (optional)
- Flag Type: static (optional)

## Description
This is the challenge description that participants will see.
Can include multiple paragraphs, links, connection instructions, etc.

## Hints
1. First hint
2. Second hint
3. Third hint

## Solution
This section contains the solution and will NOT be included in challenge.yml.
Explain how to solve the challenge here.

## Flag
`cssactf{YourFlagHere}`
```

### Required Sections in README.md
- **First line**: Challenge name (used as the challenge title in CTFd)
- **Category**: Must be one of: Binary Exploitation, Web Exploitation, Cryptography, Forensics, Reverse Engineering, Misc, OSINT, Pwn, Steganography (if more categories are added, they should be added in the script too. Or we can also improve the script to account for this; due to time constraints, that can be done in the future.)
- **Difficulty**: Easy, Medium, or Hard (becomes a tag in CTFd)
- **Points**: Number followed by "Points" (e.g., "100 Points")
- **## Description**: Challenge description shown to participants
- **## Flag**: The flag enclosed in backticks

### Optional Sections in README.md
- **## Hints**: Will be appended to the description if present
- **Type**: `standard` (fixed points) or `dynamic` (decreasing points) - defaults to `standard`
- **State**: `visible` (shown immediately) or `hidden` (hidden until revealed) - defaults to `visible`
- **Flag Type**: `static` (exact match), `regex` (pattern matching), or `case_insensitive` - defaults to `static`

### Script Defaults (if not found in README)
- **Category**: Defaults to `Misc`
- **Points**: Defaults to `100`
- **Difficulty**: Defaults to `Medium`
- **Description**: Empty string
- **Flag**: Empty string
- **Type**: Defaults to `standard`
- **State**: Defaults to `visible`
- **Flag Type**: Defaults to `static`

### Script Hardcoded Values
- **Author**: Always set to `CSSA` (configured at top of yml-maker.py)
- **Files**: Automatically includes all files from the `files/` subdirectory in each challenge folder

### Example (with optional fields)

```markdown
# Parity the Platypus
- Revision 0
- Cryptography
- Easy
- 100 Points
- Type: standard
- State: visible
- Flag Type: static

## Description
Dear Detective,

I finished creating a program that should help remove some tedious work in detective work and the program has been encrypted and sent as binary. Unfortunately, I learned that an evil-doer has blasted it with their least-significant-bit-flip-inator and the program won't decrypt anymore.

Luckily, I have a failsafe mechanism implemented where the 8th bit from the left (1st bit from the right) must be 1 if the number of 1s is odd and 0 if the number of 1s is even. Perhaps if we figure out which 8-bit words were affected (and no longer pass the failsafe), we can actually gain information about this evil-doer! I have split up the program into lines of 8-bits for ease of digestion.

I await your reply,
P.P.

## Hints
1. Look up "parity bit" to understand the error detection mechanism
2. The affected bits reveal the flag when converted to ASCII

## Solution
Calculate the parity and see which lines don't match and were thus affected. Alternatively, calculate the opposite, or even odd 1s parity and see which lines *do* match. Convert those binary numbers to ASCII characters to obtain the flag.

## Flag
`cssactf{Bit_By_Bit_I_Weep}`
```

## 2. Git

Once you've ran the script, you should stage those files, commit, and push. Ideally in a new branch, make a PR, get approval, then merge.

In a Proxmox's VM where you intend to put all your ctf-related code, and in the same folder as where CTFd is, which is likely the root folder of that VM, clone the GitHub repository where your challenges are in.

## 3. CTFCLI 

You will need to do the command IF you don't have CTFCLI yet.

```bash
pip install ctfcli
```

If that doesn't work, you may try:

```bash
pip3 install ctfcli
```

If those don't work, you may try:

```bash
python -m pip install ctfcli
```

Then, initialize it with this command. This will prompt you to put the URL where the ctfd runs, as well as the access token. You can find the token in our CTFd website/instance, if you go to Settings (NOT admin panel, but you should be logged in as admin.)

```bash
ctf init
```

## 4. Batch-install the challenges

At this time of writing, the command used to batch-install the challenges to the website is done by typing the following command in the console of the VM. This should be ran all at once. 

What's great is if the challenge has already been uploaded, it'll be skipped so there are no duplicates. If you need to update a challenge, you can use the `sync` command. More info on the links below.

**You must do one of the following (first one is recommended) in the root folder of the cloned repository:**

### Option 1
```bash
for ch in challenges/*/; do
    echo "Installing ${ch%/}"
    ctf challenge install "${ch%/}"
done
```

### Option 2
We created `batch-install.py` to automate this further, but it has not been tested yet. It will be tested once we have this year's challenges.

```bash
python batch-install.py
```

## 5. How to know if this worked

You should be able to see the challenges in the `/admin/challenges` of the CTFd website. The metadata should also match what's in `challenge.yml`. If a challenge has files folder, the file contents of that folder should be in the challenge. If a challenge has a docker folder, the docker folder contents won't be visible in the website, but that doesn't mean something failed. You will just need to manually run `docker-compose up -d` and that's it. The challenge description should tell the user what they need to do.

Note: It can be hard to troubleshoot because there were times when it said "Success" in console, with no visible errors, and yet it still didn't show up on the website.

## These links might be helpful in general
- https://github.com/CTFd/ctfcli
- https://docs.ctfd.io/docs/management/ctfcli/overview
