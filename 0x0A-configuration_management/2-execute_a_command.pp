# This puppet manifest kills a process named killmenow using pkill.

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin'],
  unless  => 'test ! -f ./killmenow',  # Runs only if the file exists
}
