package main

import (
	"io/ioutil"
	"strings"
	"fmt"
	"strconv"
)


func main() {
	target := 1001938;
	data , _ := ioutil.ReadFile("input.txt")
	str := strings.TrimSpace(string(data))
	times := []string{}
	for _ , row :=  range strings.Split(str , ",") {
		times = append(times , row)
	}
	fmt.Print(times)
	found := false
	count := target
	for !found {
		for _ , val := range times {
			intval , _ := strconv.Atoi(val)
			if val != "x" && count % intval == 0 {
				found = true
				fmt.Print((count-target)*intval)
			}
		}
		count++ 
	}


	
}