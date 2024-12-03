package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func toInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		log.Panicf("failed to convert string to int")
	}
	return num
}

func getReports(f string) [][]int {
	var reports [][]int
	file, err := os.Open(f)

	if err != nil {
		log.Panicf("failed to open file")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		nums := strings.Fields(scanner.Text())
		row := []int{}
		for _, num := range nums {
			row = append(row, toInt(num))
		}
		reports = append(reports, row)
	}
	return reports
}

func isInc(a int, b int) bool {
	if a >= b {
		return false
	}
	return true
}

func diff(a int, b int) int {
	if a >= b {
		return a - b
	}
	return b - a
}

func validDiff(a int, b int) bool {
	d := diff(a, b)
	if d > 0 && d <= 3 {
		return true
	}
	return false
}

func removeIndex(slice []int, index int) []int {
	if index < 0 || index >= len(slice) {
		// Return the original slice if the index is out of bounds
		return slice
	}

	// Create a new slice with one less capacity
	result := make([]int, 0, len(slice)-1)

	// Append elements before the index
	result = append(result, slice[:index]...)

	// Append elements after the index
	result = append(result, slice[index+1:]...)

	return result
}

func checkReport(report []int, tolerate bool) bool {
	is_inc := true

	if len(report) <= 1 {
		return true
	}

	if report[0] == report[1] {
		if tolerate {
			return checkReport(removeIndex(report, 0), false) || checkReport(removeIndex(report, 1), false)
		}
		return false
	}

	if report[0] > report[1] {
		is_inc = false
	}

	//edge case to check for removing first index
	if tolerate && checkReport(removeIndex(report, 0), false) {
		return true
	}

	for i := range report[:len(report)-1] {
		a, b := report[i], report[i+1]
		if isInc(a, b) == is_inc && validDiff(a, b) {
			continue
		} else {
			if tolerate {
				// remove the bad value and retry the check all over again with tolerate as false
				return checkReport(removeIndex(report, i), false) || checkReport(removeIndex(report, i+1), false)
			}
			return false
		}
	}

	return true
}

func sol1(f string) int {
	safe := 0
	reports := getReports(f)

	for i := range reports {
		if checkReport(reports[i], false) {
			safe += 1
		}
	}

	return safe
}

func sol2(f string) int {
	safe := 0
	reports := getReports(f)

	for i := range reports {
		if checkReport(reports[i], true) {
			safe += 1
		}
	}

	return safe
}

func main() {
	fmt.Println(sol1("input.txt"))
	fmt.Println(sol2("input.txt"))
}
