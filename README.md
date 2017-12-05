Ansible Client Deployment
===

This repository provides the ability to install your Client in a few minutes.

We setup various things, like updating your client to the latest state, install packages like VSCode, VLC, Tilix and more, to take your whole client into a working state.

Usage
---

Make sure you have an SSH key with access to this repository. If not replace the git clone command with an unzip of the downloaded `.zip` file from zip-download from GitHub.


### Fedora

```
sudo dnf install git ansible
git clone git@github.com:SISheogorath/ansible-client.git
cd ansible-client
ansible-playbook clients.yml
```

Development
---

Feel free to extend this repository with your own idea. It would be lovely to see Pull Requests and more. :wave:
