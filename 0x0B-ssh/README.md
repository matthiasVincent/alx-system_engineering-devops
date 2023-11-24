# 0x0B. SSH
In this project, interfacing securely with remote servers using SSH(Secure Shell) Protocol was examined.
Basically, secure shell protocol ensures that communication between a local/remote host and remote/another remote host is secured. It make use of pair of keys(public and private keys ).
The public key as the name indicate is what the client can share with any remote server for communication whereas the private key is exclusive to the client. It is a client-server protocol.
Server runs SSH daemon while client runs SSH client. Depending on the scenario, a remote server can also act as a client.

##Tasks

* **[ 0. use a private key](./0-use_a_private_key)**
Bash script that uses SSH to connect to a remote server using the private key in the file `~/.ssh/school` with the user `ubuntu`.

* **[ 1. create an SSH key pair](./1-create_ssh_key_pair)**
Bash script that creates an RSA key pair with requirements:
	* `school` as name of created private key
	* number of bits `4096`
	* key protected by the passphrase `betty`.
	
* **[ 2. client configuration file](./2-ssh_config)**
An answer file containing script that enables connection to a remote server without typing a password.
requirements:
	* use private key on the path `~/.ssh/school
	* refuse password based authentication

* **[ 4. client configuration file (w/puppet)](./100-puppet_ssh_config.pp)**
implement the tasks outlined in [this task](./2-ssh_config) using puppet configuration management tool.
