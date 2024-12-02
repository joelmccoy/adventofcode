package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
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

func diff(a int, b int) int {
	if a >= b {
		return a - b
	}
	return b - a
}

func getLists(f string) ([]int, []int) {
	file, err := os.Open(f)
	list1, list2 := []int{}, []int{}

	if err != nil {
		log.Panicf("failed to open file")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		nums := strings.Fields(scanner.Text())
		list1 = append(list1, toInt(nums[0]))
		list2 = append(list2, toInt(nums[1]))
	}

	sort.Ints(list1)
	sort.Ints(list2)

	return list1, list2
}

func sol1(f string) int {
	list1, list2 := getLists(f)

	distance := 0

	for i := range list1 {
		distance += diff(list1[i], list2[i])
	}
	return distance
}

func getFreq(list2 []int) map[int]int {
	freq := map[int]int{}

	for i := range list2 {
		freq[list2[i]] += 1
	}

	return freq
}

func sol2(f string) int {
	list1, list2 := getLists(f)
	freq := getFreq(list2)

	similarity := 0

	for i := range list1 {
		similarity += (list1[i] * freq[list1[i]])
	}

	return similarity
}

func main() {
	fmt.Println(sol1("input.txt"))
	fmt.Println(sol2("input.txt"))
}
