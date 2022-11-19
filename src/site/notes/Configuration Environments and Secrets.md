---
layout: note
tags:
  - tech
  - computer-science
  - personal-opinion
---

# Configuration, Environments and Secrets

## Configuration

A way to easily find and change the behavior of a program based on different intentions by changing the values of appropriate variables.

For example:

- Finding and changing the number of threads used by a program.
- Finding and changing the database URL used by a program.

So, configuration should be:

- Composed of variables and their values.
- Easy to find.
- Easy to change.

## Environments

A collection of values for different configuration variables defining a particular intention.

For example:

- A development environment containing a set of values for database URL, number of threads etc. that are tuned for serving the developer.
- A production environment containing a set of values for database URL, number of threads etc. that are tuned for serving the users.

So, environments should be:

- Composed of values for different configuration variables, including secrets.
- Properly isolated and protected.
- Easy to provision, but not very easy to change, as changing one value means changing the entire environment i.e. changing the intention.

## Secrets

Values that are not meant to be shared with the world.

For example:

- Database URL.

So, secrets should be:

- Encrypted.

## Combining All 3

- Configuration variables should be public and easy to find i.e. defined in the codebase of the program as a single source of truth, i.e. one single file.
- Values for configuration variables should either be public (defined in the codebase), or should come from the environment.
- Values that are defined in the codebase should not contain plain text secrets, but may contain encrypted secrets.
- Values that are defined in the environment should preferebly serve as switches, and may contain secrets.
- Environments should be encrypted, isolated and protected as they may contain secrets and access to critical services.

## Proof of Concept

- For each program, create a file containing all the configuration variables related to that particular program.
- The value of each variable should be either defined directly, or defined conditionally based on the environment.
  Example:
  ```
  number_of_threads = 10
  database_url = match env:
    case "dev": "dev_url"
    case "prod": environment.decrypt("prod_url")
    else: "default_url"
  ```
  See https://github.com/sayanarijit/enva
- Secret values or master password should come from the environment.
- If there is a common configuration defined separately in a common repo, only import the values, and define the variables explicitly for each program. So that it's easy to find.
- Define the environment specific values in the environment variables (/etc/environment). They are easy to provision, but requires reboot to change.
- Define secrets in git synced vault, with the master password defined as environment variable, or as a restricted file in user's home directory.
- Harden security of each environment.
