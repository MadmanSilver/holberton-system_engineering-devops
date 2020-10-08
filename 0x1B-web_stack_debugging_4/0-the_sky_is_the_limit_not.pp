# setting a high default limit for nginx
file {'/etc/default/nginx':
  ensure  => present,
  path    =>  '/etc/default/nginx',
  content => 'ULIMIT="-n 4096"',
} ~>
service { 'nginx':
  ensure => running
}
