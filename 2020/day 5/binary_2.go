package main

import (
    "fmt"
	"bufio"
	"os"
	"log"
    "strings"
	"strconv"
	"sort"
	
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	ids := []int{}
	for scanner.Scan() {
		line := (scanner.Text())

		res := strings.ReplaceAll(line, "R", "1")
		res = strings.ReplaceAll(res, "L", "0")
		res = strings.ReplaceAll(res, "B", "1")
		res = strings.ReplaceAll(res, "F", "0")

		if result, err := strconv.ParseInt(res, 2, 64); err != nil {
			fmt.Println(err)
		} else {
			ids = append(ids , int(result))
		}
	}
	sort.Ints(ids)
	fmt.Println(ids)
	for i := range ids {
		if ids[i+1] != ids[i]+1 {
			println(ids[i]+1)
			break
		}
	}
}