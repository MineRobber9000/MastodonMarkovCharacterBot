# MastodonCharacterMarkovBot

A markov bot for Mastodon. Designed for use with character quotes. Can also be used as a regular bot.

Used for [salty gem](https://botsin.space/@SaltyGem).

## How to use
### Setup
#### Credentials
Run `getAccessToken.py` and input the things it asks for.

What you need to do next depends on whether you're using this as a markov bot or a bot framework.

#### Use case: Markov bot
Edit corpus.txt and fill it with lines for your bot to say.

#### Use case: Bot framework
Replace action.py with a module of your own creation that has a makeToot function.

### Usage
Run `main.py`. It will use the `action` module's `makeToot` function to make a toot and publish it.

## Networking

One benefit of having an easily modifiable action module is that you can network easily.

Have multiple bots using characters from the same show? Modify `action.py` to replace character names with handles!
