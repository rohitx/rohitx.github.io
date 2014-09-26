---
layout: post
title: Starting mySQL on Mac 
tags: sql 
summary: I have installed mySQL, but how do I start it?
---
This is something that happens to new SQL users. "I installed mySQL with Homebrew. Now: 

1.  How do I start mysql session? 
    It is as easy as typing 'mysql'
2.  When I reboot my computer and type <span class="green">'mysql'</span> I get the following message <span class="red">"ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock"</span>. Why is this? 
The answer to question is very simple: start the sql server in the following way: 

<span class = "green">mysql.server start</span>

 Once you have it, type mysql and violà, we have the mysql server running. 

I hope this helps people who are trying to find the answer to their problems. 