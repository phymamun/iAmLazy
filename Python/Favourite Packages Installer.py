#!/usr/bin/env python3

"""
	Installer for my favourite packages
	of debian based distro.
	Supports:
		* Debian
		* Arch (Not Yet)
	It's a helper for me
	if i somehow destroy my system (it happens to me)
	Then I would be able to automate the boring staffs.
	Author: Rakibul Yeasin
	FB: https://www.facebook.com/dreygur

	***Not Licensed***
"""

import sys
import subprocess
from os import system, remove, getcwd
# from lsb_release import get_lsb_information
#   TO-DO: Implementaion of LAMP Installation from Maateen of make it myself

class Primary():
	""" This Class is for installation of the primary packages """

	def __init__(self):
		# Class Initialization
		pass

	def deb_primary(self):
		"""
		Some Basic Operations on a newly installed Distro
		"""
		#   This will install add-apt-repository
		system('sudo apt install -y software-properties-common')
		system('sudo apt install -y python-software-properties')
		update()
		#   Installs Vim, gDebi, GParted, Synaptic
		system('sudo apt install -y git git-core')
		system('sudo apt install -y vim gdebi gparted synaptic')
		system('sudo apt install -y curl php5-curl')
		system('sudo apt install -y gcc g++')
	
	def deb_qbittorrent(self):
		"""
		Installs and cobfigures qBittorrent Client
		"""
		#   This will install qBittorrent Stable
		system('sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable -y')
		update()
		system('sudo apt-get install qbittorrent -y')
		system('cp ../Assets/qBittorrent.conf ~/.config/qBittorrent/')

	def deb_libre_office(self):
		#   Installs Libre Office
		#   The replacement of Microsoft Office
		system('sudo add-apt-repository ppa:libreoffice/ppa -y')
		update()
		system('sudo apt install -y fonts-opensymbol libreoffice-avmedia-backend-gstreamer \
				libreoffice-base-core libreoffice-calc libreoffice-common libreoffice-core \
				libreoffice-draw libreoffice-gnome libreoffice-gtk2 libreoffice-help-en-us \
				libreoffice-impress libreoffice-math libreoffice-ogltrans libreoffice-pdfimport \
				libreoffice-style-breeze libreoffice-style-galaxy libreoffice-writer')

class Media():
	""" Class for Media Players """

	def __init__(self):
		# Class Initialization
		pass

	def deb_rhythmbox(self):
		#   Rhythnbox - Music Player
		system('sudo add-apt-repository ppa:fossfreedom/rhythmbox -y')
		update()
		system('sudo apt install rhythmbox -y')

	def deb_vlc(self):
		#   VLC - Video Player
		update()
		# Install VLC and VLC-Browser Plugin
		system('sudo apt-get install vlc browser-plugin-vlc -y')

class Browser():
	""" This Class is for installation of the Browsers I Need """

	def __init__(self):
		# Class Initialization
		pass

	def deb_chrome(self):
		#   Installs Google Chrome
		system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
		# Installing Google Chrome
		system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
		system('sudo apt install -fy')
		remove('google-chrome-stable_current_amd64.deb')
		#update()

	def deb_firefox(self):
		#   Removes Firefox-ESR and installs Firefox Quantum
		# Uninstalls Firefox ESR from Debian/Ubuntu/Mint/Kali
		system('sudo apt remove --purge firefox -y')
		update()
		# Installs Firefox Quantum
		system('sudo apt install firefox -y')

class IDE():
	""" This Class is for installation of the IDE's I Love to use """

	def __init__(self):
		# Class Initialization
		pass

	def deb_vscode(self):
		# Installs Microsoft Visual Studio Code
		# Download Deb Package
		system('wget -O vscode.deb https://go.microsoft.com/fwlink/?LinkID=760868')
		# Install vscode
		system('sudo dpkg -i vscode.deb')
		system('sudo apt install -fy')
		system('rm vscode.deb')

	def deb_subl(self):
		# Installs Sublime Text-3 Stable
		# Install the GPG Key
		system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
		# Ensure apt is set up to work with https sources
		system('sudo apt-get install apt-transport-https -y')
		# Select the stable channel
		system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
		update()
		# Install sublime-text
		system('sudo apt-get install sublime-text -y')

