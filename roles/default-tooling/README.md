default-tooling
===

Tilix
---

To enable tilix support in bash add the following to `~/.bashrc`:

```bash
# Tilix
if [ $TILIX_ID ] || [ $VTE_VERSION ]; then
        source /etc/profile.d/vte.sh
fi
```
