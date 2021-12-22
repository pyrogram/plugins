# Pyrogram Plugins

> A collection of Pyrogram plugins made by the community

[Pyrogram Smart Plugins](//docs.pyrogram.ml/resources/SmartPlugins) allow users to create and easily share modular framework's components with minimal boilerplate code. This repository is meant to collect awesome Pyrogram plugins.

## Using Plugins

- Create a new folder in your working directory (e.g.: *plugins*).
- [Download](https://github.com/pyrogram/plugins/archive/master.zip) and copy the desired plugin(s) into your *plugins* folder.
- Enable plugins in your Client by telling Pyrogram to search on your folder with `plugins=dict(root="plugins")`:
  ```python
  from pyrogram import Client

  app = Client("my_account", plugins=dict(root="plugins"))
  ```
- Done! Run your client with `app.run()`, the plugins will be automatically loaded.

[**More details**](https://docs.pyrogram.org/topics/smart-plugins#using-smart-plugins)

## Adding Plugins

- Understand how [Smart Plugins](https://docs.pyrogram.org/topics/smart-plugins) work.
- Create an awesome plugin.
  - Make a folder for your plugin and choose a meaningful name.
  - Create a python file named the same inside your plugin folder.
  - If necessary, create a `requirements.txt` file and add all the dependencies your plugin needs.
- Open a new [Pull Request](https://github.com/pyrogram/plugins/compare) to propose adding your plugin inside the [plugins](plugins) directory.
  - Make sure you add a proper license and your name to it.
  - Also edit the readme to add the plugin in the list below.

## Improving Plugins

You found a bug on a plugin or want to extend one? Or maybe you have ideas on how the plugin system can be improved? That's great! Open a new GitHub [Issue](issues/new) and let's discuss about it.

## Plugins Collection

Name | Description | Usage
:--- | :--- | :---
[**haste**](plugins/haste), by [delivrance](//github.com/delivrance) | Upload text to hastebin.com and send its link | Reply to a group chat text message with `!haste`
[**welcome**](plugins/welcome), by [delivrance](//github.com/delivrance) | Greet new members with a welcome message | Run and wait for new members to join your groups
[**eval**](plugins/eval), by [Furoin](//github.com/Furoin) | Evaluate a Python expression and send the result | Example: `!eval 1+2+3`
[**replace**](plugins/replace), by [brightside](//github.com/bright5ide) | Search and Replace a part of a message to suggest user if he meant something else  | Reply to a group chat text message with `!r <old>/<new>`
