# This Puppet manifest configures the SSH client to use a private key and disable password authentication.

file { '/home/annyauthe4/.ssh/ssh_config':
  ensure  => 'file',
  content => @("CONFIG"/),
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
    | CONFIG
  mode    => '0600',
  owner   => 'annyauthe4',
  group   => 'annyauthe4',
}
