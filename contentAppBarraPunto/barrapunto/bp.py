#!/usr/bin/python

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
import urllib2

def normalize_whitespace(text):
    return string.join(string.split(text),' ')

class myCounterHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.line = ""

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.title = normalize_whitespace(self.theContent)
                #line = "Title : " + self.theContent + "."
                #self.title = normalize_whitespace(self.theContent)
                self.inContent = False
                self.theContent = ""
                #print line.encode('utf-8')
            elif name == 'link':
                self.link = normalize_whitespace(self.theContent)
                self.line = "<li><a href =" + self.link + ">"+ self.title +"</a></li></br>"
                self.inContent = False
                self.theContent = ""


    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
# Load parser and driver
def get_fich():
    Parser = make_parser()
    Handler = myCounterHandler()
    Parser.setContentHandler(Handler)
    print "Good job, parse complete ! "
    # Ready, set, go!
    fich = urllib2.urlopen('http://barrapunto.com/index.rss')
    Parser.parse(fich)
    return Handler.line

    print "Parse complete"
