ESO AddOns (Cadwell)
===

This is the first (baby) step to the Linux Version compliant Mod Manager for The Elder Scrolls Online - Cadwell. As in the game Cadwell is aimed to ease the installation and later mod management of ESOUI mods on linux OSes.

This role however is currently a brute-force method to get the most annoying parts - keeping mods up to date - out of the way.

Why not Minion Mod Manager?
---

Minion Mod Manager is unmaintained for more than two years now and relies on some pretty old libraries and the JavaFX Framework, which in itself is not maintained anymore. On newer Platforms it is basically not possible (especially the Open Source way) to use this Software. E.g. on Fedora the packages / depencencies for this are not provided and the currently only distributor (for RPM packages) Oracle demands too much private information in order to get access to their packages (which didn't even work for me on Fedora 32).

How to Use
---

This manager takes a List of `name, url` objects in the variable `esoaddons_addons` and downloads them from ESOUI in the latest version, stores them under `$HOME/.local/share/Cadwell/AddOns` and symlinks them to the default install location for the Steam Version of Elder Scrolls Online on Linux.

To add a Mod you have to provide a Name and fetch the URL to the download page of the Mod. Currently the role does not get the download URLs just by name. It's really just a bit less painful way to keep mods up to date.

In the future this mod manager will become a full python program with CLI to automate a lot of these things. For the beginning, downloading the latest mods is the most important it has to do.

*Note:* Due to the nature of this role, it will never reach idempotency.
