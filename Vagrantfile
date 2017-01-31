#-*- mode: ruby -*-
#vi: set ft=ruby :


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"


    config.vm.provider :aws do |aws, override|
        aws.access_key_id = 'access_key_id'
        aws.secret_access_key = 'secret_access_key'
        aws.keypair_name = 'eduardo'
        aws.ami = "ami-01f05461"
        aws.region = "us-west-2"
        aws.security_groups = ['cc']
        aws.instance_type = "t2.micro"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "ruta a .pem"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible.yml"
  end
end
