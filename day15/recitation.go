package main

import (
	"fmt"
)

func main() {
	data := []int64{1,20,8,12,0, 14}
	fmt.Println(game(data))
}

func game(data []int64 ) int64 {
    IsInPast := true
	temp := int64(0)
	past := make(map[int64]int64)
	
	for i , n := range data {
		past[n] = int64(i+1)
	}
	prev := past[int64(len(past)-1)]
	
	for i := len(past)+1 ; int64(i) <= 2020 ; i++ {
		if IsInPast {
			prev = 0;

		} else {
		    prev = temp

		}
		
		key , val := past[prev]
		past[prev] = int64(i)
		if val {
			temp = int64(i) - key
		}
		
		
		IsInPast = !val
	}
	return prev
}