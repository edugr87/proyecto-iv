#-*- mode: ruby -*-
#vi: set ft=ruby :
Vagrant.require_plugin 'vagrant-aws'
Vagrant.require_plugin 'vagrant-omnibus'

Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"


    config.vm.provider :aws do |aws, override|
        aws.access_key_id = 'clave id'
        aws.secret_access_key = 'secretacceskey'
        aws.keypair_name = 'eduardo'
        aws.ami = "ami-5189a661"
        aws.region = "us-west-2"
        aws.security_groups = ['cc']
        aws.instance_type = "t2.micro"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "eduardo.pem"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "ansible.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
