# Password Generator

A simple command line password generator I built in Python. This was Project 3 in my Python Programming training with DecodeLabs.

## What it does

You tell it how long you want your password to be, and it gives you a random one made of letters and numbers. If you type something silly, like a number that's too small or something that isn't a number at all, it just asks again.

## Why I used `secrets` instead of `random`

My first thought was to use the `random` module, but I learned that it isn't safe for passwords because its output can be predicted. The `secrets` module is made for this exact job, so that's what I went with.

## What I practiced

- Using the `secrets` module for secure randomness
- Using the `string` module for letters and digits
- Building strings with `join()`
- Handling bad input with `try/except`
- Using a `while` loop with `continue` and `break`

## How to run it

You'll need Python installed (you can get it at [python.org/downloads](https://www.python.org/downloads/)).

```bash
git clone https://github.com/dayod4606-tech/password-generator-python.git
cd password-generator-python
python password_generator.py
```

## Example

```text
--- PASSWORD GENERATOR ---
Enter password length (12): 2
Please choose a length of at least 4.
Enter password length (12): abc
That's not a number. Try again.
Enter password length (12): 16

Your generated password: l1eK5Ol58xsRDw95
```

## Things I might add later

- Special characters like `!` and `#`
- Letting the user pick which types of characters to include
- Making sure every password has at least one letter and one number

## About

Made as part of the Python Programming Industrial Training, Batch 2026, powered by DecodeLabs.
