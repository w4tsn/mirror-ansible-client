Ansible Client Deployment
===

This repository provides the ability to install your Client in a few minutes.

We setup various things, like updating your client to the latest state, install packages like VSCode, VLC, Tilix and more, to take your whole client into a working state.

Usage
---

Clone the repository, and use `ansible-playbook` to run it.

Optionally in order to use the `optional` roles not included in the default `clients.yml` playbook make a copy of it with the filename `custom.yml`, which is part of `.gitignore` by default.

Also install `Python2`, since it is required by ansible and e.g. Fedora decided to not ship it anymore since F29.

### Fedora

```bash
sudo dnf install git ansible python
git clone https://octo.sh/ansible-client/ansible-client.git
cd ansible-client
ansible-playbook clients.yml
```

### Extend/personalize your setup

To extend the default packages you can use `extend_packages` in your `host_vars/localhost` file.

To install [`cowsay`](https://en.wikipedia.org/wiki/Cowsay) for example:

```yaml
---

extend_packages:
  - dnf: cowsay

```


Development
---

Feel free to extend this repository with your own idea. It would be lovely to see Pull Requests and more. :wave:
