#!/usr/bin/python


# Configs
zconfig = "zshrc"  # this is where you should write your plugin names
pluginZsh = "zplugins/zplugins.zsh"  # thes file contains source [plugin] and should be sourced in zconfig
pluginDir = "zplugins"  # this is where plugins will be stored

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

zconfig = Path(os.path.expanduser(zconfig)).resolve()
pluginZsh = Path(os.path.expanduser(pluginZsh)).resolve()
pluginDir = Path(os.path.expanduser(pluginDir)).resolve()



def mkPluginDir():
    """Make sure PluginDir Exists."""
    try:
        print(f"Making sure {pluginDir} exists")
        os.mkdir(pluginDir)
    except FileExistsError:
        pass


def getPluginsName() -> list:
    """Get the names of the repo/plugin from the zsh config file.

    Returns:
        list: list of repo/plguin
    """
    print(f"Getting the plugin names from {zconfig}")
    with open(zconfig, "r") as file:
        plugins = []
        for line in file:
            if "zpy begin" in line:
                for plugin in file:
                    if not "zpy end" in plugin:
                        if plugin != "\n":
                            plugins.append(
                                plugin.replace("\n", "").replace('"', "")[1:]
                            )
                    else:
                        break
    return plugins


def writePluginsName():
    """Add "source plugin-init-filr" to the zsh config file."""
    print(f"Adding source [plugin] to {pluginZsh}")
    with open(pluginZsh, "w") as pluginsFile:
        for folder in os.listdir(pluginDir):
            folder = pluginDir / Path(folder)
            if folder.is_dir():
                for file in os.listdir(folder):
                    if "plugin.zsh" in file or "theme-zsh" in file:
                        pluginsFile.write(f'source "{pluginDir/folder/file}"\n')


def cloneRepo():
    """Clone the repo of plugins in PluginDir."""
    print("Cloning the plugin repos")
    for plugin in getPluginsName():
        s = subprocess.run(
            [
                "git",
                "-C",
                pluginDir,
                "clone",
                "--depth",
                "1",
                f"https://github.com/{plugin}",
            ],
        )


def updateRepo():
    """Updates all the plugin repo with a git pull."""
    print("Updating the plugins")
    for folder in os.listdir(pluginDir):
        folder = pluginDir / Path(folder)
        if folder.is_dir():
            os.chdir(folder)
            subprocess.run(["git", "pull"])


def install():
    """Main function that calls all the other function"""
    print("Installation started")
    if getPluginsName() == []:
        print(f"No plugins mentioned in {zconfig}")
        sys.exit()
    mkPluginDir()
    cloneRepo()
    writePluginsName()


parser=argparse.ArgumentParser()
parser.add_argument("-u","--update",action="store_true")
parser.add_argument("-i","--install",action="store_true")
args=parser.parse_args()

if args.update:
    print("Updating")
    updateRepo()

if args.install:
    print("Installing")
    install()

if __name__ == '__main__':
    if len(sys.argv)==1:
        print("The plugins mentioned are")
        print("\n".join(getPluginsName()))

