#This pupppet scripts assure an nginx installation

package {'nginx':
ensure => installed,,
name   => 'nginx',
}

service { 'nginx':
ensure     => running,
enable     => true,
hasrestart => true,
require    => Package['nginx'],
subscribe  => File_line["add redirect"],
}

file {'/etc/nginx/html/index.html':
ensure  =>  present,
path    => '/etc/nginx/html/index.html',
content => 'Hello World!\n',
}

file_line {'add redirect':
ensure  => present,
path    => '/etc/nginx/sites-available/default',
replace => true,
line    => '	rewrite /redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
match   => '# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000',
}
