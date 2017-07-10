#-*- mode: ruby -*-
#vi: set ft=ruby :


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"


    config.vm.provider :aws do |aws, override|
        aws.access_key_id ='key_id'
        aws.secret_access_key = 'access_key'
        aws.keypair_name = 'eduardo'
        aws.ami = "ami-835b4efa"
        aws.region = "us-west-2"
        aws.security_groups = ['vagrant']
        aws.instance_type = "t2.micro"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = 'rutaapen'
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible.yml"
  end
end
