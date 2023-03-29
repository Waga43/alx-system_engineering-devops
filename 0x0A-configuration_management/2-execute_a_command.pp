# Using Puppet, create a manifest that kills the killmenow
# process using pkill and exec
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow'
}
