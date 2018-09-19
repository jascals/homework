#!/usr/bin/perl 

# 只有 R 会转换为大写
$str = "\urunoob";
print "$str\n";

# 所有的字母都会转换为大写
$str = "\Urunoob";
print "$str\n";

# 指定部分会转换为大写
$str = "Welcome to \Urunoob\E.com!"; 
print "$str\n";

# 将到\E为止的非单词（non-word）字符加上反斜线
$str = "\QWelcome to runoob's family";
print "$str\n";

$var='这是一个使用

多行字符串文本

的例子/n';

print "$var\n";

$v = 123;
$s = "tom";
@c=(1,2,3);
%h=('a'=>1,'b'=>2);

print "$v\n";
print "@c[1]\n";
