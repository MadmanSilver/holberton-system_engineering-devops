# Fixes a typo that causes an internal server error

exec {'sed':
  command => "sudo sed -i 's,phpp,php,' /var/www/html/wp-settings.php",
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
