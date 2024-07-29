# This manifest kills the 'killmenow' process

exec {'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  returns => [0, 1],
}
