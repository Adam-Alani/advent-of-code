package main

import (
	"bufio"
    "log"
    "os"
)

func main() {
	board , err := readLines("input.txt")

	if err != nil {
        log.Fatalf("readLines: %s", err)
    }

	prod := toboggan(1 , 1 , board)*toboggan(3 , 1 , board)*toboggan(5 , 1 , board)*toboggan(7 , 1 , board)*toboggan(1 , 2 , board)
	print(prod)
}

func toboggan(x , y int , board []string) int {
	total := 0
	xc := x 
	width := len(board[0])
	for i := y ; i < len(board) ; i += y {
		if board[i][xc] == '#' {
			total += 1
		}
		xc = (xc + x) % width
	}
	return total
}

func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

