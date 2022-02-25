# Sky is the limit, let's bring that limit higher

exec { 'limit--for-nginx':
  command  => 'bin/sed -i "s/15/4098/" /etc/default/nginx'
}

exec { 'restart-nginx':
  command => 'service nginx restart',
  require => Exec['limit--for-nginx'],
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
