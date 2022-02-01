// Here is where I add the rest of the functions. Like all the calculators we want to see the numbers on the display and 
// the operations we have done. So we create a new class constructor
class Display {
    constructor(displayCount, displayResult) {
        // here we bring the values from our elements
        this.displayCount = displayCount;
        this.displayResult = displayResult;
        // Here is the calculator functions
        this.calculator = new Calculator();
        // We tell the program we want to start with empty values on the display
        this.operationType = undefined;
        this.actualValue = '';
        this.lastValue = '';
        this.signOp = {
            sum: '+',
            sub: '-',
            multiply: 'x',
            divide: '/',
            percentage: '%'
        }
    }

    // This is for delete the last number if it´s wrong
    delete() {
        this.actualValue = this.actualValue.slice(0, -1);
        this.printValues();
    };

    reset() {
        this.actualValue = '';
        this.lastValue = '';
        this.operationType = undefined;
        this.printValues();
    }

    negative() {
        this.actualValue = -Math.abs(this.actualValue);
        this.printValues();
    }

    calculate(type) {
        this.operationType !== 'equal' && this.operation();
        this.operationType = type;
        this.lastValue = this.actualValue || this.lastValue;
        this.actualValue = '';
        this.printValues();
    }
    // now is time for the methods so we can input numbers =>

    addNumber(num) {
        // We ensure that you can only put one dot
        if(num === '.' && this.actualValue.includes('.')) {
            return
        };
        // We pass all to strings, so to ensure that happend put all .toString() method
        this.actualValue = this.actualValue.toString() + num.toString();
        // print values
        this.printValues()
    };

    // function to collect values and print them later
    printValues() {
        this.displayCount.textContent = this.actualValue;
        this.displayResult.textContent = `${this.lastValue} ${this.signOp[this.operationType] || ''}`;
    };

    // Now we need to change again our values to numbers so we use parseFloat() method
    operation() {
        // don´t forget to create a variable so we can put our numbers there
        const lastValue = parseFloat(this.lastValue);
        const actualValue = parseFloat(this.actualValue);

        // then we ensure if our numbers are correct, they are not NaN => isNaN()
        if(isNaN(actualValue) || isNaN(lastValue)) return;
        
        this.actualValue = this.calculator[this.operationType](lastValue, actualValue);
    }
}