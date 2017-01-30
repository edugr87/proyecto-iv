#-*- mode: ruby -*-
#vi: set ft=ruby :


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    config.vm.network "public_network"
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.define "localhost" do |l|
            l.vm.hostname = "localhost"
    end

    config.vm.provider :aws do |aws, override|
        aws.access_key_id = ENV['AWS_KEY']
        aws.secret_access_key = ENV['AWS_SECRET']
        aws.keypair_name = ENV['AWS_KEYNAME']
        aws.ami = "ami-d990e1e9"
        aws.region = "us-west-2"
        aws.security_groups = "default"
        aws.instance_type = "t2.micro"
        aws.security_groups = "default"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "./eduardo.pem"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "ansible.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
