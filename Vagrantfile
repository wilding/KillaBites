# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
    config.vm.box = "starboard/ubuntu-arm64-20.04.5"
    config.vm.box_version = "20221120.20.40.0"
    config.vm.box_download_insecure = true
    config.vm.provider "vmware_desktop" do |v|
        v.ssh_info_public = true
        v.gui = true
        v.linked_clone = false
        v.vmx["ethernet0.virtualdev"] = "vmxnet3"
    end
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 8000, host: 8000
end