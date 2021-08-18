---
layout: post
title: Deploying a Flask 2.x App Using Zappa
categories: [Flask, Python, Zappa, AWS]
---

I write application code, and my undestanding of cloud infrastructure is only barely better than my understanding of frontend development. While I'm always growing that cloud knowledge, I don't want to spend a lot of time fiddling with it just to get a weekend personal project deployed. So I was drawn to [Zappa](https://github.com/zappa/Zappa).

I use AWS in my day job, so I wanted to use it for my side project too. So I wanted a tool that would deploy a small [Flask](https://flask.palletsprojects.com/) app to [AWS Lambda](https://aws.amazon.com/lambda/) that would handle all the boring details. I considered just developing a [Chalice](https://github.com/aws/chalice) app instead of Flask, but I didn't want to use a framework for the app that is developed with a single cloud vender in mind. You may be saying, "but Ryan, Zappa only targets AWS", and you'd be right, but I'm still writing just a plain old Flask app that can be deployed in any number of ways to any number of vendors if/when I so choose.

But when I tried to follow the very simple steps as advertised on the side of the tin:

```bash
$ pip install zappa
$ zappa init
$ zappa deploy
```

I was met with a very frustrating error simply upon pip installing zappa:

```console
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
flask 2.0.1 requires Werkzeug>=2.0, but you have werkzeug 0.16.1 which is incompatible.
```

Oh dear, what to do? There [are](https://github.com/Miserlou/Zappa/issues/2036) [open](https://github.com/zappa/Zappa/issues/984) [issue's](https://github.com/zappa/Zappa/issues/1003) on the Zappa Github Repo dating back to February 2020 😱. I don't know what's going on with Zappa, and this issue neglect is a pretty big red flag, but the alternatives ([Architect](https://github.com/architect/architect), [serverless](https://www.serverless.com/), etc.) are appear to be more complex than I wanted for a weekend side project.

But in the Github Issues, there was [enough](https://github.com/zappa/Zappa/issues/984#issuecomment-863926723) [information](https://github.com/zappa/Zappa/issues/984#issuecomment-863932455) on how to circumnavigate this problem that I turned a blind eye to the warning signs, and moved forward with Zappa. Here is how I did it.

- I forked Zappa and made [these changes](https://github.com/zappa/Zappa/compare/master...dissolved:update_requirements) (which also adds support for Python 3.9.x)
- Then I pip installed directly from my fork like this:
```bash
python -m pip install git+https://github.com/dissolved/Zappa.git@update_requirements#egg=zappa
```

And thats it (unless I forgot something)! Now I'm deploying my tiny Flask app to AWS Lambda.
