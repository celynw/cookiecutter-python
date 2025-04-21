#!/usr/bin/env python3
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter
from git import GitConfigParser
from rich import print


def get_git_user_info():
	config = GitConfigParser([str(Path.home() / ".gitconfig")], read_only=True)
	try:
		name = config.get_value("user", "name")
	except Exception:
		name = "Your Name"
	try:
		email = config.get_value("user", "email")
	except Exception:
		email = "your.email@example.com"
	return name, email


def main():
	name, email = get_git_user_info()
	print("Getting user information from git config...")
	cookiecutter(
		template=str(Path(__file__).parent),
		extra_context={
			"author": name,
			"email": email,
		},
	)


if __name__ == "__main__":
	typer.run(main)
