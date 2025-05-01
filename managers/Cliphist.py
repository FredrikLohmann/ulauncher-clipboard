import os
import subprocess
import json
from shutil import which
from lib import exec_get, pid_of, show_message

name = 'Cliphist'
client = 'cliphist'
paste_agent = "wl-paste"
copy_agent = "wl-copy"

def can_start():
    return bool(which(client))

def is_running():
    return bool(pid_of(paste_agent))

def is_enabled():
    return True

def start():
    subprocess.Popen([paste_agent, "--watch", client ,'store'])

def add(text):
    subprocess.call([copy_agent, text])

def get_history():
            show_message(
            'ulauncher-clipboard error',
            "get history",
            'dialog-error'
        )
    val=json.loads(exec_get(client, 'list'))
    return val

