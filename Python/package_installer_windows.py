#!/usr/bin/env python3

from os import system as cmd

cmd(r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command ' + '"iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))"')
cmd(r'SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"')

cmd('choco install sublimetext3 -y')    # Sublime Text
cmd('choco install vscode -y')          # VSCode
cmd('choco install git -y')             # git