# fixes Apache 500 error by fixing typo in wordpress
# Fiz error 500 Internal server error
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
