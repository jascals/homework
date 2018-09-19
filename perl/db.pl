#!/usr/bin/perl -w

use strict;
use DBI;

my $host = "localhost";         # 主机地址
my $driver = "mysql";           # 接口类型 默认为 localhost
my $database = "perldb";        # 数据库
# 驱动程序对象的句柄
my $dsn = "DBI:$driver:database=$database:$host";  
my $userid = "root";            # 数据库用户名
my $password = "123";        # 数据库密码

# 连接数据库
my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
my $sth = $dbh->prepare("SELECT * FROM user");   # 预处理 SQL  语句
$sth->execute();    # 执行 SQL 操作

while ( my @row = $sth->fetchrow_array() )
{
       print join('	', @row)."\n";
}

$sth->finish();
$dbh->disconnect();

