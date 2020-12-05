package main

import (
    "fmt"
	"bufio"
	"os"
	"log"
	"strings"
	"strconv"
	
)


func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var res int = 0
	for scanner.Scan() {
		line := (scanner.Text())
		
		linesplit := strings.Split(line , ":")
		password := strings.TrimSpace(linesplit[1])
		prefix := linesplit[0]

		splitstr := strings.Split(prefix , " ")
		numrange := splitstr[0]
		letter := splitstr[1]

		splitstr = strings.Split(numrange , "-")
		first := splitstr[0]
		firstint , err := strconv.Atoi(first)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		second := splitstr[1]
		secondint , err := strconv.Atoi(second)
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}

		var count int = 0 
		for i, str := range(password) {
			if strings.ContainsRune(letter, str) && firstint == (i+1) {
				count += 1
			}
			if strings.ContainsRune(letter, str) && secondint == (i+1) {
				count += 1
			}
		}
		if count == 1 {
			res += 1
		}
	}
	print(res)
}

