import calDoc from './day1.1_input_output.js';

let totalSum = 0;

for (const currentWord of calDoc) {
    let firstNumber;
    let lastNumber;

    for (let i = 0; i < currentWord.length; i++) {
        let character = currentWord[i];

        if (!isNaN(character)) {
            firstNumber = +character;
            break; 
        }
    }

    for (let i = currentWord.length - 1; i > -1; i--) {
        let character = currentWord[i];

        if (!isNaN(character)) {
            lastNumber = +character;
            break; 
        }
    }

    const calibratedValue = `${firstNumber}${lastNumber}`
    totalSum += +calibratedValue
}
console.log(`Total sum of calibrated values: ${totalSum}`);