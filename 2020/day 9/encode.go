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
	part1(data)
	part2(data)
}


func part1(data []int) int{
	n := len(data)
	for i:= 25 ; i < n ; i++ {
		toCheck := data[i-25: i+1]
		check := false
		for _ , j := range toCheck {
			for _ , k := range toCheck {
				if j + k == data[i+1] {
					check = true
				}}}
		if !check {
			fmt.Print(data[i+1])
			return data[i+1]
		}}
	return 0
}

func part2(data []int) int {
	arr := data[:]
	n := len(data)
	total := 32321523
	for i := 0 ; i < (n-1) ; i++ {
		curr := arr[i]
		j := i + 1
		for j <= n {
			if curr == total {
				res := arr[i:j]
				sort.Ints(res)
				print(res[0] + res[len(res)-1])
				return 1
			}
			if curr > total || j == n {
				break
			}
			curr = curr + arr[j]
			j++
		}		
	}
	return 0
}