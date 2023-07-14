package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	T, err := strconv.Atoi(scanner.Text())
	errHandler(err)

	for i := 1; i <= T; i++ {
		scanner.Scan()
		n, err := strconv.Atoi(scanner.Text())
		errHandler(err)
		scanner.Scan()
		str := scanner.Text()

		fmt.Println(intSlice(str, n))
	}
}

func errHandler(err error) {
	if err != nil {
		panic(err)
	}
}

func intSlice(str string, n int) int {
	strSlice := strings.Fields(str)
	ratings := make([]int, len(strSlice))
	ans := n
	for j := 1; j <= n; j++ {
		d, err := strconv.Atoi(strSlice[j-1])
		errHandler(err)
		ratings[j-1] = d
		if d < 1000 {
			ans = ans - 1
		}
	}
	return ans
}
