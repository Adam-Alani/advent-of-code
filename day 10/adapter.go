package main

import (
    "fmt"
	"io"
	"os"
	"sort"
)

func main() {
	file, err := os.Open("input.txt")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var perline int 
	var data []int
	for {

		_, err := fmt.Fscanf(file, "%d\n", &perline) // give a patter to scan

		if err != nil {

				if err == io.EOF {
						break // stop reading the file
				}
				fmt.Println(err)
				os.Exit(1)
		}

		data = append(data, perline)	
		
	}
	sort.Ints(data)
	part1(data)
}

func part1(data []int) int{
	one := 0
	three := 1
	total := 0
	for _ , val := range data {
		diff := val - total
		total = val
		if diff == 1 {
			one++
		}
		if diff == 3 {
			three ++
		}
	}
	return total
}