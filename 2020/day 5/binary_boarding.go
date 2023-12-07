package main

import (
    "fmt"
	"bufio"
	"os"
	"log"
    "strings"
	"strconv"
	
)

func main2() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var final int64 = 0
	for scanner.Scan() {
		line := (scanner.Text())

		res := strings.ReplaceAll(line, "R", "1")
		res = strings.ReplaceAll(res, "L", "0")
		res = strings.ReplaceAll(res, "B", "1")
		res = strings.ReplaceAll(res, "F", "0")

		if result, err := strconv.ParseInt(res, 2, 64); err != nil {
			fmt.Println(err)
		} else {
			fmt.Println(result)
			if result > final {
				final = result
			}
		}
	}
	println(final)

}