#!/usr/bin/env -S just --justfile

set shell := ["/bin/bash", "-c"]

alias build := build-package
alias lock := check-lockfile
alias setup := set-up-project
alias sync := sync-dependencies
alias tests := run-tests
alias venv := create-virtual-environment

default:
    just --list

install-python:
    uv python install

create-virtual-environment:
    uv venv --seed --allow-existing

check-lockfile:
    uv lock --check

set-up-project: install-python create-virtual-environment sync-dependencies

sync-dependencies:
    uv sync --all-packages --all-groups --all-extras

build-package:
    pyinstaller src/textract/main.py

run-tests:
    uv run pytest -vv
