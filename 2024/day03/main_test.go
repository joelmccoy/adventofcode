package main

import "testing"

func TestSol1(t *testing.T) {
	expected := 161
	actual := sol1("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}

func TestSol2(t *testing.T) {
	expected := 48
	actual := sol2("sample2.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}
