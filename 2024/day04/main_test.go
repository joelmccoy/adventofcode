package main

import "testing"

func TestSol1(t *testing.T) {
	expected := 18
	actual := sol1("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}

func TestSol2(t *testing.T) {
	expected := 9
	actual := sol2("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}
