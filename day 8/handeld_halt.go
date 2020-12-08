//Draft, Doesnt work yet 

package main

import (
	"io/ioutil"
	"strings"
	"strconv"
)

func main() {
	data , _ := ioutil.ReadFile("input.txt")
	step := strings.Split(strings.TrimSpace(string(data)), "\n")
	halt(step)
	

}


func halt(step []string) (int) {
	var acc int
	var i int
	s := make(map[string]bool)
	for true {
		if s[string(i)]{
			return acc
		}
		s[string(i)] = true
		line := step[i]
		line = strings.Split(line , "")
		val := line[1]
		inst := line[0]
		val , _ = strconv.Atoi(val)

		println(step)


		i += 1

	}

	return acc
}


