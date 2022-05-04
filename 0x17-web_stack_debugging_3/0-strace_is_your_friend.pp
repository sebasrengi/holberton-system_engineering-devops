# fixes Apache 500 error by fixing typo in wordpress
# Fiz error 500 Internal server error
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
    }