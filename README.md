# Zpi

Zpi is a simple zsh plugin manager written in python.  

**This project is still not completely finished** 

## Features
* Zpy only runs when called by you
* Thus don't add a second to the shell startup time
* Manage plugins and theme from any vcs such as github
* Update all the plugins

## Installation

Clone this repo and run zpy.py.

```bash
git clone https://github.com/yogeshdcool/zpy
cd zpy
python zpy.py
```
add the script to path for convinience
```bash
mv zpy.py ~/.local/bin
```

## Configuration
The plugins should be mentioned as repo/plugin in your zconfig(defult is ~/.zshrc) between zpy begin and zpy end and all the lines should start with a # including the zpy ones
```
#zpy begin
#   zsh-users/zsh-completions
#     zsh-users/zsh-autosuggestions
#zsh-users/zsh-history-substring-search
# zdharma-continuum/fast-syntax-highlighting


#zpy end
```
You variables can also be changed in zpy.py
```python
zconfig = "~/.zshrc"  # this is where you should write your plugin names
pluginZsh = "~/.zplugins/zplugins.zsh"  # thes file contains source [plugin] and should be sourced in zconfig
pluginDir = "~/.zplugins"  # this is where plugins will be stored
```
## Roadmap
* Enable arguments
* Option to enable zsh-defer
* Option to enable zcompile
* Use remote and local files as plugin/theme
* Pleasant output with colors
* Add support for other shells

## Why
So many plugin managers already exists but I wanted to make one that doesn't affect the shell shartup time and wanted it to be simple as possible  


## Authors

- [@Yogesh(me)](https://www.github.com/yogeshdcool)


## Contributing
As this is my first big project bugs can be expected and there will be a lot of room for improvements  

So pull requests are more than welcome.


## License
[gpl-3.0](https://choosealicense.com/licenses/gpl-3.0/)