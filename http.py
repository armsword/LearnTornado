#coding=utf-8
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep
import string

class MainHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith(".html") or self.path.endswith(".htm") or self.path.endswith(".txt"):
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return

			if self.path.endswith(".py"):
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return

		except IOError:
			self.send_error(404,'File Not Found:%s' %self.path)
	def do_POST(self):
		try:
			ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
			print ctype # application/x-www-form-urlencoded 表单
			print pdict # {}
			# 处理上传文件
			if ctype == 'multipart/form-data':
				query = cgi.parse_multipart(self.rfile,pdict)
			self.send_response(301)
			self.end_headers()

			upfilecontent = query.get('mypicture')
			#print upfilecontent
			print "filecontent",upfilecontent[0]
			self.wfile.write("<HTML>POST OK.<BR>")
			self.wfile.write(upfilecontent[0])

		except:
			pass



def main():
	try:
		server = HTTPServer(('',8080),MainHandler)
		print "Starting The Http Server!"
		server.serve_forever()
	except KeyboardInterrupt:
		print "Shutting down The Server"
		server.socket().close()

if __name__ == "__main__":
	main()
