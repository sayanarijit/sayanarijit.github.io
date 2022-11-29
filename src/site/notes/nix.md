---
layout: note
tags:
  - tech
  - computer-science
  - os
---

# Nix

Nix is a functional package manager with an interesting concept (that makes
actual sense), powered by the Nix lang, and powering the NixOS [[Linux]] distro.

I switched to NixOS when a package upgrade broke my Manjaro. It lets me define
my OS configuration and installed packaged declaratively, and allows me to
reproduce any revision of the config [I track in git](https://github.com/sayanarijit/.files).

In short, Nix is -

os package manager + zsh config + plugin manager + neovim config + plugin manager + xplr config manager + rust & cargo version and dependency manager + python & pip version and dependency manager + node version and package manager + yarn version and...

## Resources

- https://nix.dev/
- https://nixos.wiki/
- https://github.com/nix-community/
- https://peppe.rs/posts/novice_nix:_flake_templates/
- https://devenv.sh/
- https://cachix.org/
