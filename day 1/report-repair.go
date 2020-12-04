package main

import (
    "fmt"
	"io"
	"os"
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
	report(data);

	secondreport(data);
}

func report(data []int) {
	for i := 0; i < len(data); i++ {
		for j := 0; j < len(data) ; j++ {
			if data[i] + data[j] == 2020 {
				fmt.Println(data[i]*data[j]);
			}
		}
	}
}

func secondreport(data []int) {
	for i := 0; i < len(data); i++ {
		for j := 0; j < len(data) ; j++ {
			for k := 0 ; k < len(data) ; k++ {
				if data[i] + data[j] + data[k] == 2020 {
					fmt.Println(data[i]*data[j]*data[k]);
				}
			}
		}
	}
}

