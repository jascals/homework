#!/usr/bin/perl

$to = '2052829792@qq.com';
$from = 'jascal@littleforest.com';

$subject = 'jascal`s notice';
$message = 'test message';

open(MAIL, "|/usr/sbin/sendmail -t");

print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
print MAIL $message;

close(MAIL);
print "邮件发送成功\n";
