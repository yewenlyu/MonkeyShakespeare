# Monkey Shakespeare - A Random File Generator

## Overview
**This program generates random large files of specified size on demand.** It is build to test file uploading on https://cloud.voltagedynamics.com/. The name of the project is inspired by [Infinite Monkey Theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem). 

## Motivation
Our uploading system performs MD5 Hash on each file, and thus duplicate file upload is not allowed. This makes testing upload a tedious process because it requires a large number of distinct large files.

## User Input Guard
Since it will be provided to our product team for testing, this program comes with a simple user interface, which aims to **handle all possible erroneous user input** (invalid/duplicate filename, invalid file size format, or large file size that could cause stack overflow) using Regular Expression. 

## Requirements
Python 3.0 or higher.
