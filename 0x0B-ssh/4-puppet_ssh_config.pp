# Sets ssh config values
include stdlib
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => '    BatchMode yes',
}

file_line { 'Declare identity file':
  path =>  '/etc/ssh/ssh_config',
  line =>  '    IdentityFile ~/.ssh/holberton'
}
