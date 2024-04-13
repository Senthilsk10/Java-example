package com.crud.cruddemo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MathController {

    @GetMapping("/divide/{dividend}/{divisor}")
    public String divide(@PathVariable int dividend, @PathVariable int divisor) {
        if (divisor == 0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        int result = dividend / divisor;
        return "Result of " + dividend + " / " + divisor + " = " + result;
    }
}

