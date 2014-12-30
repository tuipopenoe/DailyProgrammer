## Description
Website URLs, or Uniform Resource Locators, sometimes embed important data or arguments to be used by the server. This entire string, which is a URL with a Query String at the end, is used to "GET#Request_methods)" data from a web server.
A classic example are URLs that declare which page or service you want to access. The Wikipedia log-in URL is the following:
http://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page
Note how the URL has the Query String "?title=..", where the value "title" is "Special:UserLogin" and "returnto" is "Main+Page"?
Your goal is to, given a website URL, validate if the URL is well-formed, and if so, print a simple list of the key-value pairs! Note that URLs only allow specific characters (listed here) and that a Query String must always be of the form "<base-URL>[?key1=value1[&key2=value2[etc...]]]"

### Input
String GivenURL - A given URL that may or may not be well-formed.

#### Sample Input
http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit


### Output
If the given URl is invalid, simply print "The given URL is invalid". If the given URL is valid, print all key-value pairs in the following format:
key1: "value1"
key2: "value2"
key3: "value3"
etc...

#### Sample Output
title: "Main_Page"
action: "edit"