#!/usr/bin/env -S just --justfile

set windows-shell := ["powershell.exe", "-c"]
set shell := ["/bin/bash", "-c"]

alias build := build-package
alias lock := check-lockfile
alias setup := set-up-project
alias sync := sync-dependencies
alias tests := run-tests
alias venv := create-virtual-environment
alias clean := clean-generated-files

default:
    just --list

install-python:
    uv python install

create-virtual-environment:
    uv venv --seed --allow-existing

clean-generated-files:
    uv run --active --script --quiet scripts/clean.py

check-lockfile:
    uv lock --check

set-up-project: install-python create-virtual-environment sync-dependencies

sync-dependencies:
    uv sync --all-packages --all-groups --all-extras

build-package:
    uv run pyinstaller src/lwPython/main.py

run-tests:
    uv run pytest -vv
