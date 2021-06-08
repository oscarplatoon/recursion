let fact = require('./recursionChallenge')

console.log(fact.factorial(-1) == null)
console.log(fact.factorial('something') == null)
console.log(fact.factorial(2) == 2)
console.log(fact.factorial(3) == 6)
console.log(fact.factorial(8) == 40320)

