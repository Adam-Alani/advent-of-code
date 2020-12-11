package main

import (
	"io/ioutil"
	"strings"
	"fmt"
)

func main() {
	data , _ := ioutil.ReadFile("input.txt")
	str := strings.TrimSpace(string(data))
	board := [][]rune{}
	for _ , row :=  range strings.Split(str , "\n") {
		board = append(board , []rune(row))
	}
	fmt.Print(part1(board))
}



func part1(board [][]rune ) int {
	old := make([][]rune, len(board)) 
	for i := range old {
		old[i] = make([]rune, len(board[0]))
		copy(old[i], board[i])
	}

	new := make([][]rune, len(board)) 
	for i := range new {
		new[i] = make([]rune, len(board[0]))
	}


	state := nextGeneration(old , new )
	for state {
		old , new = new , old
		state = nextGeneration(old , new )
	}
	total := 0
	for _ , row := range new{
		for  _ , col := range row {
			if col == '#'  {
				total++
			}
		}
	}
	return total
}


func nextGeneration(board [][]rune , new [][]rune  ) bool {
	state := false	
	rows, cols := len(board), len(board[0])
	for i := 0 ; i < rows ; i++ {
		for j := 0 ; j < cols ; j++ {
			new[i][j] = board[i][j]
			if board[i][j] != '.'  {

				neighbours := countNeighbours(board , i , j )
				if board[i][j] == 'L' &&  neighbours == 0 {
					new[i][j] = '#'
					state = true
					
				} 
				if board[i][j] == '#' && neighbours >= 5 {
					new[i][j] = 'L'
					state = true

				}	
			}
		}
	}
	return state
}



func countNeighbours(board [][]rune , x , y int ) int {
	cells := 0
	possible := [][2]int { {1,1},{0,1},{-1,1}, {1,0},{-1,0}, {1,-1},{0,-1},{-1,-1},}

	for _ , p := range possible {
		dx, dy := x+p[0] , y+p[1]

		for 0 <= dx && 0 <= dy &&  dx < len(board) && dy < len(board[0]) {
			if board[dx][dy] == 'L' {
				break				
			}
			if board[dx][dy] == '#' {
				cells++
				break
			}

			dx += p[0]
			dy += p[1]

		}
	}
	return cells
}


