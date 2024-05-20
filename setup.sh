#!/bin/bash
#Genome Inspector Installation

linux() {
	#echo 'linux'
	sleep 3.0 
	sudo mkdir /etc/genome_inspector > /dev/null 2>&1
	sudo mv * /etc/genome_inspector/ > /dev/null 2>&1
	sudo cp /etc/genome_inspector/Genome_Inspector.py /bin/ > /dev/null 2>&1
	sudo chmod +x /bin/Genome_Inspector.py > /dev/null 2>&1
	sudo chmod +x /etc/genome_inspector/Genome_Inspector.py > /dev/null 2>&1
	sudo cp /etc/genome_inspector/geneinspect /bin/ > /dev/null 2>&1
	sudo cp /etc/genome_inspector/geneinspect $HOME > /dev/null 2>&1
	sudo chmod +x /bin/geneinspect > /dev/null 2>&1
	sudo chmod +x $HOME/geneinspect > /dev/null 2>&1
	install_success
	destruct
}

#Installation success
install_success() {
	clear
	echo
	echo -e '\e[92m[ Genome Inspector Installed Successfully ]\e[0m'
	echo
	sleep 1.0
	echo -e 'Type \e[92m"geneinspect"\e[0m and hit Enter to start'
	echo
	echo 'Do you want to run a program?'
	echo '[1] Yes'
	echo '[2] No'
	echo
	read -p "Select option [1/2]: " RUN
	start
}

start(){
	if [[ $RUN == 1 ]]; then
		clear
		geneinspect
	elif [[ $RUN == 2 ]]; then
		echo
		destruct
		exit 
	else
		echo -e '\e[31mInvalid input!\e[0m'
		sleep 1.0
		install_success
	fi
}	

#Self destruction - remove all files
destruct() {
	rm -rf ../genome_inspector > /dev/null 2>&1
}

#run program
exit