package main

import "testing"

func TestSol1(t *testing.T) {
	expected := 2
	actual := sol1("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}

func TestSol2(t *testing.T) {
	expected := 4
	actual := sol2("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}

func TestCheckReport(t *testing.T) {
	input := []int{88, 86, 88, 89, 90, 93, 95}

	expected := true
	actual := checkReport(input, true)

	if actual != expected {
		t.Error("input is not accepted")
	}
}
