#!/usr/env/python3 python
b=len,print,input,__import__
_a,_b,_p,_r=b[3]('sys').argv,b[3]('setup').mybuild,b[3]('functools').partial,b[3]('subprocess').run
s=shell=_p(_r,shell=1)
(i,p)=(installer,python)=(lambda x:s(f'pip install {x}'),lambda x:s(f'python {x}'))
def load(x,installer=i):
	try:return _b[3](x)
	except:return installer(x)
l=load
w=workcmd=lambda q,installer=i:(lambda _l=_p(l,installer=installer):((_l('setuptools'),_l('wheel'),_b())if(q)else(_l('twine'),p('-m twine upload dist/*'))))()
def main(*argv,_a=_a):
	L=b[0](argv)
	if L-1>0:
		match argv[1]:
			case 'build':w(1)
			case 'deploy':w(0)
			case _:b[1]('cmd must be build or deploy')
	elif L:main(None,b[2]('WARN : no param\ninput param : '))
	else:main(*_a)
if __name__=='__main__':main()
