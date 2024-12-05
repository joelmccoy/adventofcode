package main

import (
	"fmt"
	"log"
	"os"
	"regexp"
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

func getText(f string) string {
	file, err := os.Open(f)

	if err != nil {
		log.Panicf("failed to open file")
	}
	defer file.Close()

	data, err := os.ReadFile(f)
	if err != nil {
		log.Panicf("failed to read file")
	}
	return string(data)

}

func filterText(t string) string {
	re := regexp.MustCompile(`(do\(\)|don't\(\))`)
	var builder strings.Builder

	// Split and find matches
	matches := re.Split(t, -1)
	delimiters := re.FindAllString(t, -1)

	// Combine parts and matches into a single list
	result := []string{}
	for i, part := range matches {
		result = append(result, part) // Add the part of the split string
		if i < len(delimiters) {
			result = append(result, delimiters[i]) // Add the matched delimiter
		}
	}

	for i, str := range result {
		if i == 0 {
			builder.WriteString(str)
			continue
		}

		if str == "don't()" || str == "do()" {
			continue
		}

		if result[i-1] == "don't()" {
			continue
		}

		builder.WriteString(str)
	}

	return builder.String()
}

func process(text string) int {
	sum := 0

	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)

	matches := re.FindAllStringSubmatch(text, -1)
	for i := range matches {
		x, y := toInt(matches[i][1]), toInt(matches[i][2])

		sum += x * y
	}
	return sum

}

func sol1(f string) int {
	text := getText(f)
	return process(text)
}

func sol2(f string) int {
	text := getText(f)

	filtered := filterText(text)

	return process(filtered)
}

func main() {
	fmt.Println(sol1("input.txt"))
	fmt.Println(sol2("input.txt"))
}