class ZSH():
	""" This Class is for installing and configuring zsh shell """

	def __init__(self):
		# Class Initialization
		pass

	def deb_install(self):
		# Installs ZSH Shell
		system('sudo apt-get install zsh -y')
		# Changes Default shell to zsh from bash

	def deb_custom_zsh(self):
		# Installs and customize zsh shell
		_current_directory = getcwd()
		# Downloads and Copies oh-my-zsh plugin
		system('sudo rm -rf ~/.oh-my-zsh')
		system('git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh')
		# Copy the Configuration file to Home Directory
		system('sudo cp ' + _current_directory + '/.zshrc ~/')

	def deb_zsh_fonts(self):
		# Installs the required pakages for oh_my_zsh
		# Installs powerlevel9k theme
		system('git clone https://github.com/bhilburn/powerlevel9k.git \
				~/.oh-my-zsh/custom/themes/powerlevel9k')
		# download and install powerline font and font configuration
		system('wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf')
		system('wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf')
		# Move the symbol font to a valid X font path. Valid font paths can be listed with "xset q" 
		system('mkdir -p ~/.local/share/fonts/')
		system('sudo mv -f PowerlineSymbols.otf ~/.local/share/fonts/')
		# Update font Cache
		system('fc-cache -vf ~/.local/share/fonts/')
		# Install the fontconfig file
		system('mkdir -p ~/.config/fontconfig/conf.d/')
		system('sudo mv -f 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/')
	def deb_change_shell(self):
		# Changing the Default shell from bash to zsh
		system('chsh -s $(which zsh)')

def get_distro():
	#   This function will get the codename of running Distro
	info = get_distro_information()
	return info['ID']

def update():
	"""
	  This function will download the package lists from the repositories and
	  "update" them to get information on the newest versions of packages and
	  their dependencies.
	"""
	distro = get_distro()

	if distro == "Debian":
		system('sudo apt-get -y update')
	elif distro = "Arch":
		system('sudo pacman -Syu --noconfirm')

def banner():
	#   Banner for the script
	text = """
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	\tHello {0}, Welcome!!!
	\tAuthor: Rakibul Yeasin
	\tFB: https://www.facebook.com/dreygur
	\tGithub: https://www.github.com/dreygur
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	"""

	#uname = system('grep "^${USER}:" /etc/passwd | cut -d: -f5')
	uname = subprocess.getoutput('whoami')
	print(text.format(uname.title()))

def main():
	"""
		And here comes the tradition MAIN function :)
		Though we don't need it But It's a tradition
		So, I just abided by...
	"""

	banner()
	permission = str(input('Are you ready to install??? (Y/n) ')).lower()
	distro = get_distro()

	if permission == 'y':
		try:
			if distro == 'Debian':
				print('Installing Primary Packages...\n')
				prm = Primary()
				prm.deb_primary()
				print('Done!\nInstalling "QBittorrent"...')
				prm.deb_qbittorrent()
				print('QBittorrent installed.\nInstalling "Libre Office"')
				prm.deb_libre_office()
				print('"Libre Office" installed.')
			elif distro == 'Arch':
				pass
		except:
			print('Sorry, Something went wrong!\nPrimary Packages Installation Failed.')
		
		try:
			if distro == 'Debian':
				print('Installing Browser...\n')
				brw = Browser()
				print('Installing "Firefox"...')
				brw.deb_firefox()
				print('"Firefox" installed.\nInstalling "Chrome"...')
				brw.deb_chrome()
				print('Done! Browser Installed.')
			elif distro == 'Arch':
				pass
		except:
			print('Sorry, Something went wrong!\nBrowser Installation Failed.')

		try:
			if distro == 'Debian':
				print('Installing Media Players...')
				mdw = Media()
				print('Installing "VLC Media Player"...')
				mdw.deb_vlc()
				print('"VLC Media Player" installed.\nInstalling "Rhythmbox"...')
				mdw.deb_rhythmbox()
				print('"Rhythbox" installed.')
			elif distro == 'Arch':
				pass
		except:
			print('Sorry, Something went wrong!\nMedia Player installation Failed.')

		try:
			if distro == 'Debian':
				print('Installing IDE\'s')
				ide = IDE()
				print('Installing "Sublime Text 3 Stable"...')
				ide.deb_subl()
				print('"Sublime Text 3 Stable" installed.\nInstalling "Microsoft VSCode"...')
				ide.deb_vscode()
				print('"Microsoft VSCode" installed.')
			elif distro == 'Arch':
				pass
		except:
			print('Sorry, Something went wrong!\nIDE installation Failed.')

		try:
			if distro == 'Debian':
				print('Installing ZSH...')
				zsh = ZSH()
				zsh.deb_install()
				zsh.deb_custom_zsh()
				zsh.deb_zsh_fonts()
			elif distro == 'Arch':
				pass
		except :
			print('Sorry Something went wrong. ZSH Installation or Customization failed.')

		print('Succefully Installed. Enjoy!!!!\nPlease "reboot" the system now.')
		_restart = str(input('Restart now? (Y/n) ')).lower()

		if _restart == 'y':
			system('reboot')
		else:
			print('Exiting...\n')
			sys.exit(1)

	else:
		print('You Choose to Exit. Exiting....\n')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("You choose to exit.\nExiting...")
		sys.exit(0)


# End of Code :(
