# Anti Crypto-Scammer

A boilerplate codebase to deal with crypto-related scams, such as seedphrase miners.

## Motivation

Recently I noticed that whenever I would post about an issue, problem or interest I had in the crypto space, I could just expect to get a Reddit chat request, followed by some semi-literal ape trying to get me to input my seedphrase in a shitty 2016 PHP form.

Beyond that, I've also noticed the massive amount of phishing sites and scam ads on Google whenever I try to get friends into crypto. I won't link any of them, but it truly sucks how easy it is to get turned away from crypto with all this bullshit, so I decided that I want to do something about it.

## Architecture

This is the v1 of my project with an attempt to just completely overload and annoy the crap out of scammers in order to get them to take down their websites and close up operations, or at least keep them on their toes. A framework of sorts that should make it easy for anyone to add websites that are illegitimate and need to be given some of their own medicine.

The codebase consists of a task-runner, a library of utilities as well as some tests. The task-runner makes it extremely easy to add more tasks for more scam sites or other ideas that we might have in the future to deal with scammers.

The library is meant to expand in the future with utilities such as functions for generating random seedphrases. But not just any random seedphrases. I decided to use the Python `better_profanity` library to generate seedphrases with only cursewords, such as the following:

```
pasty menstruation gangbang knobjokey vulgar seduce fellate mothafuck screw strip kawk vixen queers slave kraut pussi smut breasts shagging motherfucker fooker arrse pantie fuckhead
```

## Usage

For now, there's only one crypto phishing website pre-programmed with a spamming algorithm that just constantly enters those seedphrases to hopefully overload whatever cheap services they're running. My MacBook has been at it for mere minutes and is already at over 2K requests sent to the site, and I encourage you guys to add more so we can all blast these scammers.

Now specifically, here's how you guys can run the scripts that are contained in the repository if you guys aren't as tech-savvy:

1. Download [Python](https://www.python.org/downloads/) for your operating system and install it.
2. Clone the codebase by running `git clone` [`https://github.com/Dan6erbond/anti-crypto-scammer.git`](https://github.com/Dan6erbond/anti-crypto-scammer.git) in a terminal.
3. Change your current working directory to the repository by typing in `cd anti-crypto-scammer` in the same terminal as previously used for cloning it.
4. Install all the PIP dependencies with `python3 -m pip install -r requirements.txt`.
5. Run the script: `python3` [`main.py`](https://main.py)

The program will output a log to `log.txt` should you be interested in its progress. Errors will also be added to the log if any occur, hopefully making debug a bit easier for end-users trying to implement additional tasks.

## Contributing

The [`main.py`](https://main.py) file will automatically load files from the `tasks/` folder and attempt to run their `main()` function using threading to facilitate parallel tasks. This should make it particularly easy to add more tasks that other users will then run whenever they update their repositories. Kind of like a decentralized attack on the scammers (see what I did there?)

So adding new tasks is extremely easy. Create a new `.py` file in the `tasks/` folder and implement your logic. Use the `logging` package for logging purpose and add general functions to the `lib/` folder to your heart's content. Afterwards, create a pull request on the [GitHub Repository](https://github.com/Dan6erbond/anti-crypto-scammer) so others can join on the effort to take down these scammers.  Error handling is important, as to avoid crashing the entire program if something goes wrong in one script.
