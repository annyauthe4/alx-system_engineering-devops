# Install flask from pip3 ensuring a specific version.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
