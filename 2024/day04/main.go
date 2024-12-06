package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Point struct {
	X int
	Y int
}

func (p Point) Add(other Point) Point {
	return Point{
		X: p.X + other.X,
		Y: p.Y + other.Y,
	}
}

func getPuzzle(f string) [][]rune {
	var puzzle [][]rune
	file, err := os.Open(f)

	if err != nil {
		log.Panicf("failed to open file")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		puzzle = append(puzzle, []rune(line))
	}
	return puzzle
}

func search(puzzle [][]rune, pos Point, delta Point) bool {
	maxX, maxY := len(puzzle[0])-1, len(puzzle)-1
	//out of bounds
	if pos.X+(delta.X*3) > maxX || pos.X+(delta.X*3) < 0 || pos.Y+(delta.Y*3) > maxY || pos.Y+(delta.Y*3) < 0 {
		return false
	}

	word := []rune{'M', 'A', 'S'}

	cur := pos.Add(delta)
	for i := 0; i < 3; i++ {
		if puzzle[cur.X][cur.Y] != word[i] {
			return false
		}
		cur = cur.Add(delta)
	}

	return true
}

func findNumXmas(puzzle [][]rune) int {
	num := 0
	for i, row := range puzzle {
		for j, char := range row {
			if char == 'X' {
				pos := Point{i, j}

				//check up
				if search(puzzle, pos, Point{X: -1, Y: 0}) {
					num += 1
				}

				//check top right
				if search(puzzle, pos, Point{X: -1, Y: 1}) {
					num += 1
				}

				//check right
				if search(puzzle, pos, Point{X: 0, Y: 1}) {
					num += 1
				}

				//check bottom right
				if search(puzzle, pos, Point{X: 1, Y: 1}) {
					num += 1
				}

				//check down
				if search(puzzle, pos, Point{X: 1, Y: 0}) {
					num += 1
				}

				//check bottom left
				if search(puzzle, pos, Point{X: 1, Y: -1}) {
					num += 1
				}

				//check left
				if search(puzzle, pos, Point{X: 0, Y: -1}) {
					num += 1
				}

				//check top left
				if search(puzzle, pos, Point{X: -1, Y: -1}) {
					num += 1
				}
			}
		}
	}
	return num
}

func sol1(f string) int {
	return findNumXmas(getPuzzle(f))
}

func main() {
	fmt.Println(sol1("input.txt"))
}
