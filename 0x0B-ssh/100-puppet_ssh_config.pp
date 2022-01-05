# Puppet

file_line { 'file':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'skip password':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => 'PasswordAuthentication no',
}
