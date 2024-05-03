build: deps apk

test: deps test
	echo "testing ..."

deps: 
	pip3 install -r requirements.txt

apk: deps
	buildozer android debug

run: deps 
	buildozer android deploy run