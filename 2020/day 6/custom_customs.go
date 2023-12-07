package main

import (
	"fmt"
	"strings"
	"io/ioutil"

)

func main() {
	data , _ := ioutil.ReadFile("input.txt")
	//println(data)
	//puzzle1(data)
	puzzle2(data)


}



func puzzle1(data []byte) int { 

	var total int
	var groupsum int
	alph := "abcdefghijklmnopqrstuvwxyz"
	
	for _ , group := range strings.Split(string(data), "\n\n") {
		for _ , line := range strings.Split(group, "\n") {
			
			if (len(line) == 1) {
				total += groupsum
				groupsum = 0
				alph = "abcdefghijklmnopqrstuvwxyz"
			}
			for _ , str := range line {
				char := string(str)
				if strings.ContainsAny(alph , char) {
					groupsum ++
					alph = strings.ReplaceAll(alph , string(str) , "")
				}
			}
		}
	}
	print(total)
	return total
}

