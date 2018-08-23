Hugo [optional]
===

Hugo is a static site generator written in Go. This software is not included in the base provisioning of this repository. It may be enabled by adding it locally to `custom.yml`, which is part of `.gitignore` by default.

*Note: When configured, this role may add a COPR repository. So pay attention.*

Variables
---

| Var | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| hugo_sass | bool | no | With `no` the native dnf package of hugo is installed, which is outdated and does not provide sass support. `yes` will require COPR, enable the COPR repo and install the package from there. |

Additional Information
---

* [Hugo Website](https://gohugo.io/)
* [Hugo Docs](https://gohugo.io/documentation/)
* [Getting Started Guide](https://gohugo.io/getting-started/)