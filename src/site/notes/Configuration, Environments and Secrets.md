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
- A production environment containing a set of values for database URL, number of threads etc. that are tuned for serving the user.

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

- Configuration variables should be public and easy to find i.e. defined in the codebase of the program, preferably one single file.
- Values for configuration variables should either be public (defined in the codebase), or should come from the environment.
- Values that are defined in the codebase should not contain secrets, and should be common to all environments.
- Values that are defined in the environment may contain secrets and mostly be unique to each environment (except common secrets which are rare).
- Environments should be encrypted and protected as they will contain secrets.

## Proof of Concept

- For each program, create a file containing all the configuration variables related to that particular program.
- The value of each variable should be either defined directly, or defined conditionally based on the environment.
  Example:
  ```
  number_of_threads = 10
  database_url = match env:
    case dev: "dev_url"
    case prod: from_env("prod_url")
    else: "default_url"
  ```
  See https://github.com/sayanarijit/enva
- Secret values should come from the environment.
- If there is a common configuration defined separately in a common repo, only import the values, and define the variables explicitly for each program. So that it's easy to find.
- Define the environment specific values in the environment variables (/etc/environment). They are easy to provision, but requires reboot to change.
- Encrypt the environment variables. Decrypt during the provisioning.
- Harden security of each environment.
