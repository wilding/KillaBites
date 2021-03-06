apt-get -qqy update
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
apt-get -qqy install git
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb killabites'
# su vagrant -c 'psql killabites -f /vagrant/killabites/killabites.sql'

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd
