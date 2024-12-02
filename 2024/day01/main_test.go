package main

import "testing"

func TestSample1(t *testing.T) {
	expected := 11
	actual := sol1("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}

func TestSample2(t *testing.T) {
	expected := 31
	actual := sol2("sample.txt")

	if actual != expected {
		t.Errorf("expected was %d, but got %d", expected, actual)
	}
}
