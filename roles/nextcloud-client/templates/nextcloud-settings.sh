#!/bin/sh

NEXTCLOUD_DIR=$HOME/.local/share/data/Nextcloud
NEXTCLOUD_CFG=$NEXTCLOUD_DIR/nextcloud.cfg
NEXTCLOUD_SYNC_DIR="{{ nextcloud_sync_dir }}"

if [ "$(/usr/bin/id -u)" -gt 999 ]; then

    if [ ! -e "$NEXTCLOUD_CFG" ]; then
        mkdir -p "$NEXTCLOUD_DIR"
        mkdir -p "$NEXTCLOUD_SYNC_DIR"
        cat <<EOF >"$NEXTCLOUD_CFG"
[Accounts]
0\Folders\1\ignoreHiddenFiles=true
0\Folders\1\localPath=$NEXTCLOUD_SYNC_DIR
0\Folders\1\targetPath={{ nextcloud_path }}
0\url=https://{{ nextcloud_url }}
0\user={{ nextcloud_user }}
EOF

    fi
fi
