#include <stdio.h>

char arr[50] = "uiuctf{welcome_to_wasm_e3c3bdd1}\0";

int main() {
	printf("hello, world!\n");
	arr[49] = 'c'; // force the array to not be optimized out
	return 0;
}

